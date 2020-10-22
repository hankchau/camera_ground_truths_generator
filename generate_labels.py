import os
import subprocess


class Box:
    '''Bounding Box detected by YOLO.'''

    def __init__(self):
        '''Constructor for Box.'''
        self.x = 0.0
        self.y = 0.0
        self.width = 0.0
        self.height = 0.0
        self.left = 0.0
        self.top = 0.0
        self.right = 0.0
        self.bot = 0.0


def run_yolo(inpath):
    '''Classify input images with YOLO w/ subprocess.'''
    outpath = inpath + 'output.txt'
    inpath += 'image_paths.txt'

    subprocess.run('make')
    cmd = ['./darknet', 'detect', 'cfg/yolov3.cfg', 'yolov3.weights', '-thresh', '0.98']

    input = open(inpath, 'r')
    output = open(outpath, 'w')
    subprocess.run(cmd, stdin=input, stdout=output)

    input.close()
    output.close()

    return outpath


def read_items(filepath):
    '''Parse output.txt.'''
    with open(filepath, 'r') as f:
        lines = f.readlines()

    images = []
    cars = []   # bounding boxes for detections that were cars
    i = 1
    while i < len(lines):
        if 'Enter' in lines[i]:
            images.append(cars)
            cars = []
        elif 'car' in lines[i]:
            cars.append(Box())
        elif 'Bounding Box: ' in lines[i]:
            line = lines[i].replace('Bounding Box: ', '')
            line = line.replace('=', ' ')
            line = line.split(' ')
            cars[-1].left, cars[-1].top = float(line[1]), float(line[3])
            cars[-1].right, cars[-1].bot = float(line[5]), float(line[7].replace('\n',''))
        else:
            line = lines[i].split(' ')
            cars[-1].x, cars[-1].y = float(line[0]), float(line[1])
            cars[-1].width, cars[-1].height = float(line[2]), float(line[3])
        i += 1

    return images


def main():
    inpath = 'data/parking_lot/output/'
    outpath = 'data/parking_lot/output/ground_truths.txt'

    # inpath = 'data/parking_lot_sample/output/'
    # outpath = 'data/parking_lot_sample/output/ground_truth.txt'

    # still experimenting with this method
    '''     
    x0, x0_error = 0.0, 2.0
    x1, x1_error = 180, 15.0
    x2, x2_error = 610, 15.0
    x3, x3_error = 799.0, 2.0

    # NOTE: y0 not used for now
    y0, y0_error = 80.0, 15.0
    y1, y1_error = 260.0, 30.0
    '''     # still experimenting with this method

    # each slot's X-coordinate and Margin of Error for bounding boxes
    x0, x0_error = 0.11, 0.08
    x1, x1_error = 0.30, 0.11
    x2, x2_error = 0.67, 0.10
    x3, x3_error = 0.88, 0.08

    # Y-coordinates' range for Y-Coordinate for bounding boxes
    y, y_error = 0.30, 0.06

    filepath = run_yolo(inpath)
    images = read_items(filepath)

    # classify slots
    predictions = []

    for cars in images:
        slot0, slot1, slot2, slot3 = '0', '0', '0', '0'  # 0 = False
        for c in cars:
            # within Y-range
            if abs(c.y - y) <= y_error:
                # within X-range
                if abs(c.x - x0) <= x0_error:
                    slot0 = '1'
                if abs(c.x - x1) <= x1_error:
                    slot1 = '1'
                if abs(c.x - x2) <= x2_error:
                    slot2 = '1'
                if abs(c.x - x3) <= x3_error:
                    slot3 = '1'
        predictions.append([slot0, slot1, slot2, slot3])

    print(predictions)

    with open(outpath, 'w') as f:
        for pred in predictions:
            f.write(' '.join(pred) + '\n')


if __name__ == '__main__':
    main()
