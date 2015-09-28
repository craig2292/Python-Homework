import arcpy
from arcpy import env

env.workspace = "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise05"
arcpy.AddXY_management ("hospitals.shp")
