#! /usr/bin/env python
#coding=utf-8
__author__ = 'niu ming'
import numpy as np
import cv2

class descriptor(object):
    '''
    extract features of a given image.
    '''
    def __init__(self,bins):
        '''initialize the descriptor by set the number of features vector'''
        self.bins = bins
        
    def describe(self,image):
        '''the process of getting the features'''
        features = []
        image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        (w,h) = image.shape[:2]
        #get the center of image
        (xcenter,ycenter) = (int(w/2),int(h/2))
        seg = [(0,xcenter,0,ycenter),(xcenter,w,0,ycenter),
               (xcenter,w,ycenter,h),(0,xcenter,ycenter,h)]
        #set the width and height of a eclipse
        (ecl_x,ecl_y) = (int(w * 0.75 / 2),int(h * 0.75 / 2))
        eclipsemask = np.zeros(image.shape[:2],dtype = "uint8")
        cv2.ellipse(eclipsemask,(xcenter,ycenter),(ecl_x,ecl_y),0,0,255,-1)
        
        for (xbeg,xend,ybeg,yend) in seg:
            rectmask = np.zeros(image.shape[:2],dtype = "uint8")
            cv2.rectangle(rectmask,(xbeg,ybeg),(xend,yend),255,-1) 
            rectmask = cv2.subtract(rectmask,eclipsemask)
            
            hist = self.histcalc(image,rectmask)
            
            features.extend(hist)
        hist = self.histcalc(image,eclipsemask)
        features.extend(hist)
        return features
        
    def histcalc(self,image,mask):
        '''
        calculate the histgram of given image,which should be a 3d one
        containing given bins
        '''
        hist = cv2.calcHist([image],[0,1,2],mask,self.bins,[0,180,0,256,0,256])
        hist = cv2.normalize(hist).flatten()
        return hist
        