#! /usr/bin/env python
#coding=utf-8
'''process the search'''
import numpy as np
import csv
class searcher(object):
    def __init__(self,csvpath):
        self.csvpath = csvpath
    def get_distance(self,hista,histb,eps = 1e-10):
        '''get the distance between two histgram'''
        dis = 0.5 * op.sum([((a-b)**2,(a+b+eps)) for (a,b) in zip(hista,histb)])
        return dis
    def findbasefeat(self,givenfeat,limit = 10):
        result = {}
        csvfile = open(self.csvpath,"w")
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            features = [float(x) for x in row[1:]]
            d = self.dis(features,givenfeat)
            result[row[0]] = d
        
        csvfile.close()
        
        result = sorted((v,k) for (k,v) in result.iteritems() )
        
        return result[:limit]
        