# Meters2Pixels  
## Overview 
Find an Object height in pixels in an image from Real World Coordinates. 

Inputs:
* distance - distance of the person from Camera in meters
* fov - Field of View of Camera in degrees
* person_height - Height of the Person in meters
* sensor_height - Height of the Sensor in millimeter (Can be found in the datasheet of the Camera)
* image_height - Height of the image in pixels (eg. for FHD Image, image_height is 1080)

This code provides a rough estimate of object size in meters from Real World depth in meters converted to Image plane (in pixels). Please note that this is an approximation and may not be accurate for all cameras and situations.

