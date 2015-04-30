#! /usr/bin/env python
#coding=utf-8
'''execute the query process '''
from searchercore import searcher
from clrdescriptor import descriptor
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-q","--query",
                help = "Path to the query image")
ap.add_argument("-i","--index",
                help = "Path to where the computed index will be stored")
ap.add_argument("-r","--result-path",
                help = "Path to the result path")

args = vars(ap.parse_args())


cd = descriptor((8,12,3))
query = cv2.imread(args["query"])
features = cd.describe(query)
 
# perform the search
searcherobg = searcher(args["index"])
results = searcherobg.search(features)
 
# display the query
cv2.imshow("Query", query)
 
# loop over the results
for (score, resultID) in results:
    # load the result image and display it
    result = cv2.imread(args["result_path"] + "/" + resultID)
    cv2.imshow("Result", result)
    cv2.waitKey(0)



