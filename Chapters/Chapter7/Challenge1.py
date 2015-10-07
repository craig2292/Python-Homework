import arcpy
from arcpy import env
env.workspace = "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise07"

fc = "airports.shp"
arcpy.Select_analysis(fc, "Results/airports_sel.shp", '"FEATURE" = \'Airport\'')
arcpy.Buffer_analysis("Results/airports_sel.shp", "Results/airport_buffer.shp", "15000 METERS")
arcpy.Select_analysis(fc, "Results/seaplane_sel.shp", '"FEATURE" = \'Seaplane Base\'')
arcpy.Buffer_analysis("Results/seaplane_sel.shp", "Results/seaplane_buffer.shp", "7500 METERS")


