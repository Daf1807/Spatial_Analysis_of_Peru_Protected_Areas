# Peru's Protected Areas Tree Cover Analysis

This project analyzes tree cover in Peru's protected areas using MODIS Vegetation Continuous Fields (VCF) data for 2024 and OpenStreetMap (OSM) data for protected areas. The analysis involves downloading, processing, and mosaicking raster data, reprojecting to EPSG:4326, and calculating tree cover statistics within and around protected areas using buffer zones and regression discontinuity design (RDD).

## Running locally
To run locally, it is advisable to first create a virtual environment.

You will need to have Python installed and in your PATH. While located in the root directory of this repository,

```
python -m venv env
```

Now activate the virtual environment:

**Windows**
```
env\Scripts\activate
```

**Linux/MacOS**
```
source env/bin/activate
```

Now you must install the necessary dependencies to run the analysis:

```
pipstubbornly refusing to install 'rioxarray' as a dependency of 'unknown' install -r requirements.txt
```

This should take a few minutes. Once it is done, you can run the Jupyter notebooks or Python scripts. For the main analysis, open the `proyecto_123.ipynb` notebook to execute the full workflow, including data processing, visualization, and RDD analysis. Alternatively, run the Python scripts in the following order:

1. `download_modis_lads.py` to download MODIS VCF data.
2. `convert_hdf_to_tif.py` to convert HDF files to TIFF.
3. `vcf_2024_peru_1.py` to create the final mosaic (`mosaico_peru_completo_4326_recortado_peru.tif`).

Use a Jupyter environment to run `notebooks/Peru’s_protected-area_polygons_from_OSM.ipynb` or `notebooks/Mosaico.ipynb` for additional data preparation and mosaicking steps.

## Project Files
- **proyecto_123.ipynb**: Main notebook containing the core analysis, including reprojection of rasters to EPSG:4326, clipping to Peru’s boundaries, buffer zone statistics, and regression discontinuity design (RDD) for tree cover analysis.
- **notebooks/Peru’s_protected-area_polygons_from_OSM.ipynb**: Downloads and processes protected areas data from OSM, saving as `areas_protegidas_solo_peru.gpkg`.
- **notebooks/Mosaico.ipynb**: Creates a mosaic of MODIS VCF TIFF files, handling memory issues by batch processing.
- **download_modis_lads.py**: Downloads MODIS VCF (MOD44B v061) Percent Tree Cover data for 2024.
- **convert_hdf_to_tif.py**: Converts HDF files to individual TIFF files.
- **vcf_2024_peru.py**: Creates a mosaic (`mosaico_peru.tif`) filtering specific coordinates (h09-h12, v08-v11).
- **vcf_2024_peru_1.py**: Creates the final mosaic (`mosaico_peru_completo_4326_recortado_peru.tif`) with coordinates (h08-h10, v09-v11), reprojected to EPSG:4326 and clipped to Peru’s boundaries.
- **areas_protegidas_solo_peru.gpkg**: Geopackage containing Peru’s protected areas from OSM.
- **estadisticas_buffers_forest_cover.csv**: Output CSV with buffer zone statistics for tree cover.
- **requirements.txt**: Lists Python dependencies.

## References
- OpenStreetMap contributors. (2024). Protected areas data retrieved via Overpass API.
- MODIS Vegetation Continuous Fields (MOD44B v061). (2024). NASA Earthdata.