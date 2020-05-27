# -*- coding: utf-8 -*-
"""Countrywisecases_heatmap.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZO_QMNEwTV69JY8ozzM9KxS0pYj-ub7p
"""

pip install pycountry

#pip install pycountry
import pycountry
import plotly.express as px
import pandas as pd

country_cases_file= r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
cases_country = pd.read_csv(country_cases_file)
# print(cases_country_code.head)

list_countries = cases_country['Country'].unique().tolist()
# print(list_countries) 
d_country_code = {}  
for country in list_countries:
    try:
        country_data = pycountry.countries.search_fuzzy(country)       
        country_code = country_data[0].alpha_3
        d_country_code.update({country: country_code})
    except:
        print('could not add ISO 3 code for ->', country)        
        d_country_code.update({country: ' '})

# print(d_country_code)  


for k, v in d_country_code.items():
    cases_country.loc[(cases_country.Country == k), 'iso_alpha'] = v

# print(cases_country_df.head)  

fig = px.choropleth(data_frame = cases_country,
                    locations= "iso_alpha",
                    color= "Confirmed",  
                    hover_name= "Country",
                    color_continuous_scale= 'RdYlGn',
                    animation_frame= "Date"  
                   )

fig.show()