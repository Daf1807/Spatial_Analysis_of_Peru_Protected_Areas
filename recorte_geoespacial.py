import rasterio
from rasterio.mask import mask
import geopandas as gpd
import matplotlib.pyplot as plt

# Ruta al shapefile de distritos
shapefile_path = r"C:\Users\usuario\Documents\GitHub\Spatial_Analysis_of_Peru-s_Protected_Areas\241878_hw4\shape_file\DISTRITOS.shp"

# Ruta al mosaico
raster_path = r"C:\Users\usuario\Documents\GitHub\Spatial_Analysis_of_Peru-s_Protected_Areas\241878_hw4\modis_data\tifs\mosaico_peru_completo.tif"

# Leer el shapefile
gdf = gpd.read_file(shapefile_path)

# Abrir el raster y alinear CRS si es necesario
with rasterio.open(raster_path) as src:
    if gdf.crs != src.crs:
        gdf = gdf.to_crs(src.crs)

    # Recortar usando las geometrías del shapefile
    out_image, out_transform = mask(src, gdf.geometry, crop=True)
    out_meta = src.meta.copy()

# Actualizar metadatos del nuevo raster recortado
out_meta.update({
    "driver": "GTiff",
    "height": out_image.shape[1],
    "width": out_image.shape[2],
    "transform": out_transform
})

# Guardar el raster recortado
output_path = r"C:\Users\usuario\Documents\GitHub\Spatial_Analysis_of_Peru-s_Protected_Areas\241878_hw4\modis_data\tifs\mosaico_peru_recortado.tif"

with rasterio.open(output_path, "w", **out_meta) as dest:
    dest.write(out_image)

print(f"✅ Raster recortado guardado en: {output_path}")

