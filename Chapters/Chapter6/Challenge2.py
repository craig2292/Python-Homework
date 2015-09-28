import os.path
import arcpy
from arcpy import env

env.workspace = "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise06"
if not os.path.isdir(env.workspace + '/Results/mydb.gdb'):
    print ("Creating File GDB")
    arcpy.CreateFileGDB_management("P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise06/Results", "mydb.gdb")


env.workspace = "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise06/Results/NM.gdb"
print ("Printing Feature Classes")
for feature in arcpy.ListFeatureClasses():
    dataset = arcpy.Describe(feature)
    if dataset.shapeType == "Polygon":
        print dataset.name
        arcpy.CopyFeatures_management(feature, "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise06/Results/mydb.gdb/" + dataset.name)
