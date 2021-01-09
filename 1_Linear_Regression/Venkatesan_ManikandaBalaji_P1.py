# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 16:52:59 2021

@author: Manikanda
"""
import numpy as np
import matplotlib.pyplot as plt

def load_dataset(fileName):
    dataFile = open(fileName,"r")
    info = dataFile.readline()
    info = info.split("\t")
    rows = int(info[0])
    features = int(info[1])
    print("rows ",rows,"features ",features) 
    #extraction of data into arrays
    data = np.zeros([rows,features+1])
    for i in range(rows):
        dataLine = dataFile.readline()
        dataLine = dataLine.split("\t")
        for j in range(features+1):
            data[i,j] = float(dataLine[j])
    return rows, features, data

def weight_matrices(rows,features,data):
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
   return A,B,X,y    
    
def j_calculation(w,A,X,y):
   # j value calculation
   m = A.shape[0]
   A = np.dot(X, w) - y
   J = (1/m)*np.dot(A.T, A)
   return J

def main():
   #training dataset
   #fileName = input("Enter the name of your data file: ")
   fileNameTrain = "housing_training.txt"
   rowsTrain, featuresTrain, dataTrain = load_dataset(fileNameTrain)
   ATrain, BTrain, XTrain, yTrain = weight_matrices(rowsTrain, featuresTrain, dataTrain)
   w = np.dot(ATrain, BTrain)
   jTrain = j_calculation(w, ATrain, XTrain, yTrain)    
   print("J value of training dataset is ",jTrain[0,0])
   
   #test dataset
   #fileName = input("Enter the name of your data file: ")
   fileNameTest = "housing_testing.txt"
   rowsTest, featuresTest, dataTest = load_dataset(fileNameTest)
   ATest, BTest, XTest, yTest = weight_matrices(rowsTest, featuresTest, dataTest)
   jTest = j_calculation(w, ATest, XTest, yTest)    
   print("J value of testing dataset is ",jTest[0,0])
        
if __name__ == "__main__":
    main()