#! /usr/bin/env python
#coding=utf-8
''' build a CSV file containing all features of given dataset'''
from clrdescriptor import descriptor
import argparse
import glob
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-d","--dataset",required = True,
                help = "the path to directory where the dataset to extract features")
ap.add_argument("-i","--imgindex",required = True,
                help = "the index of the image to compute")

args = vars(ap.parse_args())

cd = descriptor((8,12,3))
#open a CSV file
output = open(args["imgindex"],"w")

for imgpath in glob.glob(args["dataset"] + "/*.jpg"):
    #get name of an image
    imgname = imgpath[imgpath.rfind("/") + 1:]
    img = cv2.imread(imgname)
    #describe features of the image
    features = cd.describe(img)
    features = [str(f) for f in features]
    #write the features and save them
    output.write("%s,%s\n"%(imgname,",".join(features)))
    
output.close()    
    