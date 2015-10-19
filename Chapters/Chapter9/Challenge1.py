import arcpy
from arcpy import env
env.workspace = "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise09"

if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")
elevraster = arcpy.Raster("elevation")
lcraster = arcpy.Raster("landcover.tif")
slope = Slope(elevraster)
aspect = Aspect(elevraster)
goodslope = ((slope > 5) & (slope < 20))
goodaspect = ((aspect > 150) & (aspect < 270))
goodland = ((lcraster == 41) | (lcraster == 42) | (lcraster == 43))
outraster = (goodslope & goodaspect & goodland)
outraster.save("P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise09/outraster")
arcpy.CheckInExtension("Spatial")
