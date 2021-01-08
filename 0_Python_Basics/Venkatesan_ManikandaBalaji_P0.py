# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 12:44:37 2021

@author: Manikanda
"""
import numpy as np
import matplotlib.pyplot as plt

#plotting of data points on graph
def graphPlotter(_data,_flowerType,_xAxis,_yAxis):
   for k in range(_data.shape[0]):
      if _flowerType[k] == "setosa":
         plt.scatter(_data[k,_xAxis], _data[k,_yAxis], color =  "green", marker = "v", label = "setosa")
      elif _flowerType[k] == "versicolor":
         plt.scatter(_data[k,_xAxis], _data[k,_yAxis], color =  "blue", marker = "o", label = "setosa")
      elif _flowerType[k] == "virginica":
         plt.scatter(_data[k,_xAxis], _data[k,_yAxis], color =  "red", marker = "+", label = "setosa")
   axisDict = { 0:"sepal length", 1:"sepal width", 2:"petal length", 3:"petal width"}
   plt.xlabel(axisDict[_xAxis])
   plt.ylabel(axisDict[_yAxis])
   plt.show()
   
def main():
   #fileName = input("Enter the name of your data file: ")
   fileName = "Irisdata.txt"
   #extracting info about dataset
   dataFile = open(fileName,"r")
   info = dataFile.readline()
   info = info.split("\t")
   rows = int(info[0])
   features = int(info[1])
   print("rows ",rows,"features ",features)

   #extraction of data into arrays
   data = np.zeros([rows,features+1])
   flowerType = list()
   for i in range(rows):
       dataLine = dataFile.readline()
       dataLine = dataLine.split("\t")
       for j in range(features+1):
           if j == 4:
               flowerType.append(dataLine[j].strip())
               break
           data[i,j] = float(dataLine[j])

   #taking user input for desired plot
   print("""You can do a plot of any two features of the Iris Data set
         The feature codes are:
            0 = sepal length
            1 = sepal width
            2 = petal length
            3 = petal width""")
   xAxis = int(input("Enter feature code for the horizontal axis: "))
   yAxis = int(input("Enter feature code for the vertical axis: "))
   
   while True:
      graphPlotter(data,flowerType,xAxis,yAxis)
      userContinue = input("Would you like to do another plot? (y/n) ")
      if userContinue == "n":
         print("Exiting code")
         break

if __name__ == "__main__":
    main()