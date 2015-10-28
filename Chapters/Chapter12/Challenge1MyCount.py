import arcpy
from arcpy import env
env.workspace = "P:/Fall2015/Python/Python Scipting for ArcGIS/Data/Exercise12"

def countstringfields(table):
    """ This function determines the number of fields of type string in an input feature class.
    """
    
    fields = arcpy.ListFields (table)
    i = 0
    for field in fields:
        if field.type == "String":
            i += 1
        return i
