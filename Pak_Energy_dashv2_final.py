#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import pandas as pd                                                     # library for data analysis
import numpy as np
import folium                                                           # map rendering library
import streamlit as st                                                  # creating an app
from streamlit_folium import folium_static          
import math                                                            
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.graph_objects as px
import plotly.graph_objs as go
import streamlit.components.v1 as components
from plotly.subplots import make_subplots

hydro_energy_data = pd.read_excel("Energy.xlsx", sheet_name="hydro",engine='openpyxl')
thermal_energy_data = pd.read_excel("Energy.xlsx", sheet_name="Thermal",engine='openpyxl')
wind_energy_data=pd.read_excel("Energy.xlsx", sheet_name="Wind",engine='openpyxl')
solar_energy_data=pd.read_excel("Energy.xlsx", sheet_name="Solar",engine='openpyxl')
nuclear_energy_data=pd.read_excel("Energy.xlsx", sheet_name="Nuclear",engine='openpyxl')
hydro_years = hydro_energy_data["Year"].unique().tolist()                   # getting the years of data available
thermal_years =  thermal_energy_data["Year"].unique().tolist() 
wind_years = wind_energy_data["Year"].unique().tolist() 
solar_years = solar_energy_data["Year"].unique().tolist() 
nuclear_years = nuclear_energy_data["Year"].unique().tolist() 

years_list = hydro_years + thermal_years +wind_years + solar_years +nuclear_years
years_list = list(dict.fromkeys(years_list))
years_list.sort() 





energy_overview_data=pd.read_excel("energy_overview.xlsx", sheet_name="energy",engine='openpyxl')
energy_capacity_data=pd.read_excel("energy_overview.xlsx", sheet_name="capacity",engine='openpyxl')
energysources=pd.read_excel ("energysources.xlsx")
print('print energysources: ')
print(energysources.head())

energysectors=pd.read_csv("Energy_sectors2.csv")
#energysectors2=pd.read_excel("Energy_sectors2.xlsx", engine='openpyxl')

energy_years =  energy_overview_data["Year"].unique().tolist() 
capacity_years =  energy_capacity_data["Year"].unique().tolist() 




years_list2 = energy_years
yearslist2=list(dict.fromkeys(years_list2))
energy_data = list(energy_overview_data.groupby(["Year"]))
capacity_data = list(energy_capacity_data.groupby(["Year"]))


#st.sidebar.subheader("Pakistan Energy mapping")





#add_select = st.sidebar.selectbox("What data do you want to see?",("OpenStreetMap", "Stamen Terrain","Stamen Toner"))
st.title("Pakistan Energy Dashboard")

st.subheader("Impact of Energy Policies on Energy Mix of Pakistan")
#st.sidebar.markdown("This is an interactive dashboard that allows users to understand and visualize the energy mix of Pakistan over the last 3 decades to capture the change over time. ")
#add_select = st.selectbox("What data do you want to see?",("Consu", "Stamen Terrain","Stamen Toner"))
option = st.selectbox(
     'Select Summaries from Menu',
     ('Consumption by Sector','Maximum Demand','Energy Mix','Electricity Generation'))
#option = st.selectbox(('Consumption by Sector','Maximum Demand','Energy Mix','Electricity Generation'))
#option = st.radio('Select Summaries:',
#                  ['Consumption by Sector','Maximum Demand','Energy Mix','Electricity Generation'])
#summary_year_sector = year_selector
#st.write('You selected:', add_select)
#st.write('Showing energy data for ', year_selector)
df=pd.read_excel ("energy_overview.xlsx",engine='openpyxl',sheet_name='capacity')
#df['Year'] = df.index
#df_melt = pd.melt(df, id_vars="Year", value_vars=df.columns[1:3])
#fig=px.line(df_melt, x="Year", y=value_vars,color="variable")




if option=='Maximum Demand':
    fig1 = go.Figure()

    fig1.add_trace(go.Scatter(
        x=df.Year,
        y=df['Generation_Capability'],
        name="Generation_Capability"
    ))

    fig1.add_trace(go.Scatter(
        x=df.Year,
        y=df['Maximum_Load'],
        name="Maximum_Demand"
    ))
    fig1.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))
    fig1.update_layout(
        autosize=False,
        width=800,
        height=500,)
    fig1.update_xaxes(title_text='Years')
    fig1.update_yaxes(title_text='MW')
    st.write(fig1)
if option=='Energy Mix':
    year_selector2 = st.slider("Summary years:", min_value=years_list2[0], max_value=years_list2[len(years_list2)-1] , value = years_list2[0], step=5)
    summary_year_value2=year_selector2
    energysources['2020'] = ['19.38%','9.86%','33.33%','8.65%','25.59%','2.17%','0.42%','0.60%']
    energysources['2015'] = ['0.1%','31.80%','31.4%','4.1%','31.1%','0.7%','0.5%','0.2%']
    data = energysources[str(summary_year_value2)].tolist()

    #print(energysources.head())
    data = [i.strip('%') for i in data]
    labels = energysources['Sources']
    colors = ['#808080', '#DC143C', '#228B22', 'violet','#0000FF','cyan','orange','yellow']
    fig2 = go.Figure(data=[go.Pie(labels=['Coal','Oil','Natural gas','Nuclear','Hydro','Wind','Biofuels','Solar PV'],
                             values=data)])
    fig2.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors))
    fig2.update_layout(
    autosize=False,
    width=600,
    height=600,
    title={
        'text': "Pakistan Energy Generation Mix",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    #xaxis_title="X Axis Title",
    #yaxis_title="Y Axis Title",
   # legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=16,
        #color="RebeccaPurple"
    )
    )
    st.write(fig2)
