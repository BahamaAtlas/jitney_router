import pandas as pd
import geopandas as gpd
import osmnx as ox
from shapely.geometry import Point

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('streets.csv')

# Create an empty list to store Point geometries
geometry = []

# Retrieve the street network for Nassau, Bahamas
graph = ox.graph_from_place("Nassau, Bahamas", network_type='all_private', which_result=2)

# Iterate over the street names in the CSV
for street_name in df['street_names']:
    # Find the nearest network nodes to the given street name
    nodes = ox.distance.nearest_nodes(graph, df['latitude'], df['longitude'], method='euclidean')
    
    # Create Point geometries from the nearest nodes
    points = [Point(graph.nodes[node]['x'], graph.nodes[node]['y']) for node in nodes]
    
    # Add the Point geometries to the geometry list
    geometry.extend(points)

# Create a GeoDataFrame from the DataFrame and Point geometries
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')

# Save the GeoDataFrame as a shapefile
gdf.to_file('point_layer.shp', driver='ESRI Shapefile')
