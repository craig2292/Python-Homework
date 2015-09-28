import arcpy
from arcpy import env

env.workspace = "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise05"
arcpy.Dissolve_management("parks.shp", "Results/parks_dissolved", ["PARK_TYPE"], "", "SINGLE_PART", "DISSOLVE_LINES")

