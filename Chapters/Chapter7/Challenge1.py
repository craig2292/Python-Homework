import arcpy
from arcpy import env
env.workspace = "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise07"

fc = "airports.shp"
airport = arcpy.CreateUniqueName("Results/buffer01.shp")
seaplane = arcpy.CreateUniqueName("Results/buffer02.shp")

arcpy.Buffer_analysis(fc, airport, "15000 METERS")
arcpy.Buffer_analysis(fc, seaplane, "7500 METERS")
print fc