if option=='Electricity Generation':
    df=pd.read_excel ("electricity_generation.xlsx",engine='openpyxl')
    x=df['Years']
    y1=df['Coal']
    y2=df['Oil']
    y3=df['Natural gas']
    y4=df['Nuclear']
    y5=df['Hydro']

    plot3 = px.Figure()
  
    plot3.add_trace(go.Scatter(
    name = 'Coal',
    x = x,
    y = y1,
    stackgroup='one',
    fillcolor= '#808080'
   ))
      
    plot3.add_trace(go.Scatter(
    name = 'Oil',
    x = x,
    y = y2,
    stackgroup='one',
    fillcolor='#DC143C'
   ))
    plot3.add_trace(go.Scatter(
    name = 'Natural gas',
    x = x,
    y = y3,
    stackgroup='one',
    fillcolor='#228B22'
   ))
    plot3.add_trace(go.Scatter(
    name = 'Nuclear',
    x = x,
    y = y4,
    stackgroup='one',
    fillcolor=  'violet'
   ))
    plot3.add_trace(go.Scatter(
    name = 'Hydro',
    x = x,
    y = y5,
    stackgroup='one',
    fillcolor= '#0000FF'
   )
)
    plot3.update_layout(
    autosize=False,
    width=800,
    height=500,
    title={
        'text': "Electricity Generation by Sources",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    #xaxis_title="X Axis Title",
    #yaxis_title="Y Axis Title",
   # legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=16,
        #color="RebeccaPurple"
    )
    )
    plot3.update_xaxes(title_text='Years')
    plot3.update_yaxes(title_text='Electricity Generation GWH')
    st.write(plot3)
if option=='Consumption by Sector':
    year_selector3 = st.slider("Select years:", min_value=years_list[0], max_value=years_list[len(years_list)-1] , value = years_list[0], step=1)
   # year_selector3=2003
    
    summary_year_value3=year_selector3
    data = energysectors[str(summary_year_value3)].tolist()
    data = [i.strip('%') for i in data]
    labels = energysectors['Sectors']
    colors = ['Blue', '#DC143C', '#228B22', 'violet','yellow']
    fig4 = go.Figure(data=[go.Pie(labels=['Domestic','Commercial','Industrial','Agriculture','Streetlight'],
                             values=data)])
    fig4.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors))
    fig4.update_layout(
    autosize=False,
    width=600,
    height=600,
    title={
        'text': "Electricity consumption by Sector",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    #xaxis_title="X Axis Title",
    #yaxis_title="Y Axis Title",
   # legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=16,
        #color="RebeccaPurple"
    )
    )
    st.write(fig4)
#fig = px.line(df, x='Year',  y=df.columns[1:3],width=1000,height=500)
#fig.update_xaxes(title_text='Years')
#fig.update_yaxes(title_text='MW')
#st.write(fig)
   
   # fig= px.pie(energysources, values=data, names='Sources')
   # fig.update_layout(
   #    title={
   #        'text': "Pakistan Energy Mix Share by Sources",
   #        'y':1,
   #        'x':0.5,
   #        'xanchor': 'center',
   #        'yanchor': 'top'})
   # st.write(fig)

st.markdown("KEY INSIGHTS in Energy Mix: In **1990**, share of Hydel Energy was **44%**, however policies of successive govenments drastically shifted the energy mix to the point where almost **70%** of all power generation used thermal sources such as furnace oil and gas by year **2000** while Hydel energy was reduced to mere **25%**") 
hydro_grouped_energy_data = list(hydro_energy_data.groupby(["Year"]))
thermal_grouped_energy_data = list(thermal_energy_data.groupby(["Year"]))
wind_grouped_energy_data = list(wind_energy_data.groupby(["Year"]))
solar_grouped_energy_data = list(solar_energy_data.groupby(["Year"]))
nuclear_grouped_energy_data = list(nuclear_energy_data.groupby(["Year"]))
#year_value = year_selector3




st.text("")
st.subheader("Data References")
st.markdown(
        """
        1. Pakistan Installed capacity and Power Plants data from 2003 to 2018  were obtained from https://nepra.org.pk/publications/SOI_reports.php 
         
        
        2. Pakistan Energy Year Books prepared by Hydrocarbon Development Institute of Pakistan ,Ministry of Energy were also consulted
        3. International Energy Agency data was used to obtain Pakistan's Electricity generation(GWH), Electricity Consumption(GWH) ,Pakistan Generation Capacity(MW) and Peak Demand(MW) https://www.iea.org/countries/pakistan
 
        """
    )
st.text("")


