import os
import time
import requests
from PIL import Image
from io import BytesIO


def main():
    url = 'http://140.138.178.29:8090/?action=snapshot'
    outpath = os.path.join(os.getcwd(), 'data/parking_lot/')
    # outpath = os.path.join(os.getcwd(), 'data/parking_lot_sample/')

    # check if output dir exists
    if not os.path.isdir(outpath):
        os.mkdir(outpath)

    sleep_time = 3     # seconds to wait before next attempt
    max_photos = 6     # max number of photos to collect
    counter = 0     # number of photos collected so far

    im_paths = []   # list of all output paths

    while True:
        if counter == max_photos:
            break

        try:
            r = requests.get(url)
            im = Image.open(BytesIO(r.content))

            fname = 'image' + '%03d' % counter + '.png'
            im.save(outpath + fname)
            im_paths.append(outpath + fname)

            counter += 1
            time.sleep(sleep_time)

        except requests.exceptions.ConnectionError:
            print('error: failed to connect to server')
            exit(0)

    outpath = os.path.join(outpath, 'output/')
    os.mkdir(outpath)
    with open(outpath + 'image_paths.txt', 'w') as f:
        for path in im_paths:
            f.write(path + '\n')

    print('Collected a total of ' + str(counter) + ' photos over ' + str(counter * sleep_time) + ' seconds')


if __name__ == '__main__':
    main()
