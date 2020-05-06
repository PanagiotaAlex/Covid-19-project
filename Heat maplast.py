#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import geopandas as gpd
import math


# In[3]:


import folium
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap, MarkerCluster


# In[5]:


# Create a map
m_1 = folium.Map(location=[42.32,-71.0589], tiles='openstreetmap', zoom_start=2)

# Display the map
m_1


# In[3]:


data = pd.read_csv(r"C:\Users\user\OneDrive\Υπολογιστής\covid_19.csv")                       
df = data.copy()


# In[4]:


# Create a base map
m_5 = folium.Map(location=[42.32,-71.0589], tiles='cartodbpositron', zoom_start=2)

# Add a heatmap to the base map
HeatMap(data=data[['Lat', 'Long']], radius=10).add_to(m_5)

# Display the map
m_5


# In[ ]:




