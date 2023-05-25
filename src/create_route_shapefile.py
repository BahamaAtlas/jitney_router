import pandas as pd
import geopandas as gpd
import osmnx as ox
from shapely.geometry import LineString

def generate_route_shapefile:
  # Read the CSV file into a pandas DataFrame
  df = pd.read_csv('streets.csv')

  # Create an empty list to store LineString geometries
  geometry = []

  # Iterate over the street names in the CSV
  for street_name in df['street_names']:
      # Retrieve the street network for the given street name
      graph = ox.graph_from_place(street_name, network_type='all_private')
    
     # Extract the coordinates for the street network
      nodes, edges = ox.graph_to_gdfs(graph)
    
      # Create a LineString from the extracted coordinates
      line = LineString(nodes.geometry.values)
    
      # Add the LineString to the geometry list
      geometry.append(line)

  # Create a GeoDataFrame from the DataFrame and LineString geometries
  gdf = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')

  # Save the GeoDataFrame as a shapefile
  gdf.to_file('line_layer.shp', driver='ESRI Shapefile')
