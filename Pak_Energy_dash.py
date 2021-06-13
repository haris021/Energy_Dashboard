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
energysources=pd.read_excel ("energysources.xlsx",engine='openpyxl')
energysectors=pd.read_csv("Energy_sectors2.csv")


energy_years =  energy_overview_data["Year"].unique().tolist() 
capacity_years =  energy_capacity_data["Year"].unique().tolist() 




years_list2 = energy_years
yearslist2=list(dict.fromkeys(years_list2))
energy_data = list(energy_overview_data.groupby(["Year"]))
capacity_data = list(energy_capacity_data.groupby(["Year"]))

st.sidebar.subheader("Impact of Energy Policies on Energy Mix of Pakistan")
st.sidebar.markdown("This is an interactive dashboard that allows users to understand and visualize the energy sector of Pakistan over the last 3 decades to capture the change over time to grasp the policy decisions made by successive governments.")




st.sidebar.subheader("Pakistan Energy mapping")
st.sidebar.markdown("Users can use this time slider to visualize the power plants progression over time across the country"
) 

year_selector = st.sidebar.slider("Select year:", min_value=years_list[0], max_value=years_list[len(years_list)-1] , value = years_list[0], step=1)


summary_year_value=year_selector




#add_select = st.sidebar.selectbox("What data do you want to see?",("OpenStreetMap", "Stamen Terrain","Stamen Toner"))
st.title("Pakistan Energy Dashboard")


#add_select = st.selectbox("What data do you want to see?",("Consu", "Stamen Terrain","Stamen Toner"))
option = st.radio('Select Summaries:',
                  ['Consumption by Sector','Peak Demand','Energy Mix','Electricity Generation'])
#summary_year_sector = year_selector
#st.write('You selected:', add_select)
#st.write('Showing energy data for ', year_selector)
df=pd.read_excel ("energy_overview.xlsx",engine='openpyxl',sheet_name='capacity')
#df['Year'] = df.index
#df_melt = pd.melt(df, id_vars="Year", value_vars=df.columns[1:3])
#fig=px.line(df_melt, x="Year", y=value_vars,color="variable")
if option=='Peak Demand':
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df.Year,
        y=df['Generation_Capability'],
        name="Generation_Capability"
    ))

    fig.add_trace(go.Scatter(
        x=df.Year,
        y=df['Maximum_Load'],
        name="Peak_Demand"
    ))
    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))
    fig.update_layout(
        autosize=False,
        width=800,
        height=500,)
    fig.update_xaxes(title_text='Years')
    fig.update_yaxes(title_text='MW')
    st.write(fig)
