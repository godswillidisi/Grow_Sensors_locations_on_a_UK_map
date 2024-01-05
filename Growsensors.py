# I imported necessary libraries for this project. pandas for data manipulation, geopandas for 
# handling geographical data, point class from shapely for representing point geometries and
# Matplotlib for plotting.
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

# reading the data from a CSV file into a Dataframe
df = pd.read_csv('GrowLocations.csv')

# To remove bad values I Filtered out rows with invalid latitude and longitude values
df1 = df[(df['Latitude'] >= -90) & (df['Latitude'] <= 90) & (df['Longitude'] >= -180) & (df['Longitude'] <= 180)]

# Remove duplicates based on latitude and longitude columns
data= df1.drop_duplicates(subset=['Latitude', 'Longitude'])


# I noticed some error with the bounding box data. I fixed it by swapping the Latitude and Longitude label 
# in other to get the correct plot. I went further to filter out locations outside the bounding box.
data = data[(data['Latitude'] >= -10.592) & (data['Latitude'] <= 1.6848) &
            (data['Longitude'] >= 50.681) & (data['Longitude'] <= 57.985)]

# Create a GeoDataFrame from the dataframe with coordinates
geometry = [Point(xy) for xy in zip(data['Latitude'], data['Longitude'])] 
# Create a GeoDataFrame with Point geometries and set the coordinate reference system (CRS)
gdf = gpd.GeoDataFrame(data, geometry=geometry, crs='EPSG:4326')

# Read and Load the map image 
map_image = plt.imread('map7.png')

# Setting up the figure and axis for plotting of the pointd
fig, ax = plt.subplots(figsize=(15, 10))

# Display the map image using the correct bounding box
ax.imshow(map_image, extent=[-10.592, 1.6848, 50.681, 57.985])

# Plotting the sensor locations on the map
gdf.plot(ax=ax, marker='o', color='blue', markersize=7, label='GROW sensor locations')

# Set plot title and axislabels
plt.title('Grow Sensor Locations on UK Map')
plt.xlabel('Latitude')  
plt.ylabel('Longitude')

# Show the plot with legend
plt.legend()
plt.show()

