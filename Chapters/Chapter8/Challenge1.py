import arcpy
import fileinput
import string
import os
from arcpy import env

env.workspace = "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise08"
env.overwriteOutput = True
outpath = "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise08"
newfc = "Results/square.shp"

arcpy.CreateFeatureclass_management(outpath, newfc, "Polygon")
infile = "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise08/Results/square.txt"
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
for line in fileinput.input(infile):
    parts = string.split(" ")
    id = parts[0] 
    coord1 = "({},{})".format(parts[1], parts[2])
    coord2 = "({},{})".format(parts[3], parts[4])
    coord3 = "({},{})".format(parts[5], parts[6])
    coord4 = "({},{})".format(parts[7], parts[8]) 
    
    array.add(arcpy.Point(X, Y))
cursor.insertRow([arcpy.Polygon(array)])
fileinput.close()
del cursor