if option=='Energy Mix':
    year_selector2 = st.slider("Summary years:", min_value=years_list2[0], max_value=years_list2[len(years_list2)-1] , value = years_list2[0], step=5)
    summary_year_value2=year_selector2
    data = energysources[str(summary_year_value2)].tolist()
    data = [i.strip('%') for i in data]
    labels = energysources['Sources']
    colors = ['Blue', '#DC143C', '#228B22', 'violet','#0000FF','cyan','orange','yellow']
    fig = go.Figure(data=[go.Pie(labels=['Coal','Oil','Natural gas','Nuclear','Hydro','Wind','Biofuels','Solar PV'],
                             values=data)])
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors))
    fig.update_layout(
    autosize=False,
    width=600,
    height=600,
    title={
        'text': "Pakistan Energy Mix Share by Sources",
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
    st.write(fig)
if option=='Electricity Generation':
    df=pd.read_excel ("electricity_generation.xlsx",engine='openpyxl')
    x=df['Years']
    y1=df['Coal']
    y2=df['Oil']
    y3=df['Natural gas']
    y4=df['Nuclear']
    y5=df['Hydro']

    plot = px.Figure()
  
    plot.add_trace(go.Scatter(
    name = 'Coal',
    x = x,
    y = y1,
    stackgroup='one'
   ))
      
    plot.add_trace(go.Scatter(
    name = 'Oil',
    x = x,
    y = y2,
    stackgroup='one'
   ))
    plot.add_trace(go.Scatter(
    name = 'Natural gas',
    x = x,
    y = y3,
    stackgroup='one'
   ))
    plot.add_trace(go.Scatter(
    name = 'Nuclear',
    x = x,
    y = y4,
    stackgroup='one'
   ))
    plot.add_trace(go.Scatter(
    name = 'Hydro',
    x = x,
    y = y5,
    stackgroup='one'
   )
)
    plot.update_layout(
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
    plot.update_xaxes(title_text='Years')
    plot.update_yaxes(title_text='Electricity Generation GWH')
    st.write(plot)
if option=='Consumption by Sector':
    year_selector3 = st.slider("Select years:", min_value=years_list[0], max_value=years_list[len(years_list)-1] , value = years_list[0], step=1)
   # year_selector3=2003
    
    summary_year_value3=year_selector3
    data = energysectors[str(summary_year_value3)].tolist()
    data = [i.strip('%') for i in data]
    labels = energysectors['Sectors']
    colors = ['Blue', '#DC143C', '#228B22', 'violet','yellow']
    fig = go.Figure(data=[go.Pie(labels=['Domestic','Commercial','Industrial','Agriculture','Streetlight'],
                             values=data)])
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors))
    fig.update_layout(
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
    st.write(fig)
#fig = px.line(df, x='Year',  y=df.columns[1:3],width=1000,height=500)
#fig.update_xaxes(title_text='Years')
#fig.update_yaxes(title_text='MW')
#st.write(fig)

st.markdown("KEY INSIGHTS in Energy Mix: In **1990**, share of Hydel Energy was **44%**, however policies of successive govenments drastically shifted the energy mix to the point where almost **70%** of all power generation used thermal sources such as furnace oil and gas by year **2000** while Hydel energy was reduced to mere **25%**") 
st.title('Pakistan Energy Map')




    

   
   # fig= px.pie(energysources, values=data, names='Sources')
   # fig.update_layout(
   #    title={
   #        'text': "Pakistan Energy Mix Share by Sources",
   #        'y':1,
   #        'x':0.5,
   #        'xanchor': 'center',
   #        'yanchor': 'top'})
   # st.write(fig)


hydro_grouped_energy_data = list(hydro_energy_data.groupby(["Year"]))
thermal_grouped_energy_data = list(thermal_energy_data.groupby(["Year"]))
wind_grouped_energy_data = list(wind_energy_data.groupby(["Year"]))
solar_grouped_energy_data = list(solar_energy_data.groupby(["Year"]))
nuclear_grouped_energy_data = list(nuclear_energy_data.groupby(["Year"]))
year_value = year_selector


#showing the maps
m = folium.Map(location=(32, 67),
              zoom_start=4,tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Physical_Map/MapServer/tile/{z}/{y}/{x}',attr='Tiles &copy; Esri &mdash; Source: US National Park Service')


if year_selector in thermal_years:
    
    thermal_ind = thermal_years.index(year_value)
    year_energy_data_thermal = thermal_grouped_energy_data[thermal_ind][1] 


    data = year_energy_data_thermal
    for i in range(0,len(data)):

        # skipping if latitude or longitude is nan

        if math.isnan(float(data.iloc[i]['Latitude'])) or math.isnan(float(data.iloc[i]['Longitude'])): 
            continue

        folium.Circle(
            location=[data.iloc[i]['Latitude'], data.iloc[i]['Longitude']],
            popup=str(data.iloc[i]['Name']) +str(", ")+ str(float(data.iloc[i]['value'])) +str(" ")+ "MW",
            radius=float(data.iloc[i]['value']) * 20,                                                                 # change the multiplication to scale the bubbles up or down            
            color='Red',
            fill=True,
            fill_color='Red'
        ).add_to(m)




if year_selector in hydro_years: 
    
    hydro_ind = hydro_years.index(year_value)
    year_energy_data_hydro = hydro_grouped_energy_data[hydro_ind][1]

    data = year_energy_data_hydro
    for i in range(0,len(data)):

        # skipping if latitude or longitude is nan
        
        if math.isnan(float(data.iloc[i]['Latitude'])) or math.isnan(float(data.iloc[i]['Longitude'])): 
            continue
    

        folium.Circle(
        location=[data.iloc[i]['Latitude'], data.iloc[i]['Longitude']],
            popup=str(data.iloc[i]['Name']) +str(", ")+ str(float(data.iloc[i]['value'])) +str(" ")+ "MW",
        radius=float(data.iloc[i]['value']) * 20,                                                                 # change the multiplication to scale the bubbles up or down            
        color='Blue',
        fill=True,
        fill_color='Blue'
    ).add_to(m)

if year_selector in wind_years: 
    
    wind_ind = wind_years.index(year_value)
    year_energy_data_wind = wind_grouped_energy_data[wind_ind][1]

    data = year_energy_data_wind
    for i in range(0,len(data)):

        # skipping if latitude or longitude is nan
        
        if math.isnan(float(data.iloc[i]['Latitude'])) or math.isnan(float(data.iloc[i]['Longitude'])): 
            continue
    

        folium.Circle(
        location=[data.iloc[i]['Latitude'], data.iloc[i]['Longitude']],
            popup=str(data.iloc[i]['Name']) +str(", ")+ str(float(data.iloc[i]['value'])) +str(" ")+ "MW",
        radius=float(data.iloc[i]['value']) * 20,                                                                 # change the multiplication to scale the bubbles up or down            
        color='cyan',
        fill=True,
        fill_color='cyan'
    ).add_to(m)


if year_selector in solar_years: 
    
    solar_ind = solar_years.index(year_value)
    year_energy_data_solar = solar_grouped_energy_data[solar_ind][1]

    data = year_energy_data_solar
    for i in range(0,len(data)):

        # skipping if latitude or longitude is nan
        
        if math.isnan(float(data.iloc[i]['Latitude'])) or math.isnan(float(data.iloc[i]['Longitude'])): 
            continue
    

        folium.Circle(
        location=[data.iloc[i]['Latitude'], data.iloc[i]['Longitude']],
            popup=str(data.iloc[i]['Name']) +str(", ")+ str(float(data.iloc[i]['value'])) +str(" ")+ "MW",
        radius=float(data.iloc[i]['value']) * 20,                                                                 # change the multiplication to scale the bubbles up or down            
        color='yellow',
        fill=True,
        fill_color='yellow'
    ).add_to(m)


if year_selector in nuclear_years: 
    
    nuclear_ind = nuclear_years.index(year_value)
    year_energy_data_nuclear = nuclear_grouped_energy_data[nuclear_ind][1]

    data = year_energy_data_nuclear
    for i in range(0,len(data)):

        # skipping if latitude or longitude is nan
        
        if math.isnan(float(data.iloc[i]['Latitude'])) or math.isnan(float(data.iloc[i]['Longitude'])): 
            continue
    

        folium.Circle(
        location=[data.iloc[i]['Latitude'], data.iloc[i]['Longitude']],
            popup=str(data.iloc[i]['Name']) +str(", ")+ str(float(data.iloc[i]['value'])) +str(" ")+ "MW",
        radius=float(data.iloc[i]['value']) * 50,                                                                 # change the multiplication to scale the bubbles up or down            
        color='darkviolet',
        fill=True,
        fill_color='darkviolet'
    ).add_to(m)


url = 'https://www.rethinkingindus.com/'
st.sidebar.image("logo.png", width=100)
st.sidebar.markdown("RethinkingIndus")
st.sidebar.markdown(url)






folium_static(m)
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


