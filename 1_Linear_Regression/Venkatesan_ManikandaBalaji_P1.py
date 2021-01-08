# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 16:52:59 2021

@author: Manikanda
"""
import numpy as np
import matplotlib.pyplot as plt

def main():
   #fileName = input("Enter the name of your data file: ")
   fileName = "housing_training.txt"
   #extracting info about dataset
   dataFile = open(fileName,"r")
   info = dataFile.readline()
   info = info.split("\t")
   rows = int(info[0])
   features = int(info[1])
   m = rows
   print("rows ",rows,"features ",features)
   
   #extraction of data into arrays
   data = np.zeros([rows,features+1])
   for i in range(rows):
       dataLine = dataFile.readline()
       dataLine = dataLine.split("\t")
       for j in range(features+1):
           data[i,j] = float(dataLine[j])
   
   #X matrix
   X = np.ones([rows,features+1])
   for i in range(features):
       X[:,i+1] = data[:,i]
   
   #y matrix
   y = np.zeros([rows,1])
   y[:,0] = data[:,features]
   
   #weights calculation
   A = np.linalg.pinv(np.dot(X.T, X))
   B = np.dot(X.T, y)
   w = np.dot(A, B)
   
   # j value calculation
   A = np.dot(X, w) - y
   J = (1/m)*np.dot(A.T, A)
   print(J)
           
     
           
           
if __name__ == "__main__":
    main()