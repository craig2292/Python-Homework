import arcpy
from arcpy import env

env.workspace = "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise05"

if arcpy.CheckExtension("3D") == "Available":
    arcpy.CheckOutExtension("3D")
    arcpy.CheckInExtension("3D")
else:
    print "The extension 3D analyst is not available."

if arcpy.CheckExtension("network") == "Available":
    arcpy.CheckOutExtension("network")
    arcpy.CheckInExtension("network")
else:
    print "The extension network analyst is not available."

if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckInExtension("spatial")
else:
    print "The extension spatial analyst is not available."
    
