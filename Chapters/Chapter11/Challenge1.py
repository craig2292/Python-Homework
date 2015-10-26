import arcpy
from arcpy import env
env.workspace = "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise07"
fc = "airports.shp"
rows = arcpy.SearchCursor(fc)
fields = arcpy.ListFields(fc)
for field in fields:
    if field.name == "NAME":
        for row in rows:
            print "NAME = {0}".format(row.getValue(field.name))

"""
    on line 4 "FC" needed to be changed to "fc"
    on line 8 "fields.name" needed to be changed to "field.name"
    on line 8 there needed to be a colon (:) at the end of the line
    line 10 need to be indented
"""
