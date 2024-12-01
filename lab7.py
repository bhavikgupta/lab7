import arcpy

##### TASK 1 ######

## Define Paths
Dem=r'D:/Lab7/n30_w097_1arc_v3.tif'
hillshade_output=r'D:/Lab7/Hillshade.tif'
slope_output=r'D:/Lab7/Slope.tif'

## Calculate Hillshade
arcpy.ddd.HillShade(
    Dem,   # 'DEM' file path
    hillshade_output,  # output tif file path.
    315,             # the default value of this dataset's azimuth (315)
    45,              # the default value of this dataset (45)
    "NO_SHADOWS",    # w so set "NO_SHADOWS" to this param
    1,               # default value is 1
)

## Calculate Slope
arcpy.ddd.Slope(
    Dem,   # DEM' file path
    slope_output,  # output tif file path.
    "DEGREE",      # the default value of this dataset's ("DEGREE")
    1,               #  the default value of this dataset's z_factor (1)
)

### TASK 2 ######

# Define paths for bands
red_band_path=r"D:\\Lab7\\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B3.tiff"
green_band_path=r"D:\\Lab7\\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B2.tiff"
blue_band_path=r"D:\\Lab7\\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B1.tiff"
compsite_output=r"D:\\Lab7\\compbands.tif"

## Loads bands in arcpy 
band_RED = arcpy.sa.Raster(red_band_path) #  band represents RED value.
band_GREEN = arcpy.sa.Raster(green_band_path) # band represents GREEN value.
band_BLUE = arcpy.sa.Raster(blue_band_path) # band represents BLUE value.

# ********************
# BE CAREFUL
# The order of the list of the bands' objs should follow the order of R-G-B to get a correct RGB composite raster.
# ********************

## Compsite bands
arcpy.management.CompositeBands(
    [band_RED, band_GREEN, band_BLUE],compsite_output
)



##### TASK 2-2 #######

## Define paths for bands
BASE_DIR=r"D:\Lab7"
band_RED = arcpy.sa.Raster(f"{BASE_DIR}\\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B3.tiff")
band_GREEN = arcpy.sa.Raster(f"{BASE_DIR}\\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B2.tiff")
band_BLUE = arcpy.sa.Raster(f"{BASE_DIR}\\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B1.tiff")
band_NIR = arcpy.sa.Raster(f"{BASE_DIR}\\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B4.tiff")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>
# Add your code here
# Compute the NDVI values
# formula: NDVI_ESRI = ((NIR - RED)/(NIR + RED))*100 + 100

## NDVI calculation
NDVI_ESRI = ((band_NIR - band_RED)/(band_NIR + band_RED))*100 + 100
band_NDVI = NDVI_ESRI

## Saved NDVI band
band_NDVI.save(f"{BASE_DIR}\\ESRI_NDVI.TIF")

