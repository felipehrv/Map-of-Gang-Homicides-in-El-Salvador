# Created by: Felipe Rodríguez
### Purpose 
Map gang homicides perpetreted in El Salvador during 2014 (Totals at the municipal level).

### Data

Gang Homicides: The data reports the total number of homicides perpetrated by gangs during 2014.

Data source: https://www.transparencia.gob.sv/institutions/pnc/documents/estadisticas

Municipalities: The data reports the shapes of all 262 municipalities of El Salvador (WGS 1894). 

Data source: https://www.cnr.gob.sv/geoportal-cnr/


```python
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as mplc
import matplotlib.ticker as ticker
import numpy as np
```

Reading shapefile containing the 262 municipalities of El Salvador


```python
municipalities = gpd.read_file('/Users/feliperodriguez/Documents/data analysis/raw/LIMITES WGS 84/LIM_MUNICIPAL.shp')
```


```python
municipalities.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FCODE</th>
      <th>UID</th>
      <th>ASD</th>
      <th>COD</th>
      <th>NA2</th>
      <th>NA3</th>
      <th>NAM</th>
      <th>PPL</th>
      <th>ACC</th>
      <th>CCN</th>
      <th>SDV</th>
      <th>SDP</th>
      <th>SRT</th>
      <th>TXT</th>
      <th>AREA_KM</th>
      <th>PERIMETRO</th>
      <th>geometry</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>FA000</td>
      <td>ADC5DBEA-E0F4-41A6-A041-F59F7BE599C6</td>
      <td>1</td>
      <td>1</td>
      <td>MEANGUERA DEL GOLFO</td>
      <td>1410</td>
      <td>Meanguera Del Golfo</td>
      <td>2398.0</td>
      <td>1</td>
      <td>Derechos reservados por el Centro Nacional de ...</td>
      <td>Desconocido</td>
      <td>Desconocido</td>
      <td>0</td>
      <td>14</td>
      <td>24.73</td>
      <td>39.19</td>
      <td>MULTIPOLYGON (((-87.68407 13.16659, -87.68438 ...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>FA000</td>
      <td>150EB5DA-75AD-483F-97F2-4D63D41867EA</td>
      <td>1</td>
      <td>1</td>
      <td>INTIPUCÁ</td>
      <td>1407</td>
      <td>Intipucá</td>
      <td>7567.0</td>
      <td>1</td>
      <td>Derechos reservados por el Centro Nacional de ...</td>
      <td>Desconocido</td>
      <td>Desconocido</td>
      <td>0</td>
      <td>14</td>
      <td>93.99</td>
      <td>42.16</td>
      <td>POLYGON ((-88.00756 13.25025, -87.99033 13.236...</td>
    </tr>
  </tbody>
</table>
</div>



#### Map of El Salvador at the municipal level


```python
municipalities.plot()
```




    <AxesSubplot:>




    
![png](output_7_1.png)
    


#### Now, reading gang homicides data from El Salvador


```python
homicides2014 = pd.read_csv('/Users/feliperodriguez/Documents/data analysis/raw/homicides_municipalities_2014.csv', encoding='utf-8')
```


```python
homicides2014.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DEPARTAMENTO</th>
      <th>MUNICIPIO</th>
      <th>TOTAL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AHUACHAPAN</td>
      <td>AHUACHAPÁN</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AHUACHAPAN</td>
      <td>ATIQUIZAYA</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



#### Next, we merge both datasets to combine homicide data at the municipal level with its corresponing geographic features


```python
municipalities = municipalities.merge(right = homicides2014,
                                    left_on = 'NA2',
                                    right_on = 'MUNICIPIO',
                                    how = 'left')
```


