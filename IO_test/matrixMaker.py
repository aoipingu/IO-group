"""
This script provides 2 functions:
    make_simple_matrix: This function takes a folder with images named Layer0000,Layer0001... and makes a 3d array containing the H,S and V color
    values of each position for later processing. The function will take the cropped images obtained from the Visual Human Project by another part
    of the code.
    assign_tags: This function uses data from a materials dictionary and from the config to assign a tissue type (or air) to the different voxels of
    the 3D array of HSV values. It outputs a matrix with integer tissue tags and luminosity values for each voxel. For instance, for a matrix named M
    one can adress a tissue tag by doing M[x,y,z,0] and the luminosity with M[x,y,z,1]
    
Authos: Carlos Barbero
"""
import cv2 as cv
import numpy as np
import os.path
import sys

import csv
from numpy.core.fromnumeric import size
import materialclass

#to find hsv of different colours -------
# green = np.uint8([[[0,255,0 ]]])
# hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
# print (hsv_green)
IMAGE_FILE_EXTENSION = ".png"

def make_simple_matrix(folder_path):
    """this function gets the path to a folder with images named Layer0000, Layer0001, Layer0002 ... and so on from the visual human project
    from bottom to top.
    It returns a numpy 3d array of the HSV colour values of the body part for later processing."""
    #we fist need the size of the image and the number of images to define the numpy array size------
    fileCount = 0
    while os.path.exists(folder_path + f"/Layer{fileCount :04d}" + IMAGE_FILE_EXTENSION):
        fileCount += 1
    if fileCount == 0:
        raise ValueError("No files in folder path named Layer0000...")
    else:
        LAYER_NUMBER = fileCount;
        #check resolution of one image and finally get the numpy array for the matrix
        img = cv.imread(folder_path + f"/Layer0000" + IMAGE_FILE_EXTENSION, cv.IMREAD_COLOR)
        IMG_WIDTH = np.size(img,0)
        IMG_HEIGHT = np.size(img,1)
        print(f"Array width is {IMG_WIDTH}, and height {IMG_HEIGHT} with {LAYER_NUMBER} layers.")
        simpleMatrix = np.zeros((IMG_WIDTH,IMG_HEIGHT,LAYER_NUMBER,3), dtype= int) #4 dimensional array that has spacial axis and the 3 colours of HSV
        #Go through each image and add it to the matrix
        for layer in range(0,LAYER_NUMBER):
            image_path = folder_path + f"/Layer{layer :04d}" + IMAGE_FILE_EXTENSION
            img = cv.imread(image_path,cv.IMREAD_COLOR)
            for i in range(0,IMG_WIDTH):
                for j in range(0,IMG_HEIGHT):
                    HSV_values = cv.cvtColor(np.uint8([[img[i,j]]]),cv.COLOR_BGR2HSV)
                    simpleMatrix[i,j,layer] = HSV_values
    return simpleMatrix

def assign_tags(sMatrix, materials, tolerance = 0):
    """takes the HSV colour values from the simple matrix and a dictionary of materials objects to then return a 3D Matrix. Needs the colour tolerances from the config file"""
    tagMatrix = np.zeros((np.size(sMatrix,0),np.size(sMatrix,1),np.size(sMatrix,2),2), dtype= float) #3d matrix to store the tissue type tags with a 4th dimension for luminosity
    for i in range(0,np.size(sMatrix,0)):
        for j in range(0,np.size(sMatrix,1)):
            for k in range(0,np.size(sMatrix,2)):
                for tag in materials:
                    materialHSV= np.array(materials[tag].hsv)
                    if cv.inRange(sMatrix[i,j,k,:],materialHSV-tolerance,materialHSV+tolerance)[0]==255:#the inRange function is meant to work for making masks and so it returs [255] if True
                        #print (f"decided {tag} for ({i},{j},{k})")
                        tagMatrix[i,j,k,0] = tag

    return tagMatrix
                        
#TEST /// MAY BE COMMENTED -----------------------------------------------------------------------------
#make dictionary for test materials ------
with open("testing_materials.csv", newline='') as csvfile: # Probably change the name of the csv.
    data = list(csv.reader(csvfile))
#mat_dict is the master dictionary with the tag as the key and the material class as the value.
mat_dict = materialclass.Materials.data_to_dict(data)
for i in mat_dict:
    print(f"colour {mat_dict[i].name} with tag {i}")
simpleMatrix = make_simple_matrix("testing_images/basic_colours_small")
complexMatrix = assign_tags(simpleMatrix, mat_dict)
np.set_printoptions(threshold=sys.maxsize)
# print(simpleMatrix[:,:,0])
print(complexMatrix[:,:,0,0])
print(complexMatrix[:,:,0,1])
