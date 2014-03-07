divide_and_dissolve
===================

The aim for this code is to make the ESRI dissollve functions faster and more efficient using their own code. In the current release the code uses the ESRI arcpy dissolve function to dissolve spatial geometries. The geometry dissolve using the plain ESRI dissolve functionality is painfully slow. Allowing for cutting the job into smaller peaces makes the overall work faster.

The code aims at beating ESRI on their own half - just using their own code libraries to make analysis faster.

