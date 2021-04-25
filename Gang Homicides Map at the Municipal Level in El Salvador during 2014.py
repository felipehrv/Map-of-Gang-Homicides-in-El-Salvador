#!/usr/bin/env python
# coding: utf-8

# # Created by: Felipe Rodríguez
# ### Purpose 
# Map gang homicides perpetreted in El Salvador during 2014 (Totals at the municipal level).

# ### Data
# 
# Gang Homicides: The data reports the total number of homicides perpetrated by gangs during 2014.
# 
# Data source: https://www.transparencia.gob.sv/institutions/pnc/documents/estadisticas
# 
# Municipalities: The data reports the shapes of all 262 municipalities of El Salvador (WGS 1894). 
# 
# Data source: https://www.cnr.gob.sv/geoportal-cnr/

# In[23]:


import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as mplc
import matplotlib.ticker as ticker
import numpy as np


# Reading shapefile containing the 262 municipalities of El Salvador

# In[24]:


municipalities = gpd.read_file('/Users/feliperodriguez/Documents/data analysis/raw/LIMITES WGS 84/LIM_MUNICIPAL.shp')


# In[3]:


municipalities.head(2)


# #### Map of El Salvador at the municipal level

# In[4]:


municipalities.plot()


# #### Now, reading gang homicides data from El Salvador

# In[5]:


homicides2014 = pd.read_csv('/Users/feliperodriguez/Documents/data analysis/raw/homicides_municipalities_2014.csv', encoding='utf-8')


# In[6]:


homicides2014.head(2)


# #### Next, we merge both datasets to combine homicide data at the municipal level with its corresponing geographic features

# In[7]:


municipalities = municipalities.merge(right = homicides2014,
                                    left_on = 'NA2',
                                    right_on = 'MUNICIPIO',
                                    how = 'left')


# In[8]:


municipalities.head(2)


# #### For data quality purposes, we replace missing values in the homicides variable with 0 (zeros). We also replace the missing values in the MUNIPIO variable with the values of the NA2 variable, to define MUNICIPIO as the main geographic variable.

# In[9]:


municipalities.MUNICIPIO.fillna(municipalities.NA2, inplace=True)


# In[10]:


municipalities['TOTAL'] = municipalities['TOTAL'].fillna(0)


# In[11]:


municipalities.head(2)


# #### In this first attempt plotting gang homicides at the municipal levels, the geographic differences in homicides levels are hard to see. San Salvador (the capital), is the only municipalities painted in yellow, which indicates that municipalities in yellow and green tones are the municipalities with the higher levels of gang homicides. 

# In[12]:


municipalities.plot(column = 'TOTAL')


# #### Next, we include shades of blue to make geographic differences more visible.

# In[13]:


municipalities.plot(column = 'TOTAL',
                    legend = True,
                    legend_kwds = {
                        'label': "Total number of homicides",
                        'orientation': "horizontal"},
                   cmap = 'Blues')


# #### Next, we apply logs to the homicides variable and plot our map again to highlight the geographich variation in the levels of gang homicides.

# In[14]:


municipalities['TOTAL'] = municipalities['TOTAL'].fillna(1)
municipalities['TOTAL_log'] = np.log10(municipalities['TOTAL'])


# In[15]:


municipalities['TOTAL_log'] = municipalities['TOTAL_log'].replace([np.inf,-np.inf],0)


# In[16]:


municipalities.plot(column = 'TOTAL_log',
                    legend = True,
                    legend_kwds = {
                        'label': "Total number of homicides",
                        'orientation': "horizontal"},
                   cmap = 'Blues')


# #### Finally, we use the quartile distribution to map the geographich variation of gang homicides at the municipal level. We also add the edges of all the municipalities. 

# In[22]:


labels = ['Quartil_1', 'Quartil_2','Quartil_3','Quartil_4']

#Creating a new column including the quartile distribution of the total number of gang homicides
municipalities['TOTAL_Quartiles'] = pd.cut(
                        x = municipalities['TOTAL_log'],
                        bins = 4, 
                        labels = labels
                        )


#Using matplotlib
fig , ax = plt.subplots(1, figsize = (14,8))

#Map characteristics
municipalities.plot(
  column = 'TOTAL_Quartiles', 
  categorical = True, 
  legend = True,
  cmap = 'Blues',
  ax = ax,
  linewidth = 1,
  edgecolor = 'black',
  )

ax.set_title('Total number of gang homicides at the municipal level (2014)', fontsize = 25)


ax.axis('off')


fig.show()


# #### In our final product, we can easily see that the municipalities with the highest levels of gang homicides in 2014 were San Salvador, Soyapango, Apopa, Colon, San Martin, Ilobasco and Zacatecoluca.
