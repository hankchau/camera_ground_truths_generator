# Find Ground-Truth Values for Camera Streams #
This is a vanilla program to find the ground-truth values of a camera stream in conjunction with YOLOv3. This program was written to suit the needs of my specific project. Feel free to change it to fit for other cases. 

<br/>
Credits: Please refer to https://pjreddie.com/darknet/yolo/ for more info on YOLOv3.

## How to Use:
– 1. Follow the guide in the link above to download the CNN model and pre-trained weights for YOLOv3.<br/>
– 2. Once you're done with downloading YOLOv3, place the .py files in this repository under the root folder 'darknet'<br/>
– 3. Replace 'image.c' under 'darknet/src' with the 'image.c' from this repo.<br/>
– 4. Navigate to 'darknet' in Command Line and build 'get_labels.sh' into an executable script with 'chmod +x get_labels.sh'<br/>
– 5. Run the script with './get_labels.sh'.<br/>

Inputs: None<br/>
Outputs:<br/>
– 'darknet/data/parking_lot/': A folder containing collected images (.png) from the camera stream.<br/>
– 'data/parking_lot/ground_truths': A matrix with rows corresponding to the ground-truth values of each parking slot in an image.<br/>
– 'data/parking_lot/image_paths.txt': A file containing the absolute paths of collected images under 'darknet/data/parking_lot' needed by YOLOv3.<br/>  
– 'data/parking_lot/output.txt': Output file from YOLOv3 detailing the boundary boxes and coordinates for each detection.<br/>

## Sample Input:
![image01.png](https://github.com/hankchau/camera_ground_truths_generator/blob/main/parking_lot_sample/image01.png =30x40)
![image04.png](https://github.com/hankchau/camera_ground_truths_generator/blob/main/parking_lot_sample/image04.png =30x40)

## Sample Output:
![alt text](https://github.com/hankchau/camera_ground_truths_generator/blob/main/predictions01.jpg)
![alt text](https://github.com/hankchau/camera_ground_truths_generator/blob/main/predictions04.jpg)
![alt text](https://github.com/hankchau/camera_ground_truths_generator/blob/main/output.png)
![alt text](https://github.com/hankchau/camera_ground_truths_generator/blob/main/ground_truths.jpg)


Note:<br/>
The program currently does not produce images with detection boundary boxes yet. It will be added in a later commit. The<br/>
The decision boundaries for determining each parking slot's (1 - 4) vacancy can be altered for further optimization.<br/>

## Citations: 
@article{yolov3,
  title={YOLOv3: An Incremental Improvement},
  author={Redmon, Joseph and Farhadi, Ali},
  journal = {arXiv},
  year={2018}
}
