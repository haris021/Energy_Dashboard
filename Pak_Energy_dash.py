
import pandas as pd                                                     # library for data analysis
import numpy as np
import folium                                                           # map rendering library
import streamlit as st                                                  # creating an app
from streamlit_folium import folium_static          
import math                                                            
import plotly.express as px
import matplotlib.pyplot as plt
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

energy_years =  energy_overview_data["Year"].unique().tolist() 
capacity_years =  energy_capacity_data["Year"].unique().tolist() 





years_list2 = energy_years
yearslist2=list(dict.fromkeys(years_list2))
energy_data = list(energy_overview_data.groupby(["Year"]))
capacity_data = list(energy_capacity_data.groupby(["Year"]))
year_selector = st.sidebar.slider("Select year:", min_value=years_list[0], max_value=years_list[len(years_list)-1] , value = years_list[0], step=1)



     

#add_select = st.sidebar.selectbox("What data do you want to see?",("OpenStreetMap", "Stamen Terrain","Stamen Toner"))
st.title("Pakistan Energy Dashboard")

st.subheader("Impact of Energy Policies on Energy Mix of Pakistan")
st.markdown("This is an interactive dashboard that allows users to understand and visualize the energy mix of Pakistan over the last 3 decades to capture the change over time. The users can interact with the map and see the progression and change in the installed and generation capacity to grasp the policy decisions made by successive governments.")
#st.write('You selected:', add_select)
#st.write('Showing energy data for ', year_selector)
df=pd.read_excel ("energy_overview.xlsx",engine='openpyxl',sheet_name='capacity')
#df['Year'] = df.index
#df_melt = pd.melt(df, id_vars="Year", value_vars=df.columns[1:3])
#fig=px.line(df_melt, x="Year", y=value_vars,color="variable")
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df.Year,
    y=df['Generation_Capability'],
    name="Generation_Capability"
))

fig.add_trace(go.Scatter(
    x=df.Year,
    y=df['Maximum_Load'],
    name="Maximum_Load"
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
#for col in df.columns:
    
#    fig.add_trace(go.Line(name= df[col], x=df.Year, y=df[col]))
#    fig.update_layout(legend=dict(
#    yanchor="top",
#    y=0.99,
#    xanchor="left",
#    x=0.01
#))

st.write(fig)
#fig = px.line(df, x='Year',  y=df.columns[1:3],width=1000,height=500)
#fig.update_xaxes(title_text='Years')
#fig.update_yaxes(title_text='MW')
#st.write(fig)

st.sidebar.markdown("Power generation capacity and Peak demand of the country over the course of 30 years"
) 
year_selector2 = st.sidebar.slider("Summary Years:", min_value=years_list2[0], max_value=years_list2[len(years_list2)-2] , value = years_list2[0], step=5)
url = 'https://www.rethinkingindus.com/'
st.sidebar.image("logo.png", width=100)
st.sidebar.markdown("RethinkingIndus")
st.sidebar.markdown(url)
summary_year_value = year_selector2

    
col1, col2 = st.beta_columns(2)
with col1:
    
    st.subheader('Summary Display Year:')
with col2:
    st.subheader(summary_year_value)
#year_selector2
col1, col2 = st.beta_columns((1,2))

    
with col1:
    

    energy_ind = energy_years.index(summary_year_value)
    year_energy_data = energy_data[energy_ind][1] 


    data = year_energy_data
    for i in range(0,len(data)):
        st.subheader ('Electricity Generation (GWH) ')
        st.markdown(str(data.iloc[i]['Electricity_Generation(GWH)']))
        
    st.subheader ('Electricity Consumption (GWH) ')
    energy_ind = energy_years.index(summary_year_value)
    year_energy_data = energy_data[energy_ind][1]


    data = year_energy_data
    for i in range(0,len(data)):
        st.markdown(str(data.iloc[i]['Electricity_Consumption (GWH)']))


with col2:

    data = energysources[str(summary_year_value)].tolist()
    data = [i.strip('%') for i in data]
    labels = energysources['Sources']

    fig= px.pie(energysources, values=data, names='Sources')
    fig.update_layout(
       title={
           'text': "Pakistan Energy Mix Share by Sources",
           'y':1,
           'x':0.5,
           'xanchor': 'center',
           'yanchor': 'top'})
    st.write(fig)

st.markdown("KEY INSIGHTS: In **1990**, share of Hydel Energy was **44%**, however policies of successive govenments drastically shifted the energy mix to the point where almost **70%** of all power generation used thermal sources such as furnace oil and gas by year **2000** while Hydel energy was reduced to mere **25%**") 
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




st.title('Pakistan Energy Map')









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