```python
municipalities.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FCODE</th>
      <th>UID</th>
      <th>ASD</th>
      <th>COD</th>
      <th>NA2</th>
      <th>NA3</th>
      <th>NAM</th>
      <th>PPL</th>
      <th>ACC</th>
      <th>CCN</th>
      <th>SDV</th>
      <th>SDP</th>
      <th>SRT</th>
      <th>TXT</th>
      <th>AREA_KM</th>
      <th>PERIMETRO</th>
      <th>geometry</th>
      <th>DEPARTAMENTO</th>
      <th>MUNICIPIO</th>
      <th>TOTAL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>FA000</td>
      <td>ADC5DBEA-E0F4-41A6-A041-F59F7BE599C6</td>
      <td>1</td>
      <td>1</td>
      <td>MEANGUERA DEL GOLFO</td>
      <td>1410</td>
      <td>Meanguera Del Golfo</td>
      <td>2398.0</td>
      <td>1</td>
      <td>Derechos reservados por el Centro Nacional de ...</td>
      <td>Desconocido</td>
      <td>Desconocido</td>
      <td>0</td>
      <td>14</td>
      <td>24.73</td>
      <td>39.19</td>
      <td>MULTIPOLYGON (((-87.68407 13.16659, -87.68438 ...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>FA000</td>
      <td>150EB5DA-75AD-483F-97F2-4D63D41867EA</td>
      <td>1</td>
      <td>1</td>
      <td>INTIPUCÁ</td>
      <td>1407</td>
      <td>Intipucá</td>
      <td>7567.0</td>
      <td>1</td>
      <td>Derechos reservados por el Centro Nacional de ...</td>
      <td>Desconocido</td>
      <td>Desconocido</td>
      <td>0</td>
      <td>14</td>
      <td>93.99</td>
      <td>42.16</td>
      <td>POLYGON ((-88.00756 13.25025, -87.99033 13.236...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



#### For data quality purposes, we replace missing values in the homicides variable with 0 (zeros). We also replace the missing values in the MUNIPIO variable with the values of the NA2 variable, to define MUNICIPIO as the main geographic variable.


```python
municipalities.MUNICIPIO.fillna(municipalities.NA2, inplace=True)
```


```python
municipalities['TOTAL'] = municipalities['TOTAL'].fillna(0)
```


```python
municipalities.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FCODE</th>
      <th>UID</th>
      <th>ASD</th>
      <th>COD</th>
      <th>NA2</th>
      <th>NA3</th>
      <th>NAM</th>
      <th>PPL</th>
      <th>ACC</th>
      <th>CCN</th>
      <th>SDV</th>
      <th>SDP</th>
      <th>SRT</th>
      <th>TXT</th>
      <th>AREA_KM</th>
      <th>PERIMETRO</th>
      <th>geometry</th>
      <th>DEPARTAMENTO</th>
      <th>MUNICIPIO</th>
      <th>TOTAL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>FA000</td>
      <td>ADC5DBEA-E0F4-41A6-A041-F59F7BE599C6</td>
      <td>1</td>
      <td>1</td>
      <td>MEANGUERA DEL GOLFO</td>
      <td>1410</td>
      <td>Meanguera Del Golfo</td>
      <td>2398.0</td>
      <td>1</td>
      <td>Derechos reservados por el Centro Nacional de ...</td>
      <td>Desconocido</td>
      <td>Desconocido</td>
      <td>0</td>
      <td>14</td>
      <td>24.73</td>
      <td>39.19</td>
      <td>MULTIPOLYGON (((-87.68407 13.16659, -87.68438 ...</td>
      <td>NaN</td>
      <td>MEANGUERA DEL GOLFO</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>FA000</td>
      <td>150EB5DA-75AD-483F-97F2-4D63D41867EA</td>
      <td>1</td>
      <td>1</td>
      <td>INTIPUCÁ</td>
      <td>1407</td>
      <td>Intipucá</td>
      <td>7567.0</td>
      <td>1</td>
      <td>Derechos reservados por el Centro Nacional de ...</td>
      <td>Desconocido</td>
      <td>Desconocido</td>
      <td>0</td>
      <td>14</td>
      <td>93.99</td>
      <td>42.16</td>
      <td>POLYGON ((-88.00756 13.25025, -87.99033 13.236...</td>
      <td>NaN</td>
      <td>INTIPUCÁ</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



#### In this first attempt plotting gang homicides at the municipal levels, the geographic differences in homicides levels are hard to see. San Salvador (the capital), is the only municipalities painted in yellow, which indicates that municipalities in yellow and green tones are the municipalities with the higher levels of gang homicides. 


```python
municipalities.plot(column = 'TOTAL')
```




    <AxesSubplot:>




    
![png](output_19_1.png)
    


#### Next, we include shades of blue to make geographic differences more visible.


```python
municipalities.plot(column = 'TOTAL',
                    legend = True,
                    legend_kwds = {
                        'label': "Total number of homicides",
                        'orientation': "horizontal"},
                   cmap = 'Blues')
```




    <AxesSubplot:>




    
![png](output_21_1.png)
    


#### Next, we apply logs to the homicides variable and plot our map again to highlight the geographich variation in the levels of gang homicides.


```python
municipalities['TOTAL'] = municipalities['TOTAL'].fillna(1)
municipalities['TOTAL_log'] = np.log10(municipalities['TOTAL'])
```

    /Users/feliperodriguez/opt/anaconda3/lib/python3.8/site-packages/pandas/core/series.py:726: RuntimeWarning: divide by zero encountered in log10
      result = getattr(ufunc, method)(*inputs, **kwargs)



```python
municipalities['TOTAL_log'] = municipalities['TOTAL_log'].replace([np.inf,-np.inf],0)
```


```python
municipalities.plot(column = 'TOTAL_log',
                    legend = True,
                    legend_kwds = {
                        'label': "Total number of homicides",
                        'orientation': "horizontal"},
                   cmap = 'Blues')
```




    <AxesSubplot:>




    
![png](output_25_1.png)
    


#### Finally, we use the quartile distribution to map the geographich variation of gang homicides at the municipal level. We also add the edges of all the municipalities. 


```python
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
```

    <ipython-input-22-6897cf1f156c>:31: UserWarning: Matplotlib is currently using module://ipykernel.pylab.backend_inline, which is a non-GUI backend, so cannot show the figure.
      fig.show()



    
![png](output_27_1.png)
    


#### In our final product, we can easily see that the municipalities with the highest levels of gang homicides in 2014 were San Salvador, Soyapango, Apopa, Colon, San Martin, Ilobasco and Zacatecoluca.
