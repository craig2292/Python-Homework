import arcpy
from arcpy import env

env.workspace = "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise06/Results"
fclasses = arcpy.ListFeatureClasses()
for fclass in fclasses:
    fctype = arcpy.Describe(fclass).shapeType
    print "{0} is a {1} feature class".format(fclass, fctype)
    
