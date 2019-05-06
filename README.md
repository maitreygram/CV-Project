# CV-Project

# CV-Project

## Objective
**1.** Feature based
sparse slam'
3d map construction
monocular slam

### We present an algorithm to recover 3D trajectory of a camera using feature based sparse slam using a single camera (also called MonoSLAM).     

##  Method of Approach
**1.** Feature extraction
We used the feature trackers present in the opencv library (goodFeaturestotrack and ORB feature tracker). 

**2.** Feature Matching
We calculate the distance between all the two points using brute force approach. We estimate the 2 nearest neighbour of every point using knn clustering and eliminate the points/pairs using ratio test. In the next step, we estimate the essential matrix using 8 point algorithm. For that we convert the image coordinates to camera cordinates and check for a minimum of 8 feature points. We eliminate the outliers using thresholding and ransac.       

pose estimation
We estimate the pose of the current frame using the Essential matrix. See references[2].

World coordinates

Displaylowe's a

## Dataset
Driving stock video

## list of code dependencies
- opencv
- openGL
- pygame
- pangolin
- multiprocessing
- matplotlib
- numpy
- skimage
for python3 

## How to run the code

## Results

## Discussions

##installation instructions and run main.py

## References



## Objective
**1.** Feature based
sparse slam'
3d map construction
monocular slam

### We present an algorithm to recover 3D trajectory of a camera using feature based sparse slam. We implement monocular slam for    

##  Method of Approach
# CV-Project

## Objective
**1.** Feature based
sparse slam'
3d map construction
monocular slam

### We present an algorithm to recover 3D trajectory of a camera using feature based sparse slam. We implement monocular slam for    

##  Method of Approach
**1. 
feature extraction
feature matching
pose estimation
World coordinates
Display

## Dataset
Driving stock video

## list of code dependencies
- opencv
- openGL
- pygame
- pangolin
- multiprocessing
- matplotlib
- numpy
- skimage
for python3 

## How to run the code

## Results

## Discussions

##installation instructions and run main.py

## References




feature extraction
feature matching
pose estimation
World coordinates
Display

## Dataset
Driving stock video

## list of code dependencies
- opencv
- openGL
- pygame
- pangolin
- multiprocessing
- matplotlib
- numpy
- skimage
for python3 

## How to run the code

## Results

## Discussions

##installation instructions and run main.py

## References



