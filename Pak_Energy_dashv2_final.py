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
data ={
    "data": [
        {
            "type": "sankey",
            "domain": {
                "x": [
                    0,
                    1
                ],
                "y": [
                    0,
                    1
                ]
            },
            "orientation": "h",
            "valueformat": ".3f",
            "valuesuffix": "MTOe",
            "node": {
                "pad": 15,
                "thickness": 15,
                "line": {
                    "color": "black",
                    "width": 0.5
                },
                "label": [
                    "Oil Prod",
                    "Oil Imp",
                    "Oil Product Imp",
                    "Coal prod",
                    "Coal imp",
                    "Bio/waste Prod",
                    "Electricity imp",
                    "Solar/wind",
                    "Hydro",
                    "Nuclear prod",
                    "Refineries",
                    "Other transformation",
                    "Power Station",
                    "Power Loses",
                    "Exports",
                    "Bunkers",
                    "Own use",
                    "Industry",
                    "Transport",
                    "Other",
                    "Non-energy",
                    "Gas Prod",
                    "Gas imp",
                    "Total Oil",
                    "Total Coal",
                    "Total Gas",
                    "Total Electricity"              
                      ],
                "color": [
                    "rgba(31, 119, 180, 0.8)", # "Oil Prod",
                    "rgba(255, 127, 14, 0.8)",#"Oil Imp",
                    "rgba(44, 160, 44, 0.8)",  #"Oil Product Imp",
                    "rgba(214, 39, 40, 0.8)", # "Coal prod",
                    "rgba(148, 103, 189, 0.8)",#  "Coal imp",
                    "rgba(140, 86, 75, 0.8)", # "Bio/waste Prod",
                    "rgba(227, 119, 194, 0.8)",#  "Electricity imp",
                    "rgba(255, 255, 0, 0.8)",# "solar/wind",
                    "rgba(0, 0, 128, 0.8)",#"Hydro imp",
                    "rgba(23, 190, 207, 0.8)", #"Nuclear prod",
                    "rgba(31, 119, 180, 0.8)",  #"Refineries",
                    "rgba(255, 127, 14, 0.8)", #"Other transformation",
                    "rgba(44, 160, 44, 0.8)",  #"Power Station",
                    "rgba(214, 39, 40, 0.8)", #"Power Loses",
                    "rgba(148, 103, 189, 0.8)",# "Exports",
                    "rgba(140, 86, 75, 0.8)", #Bunkers",
                    "rgba(227, 119, 194, 0.8)",#"Own use",
                    "rgba(127, 127, 127, 0.8)",#"Industry",
                    "rgba(188, 189, 34, 0.8)",  # "Transport",
                    
                    "rgba(148, 103, 189, 0.8)", #"Other",
                    "rgba(140, 86, 75, 0.8)",#"Non-energy",
                    "rgba(227, 119, 194, 0.8)", #"Gas Prod",
                    "rgba(127, 127, 127, 0.8)",#"Gas imp",
                    "rgba(188, 189, 34, 0.8)", #"Total Oil",
                    
                    "rgba(148, 103, 189, 0.8)", #"Total Coal",
                    "rgba(140, 86, 75, 0.8)",#"Total Gas",
                    "rgba(227, 119, 194, 0.8)",# "Total Electricity"
                    ]
            },
            "link": {
                "source": [
                    0,1,2,10,23,23,23,23,23,23,23,23,
                    21,22,25,25,25,25,25,25,
                    3,4,24,24,
                    5,5,5,
                    8,7,9,
                    6,12,
                    12,
                   26,26,26

                ],
                "target": [
                    10,10,23,23,12,17,18,19,20,14,15,16,
                    25,25,12,17,18,19,20,16,
                    24,24,17,12,
                    12,17,19
                    ,12,12,12
                    ,26,26
                    ,13,
                   16,17,19
                    
                   
                ],
                "value": [
                   4.29,
                    6.284,
                    10.17,
                    9.55,
                    2.87,
                    1.23,
                    14.17,
                    1.42,
                    0.29,
                    0.33,
                    0.29,
                    0.27,
                    21.32,
                    7.73,
                    7.7,
                    5.67,
                    1.03,
                    7.98,
                    3.8,
                    0.13,
                    3.18,
                    10.17,
                    6.95,
                    6.32,
                    0.24,
                    4.07,
                    32.58,
                    2.92,
                    0.32,
                    3,
                    2.2,
                    11.46,
                    11.94,
                    0.23,
                    2.2,
                    7.06,                    
                    ],
                "color": [
                    "rgba(0,0,96,0.2)",#0-10
                    "rgba(0,0,96,0.2)",#1-10
                    "rgba(0,0,96,0.2)",#2-23
                    "rgba(0,0,96,0.2)",#10-23
                    "rgba(0,0,96,0.2)",#23-12
                    "rgba(0,0,96,0.2)",#23-17
                    "rgba(0,0,96,0.2)",#23-18
                    "rgba(0,0,96,0.2)",#23-19
                    "rgba(0,0,96,0.2)",#23-20
                    "rgba(0,0,96,0.2)",#23-14
                    "rgba(0,0,96,0.2)",#23-15
                    "rgba(0,0,96,0.2)",#23-16
                    "rgba(0,0,96,0.2)",#21-25
                    "rgba(0,0,96,0.2)",#22-25
                    "rgba(0,0,96,0.2)",#25-12
                    "rgba(0,0,96,0.2)",#25-117
                    "rgba(0,0,96,0.2)",#25-18
                    "rgba(0,0,96,0.2)",#25-19
                    "rgba(0,0,96,0.2)",#25-20
                    "rgba(0,0,96,0.2)",#25-16
                    "rgba(0,0,96,0.2)",#3-24
                    "rgba(0,0,96,0.2)",#4-24
                    "rgba(0,0,96,0.2)",#24-17
                    "rgba(0,0,96,0.2)",#24-12
                    "rgba(0,0,96,0.2)",#5-12
                    "rgba(0,0,96,0.2)",#5-17
                    "rgba(0,0,96,0.2)",#5-19
                    "rgba(0,0,96,0.2)",#8-12
                    "rgba(0,0,96,0.2)",#7-12
                    "rgba(0,0,96,0.2)",#9-12
                    "rgba(0,0,96,0.2)",#6-26
                    "rgba(0,0,96,0.2)",#12-26
                    "rgba(0,0,96,0.2)",#12-13
                    "rgba(0,0,96,0.2)",#26-16
                    "rgba(0,0,96,0.2)",#26-17
                    "rgba(0,0,96,0.2)",#26-19
                ],
                "label": [
                    "stream 1",
                    "",
                    "",
                    "",
                    "stream 1",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    ""
                ]
            }
        }],
    "layout": {
        "title": {"text": "Energy forecast for 2050, UK — Department of Energy & Climate Change<br>Imperfect copy of <a href='https://bost.ocks.org/mike/sankey/'>Mike Bostock's example</a><br>with numerous <a href='https://plotly.com/javascript/'>Plotly</a> features"},
        "width": 1118,
        "height": 772,
        "font": {
            "size": 10
        },
        "updatemenus": [
            {
                "y": 1,
                "buttons": [
                    {
                        "label": "Light",
                        "method": "relayout",
                        "args": [ "paper_bgcolor", "white" ]
                    },
                    {
                        "label": "Dark",
                        "method": "relayout",
                        "args": [ "paper_bgcolor", "black"]
                    }
                ]
            },
            {
                "y": 0.9,
                "buttons": [
                    {
                        "label": "Thick",
                        "method": "restyle",
                        "args": [ "node.thickness", 15 ]
                    },
                    {
                        "label": "Thin",
                        "method": "restyle",
                        "args": [ "node.thickness", 8]
                    }
                ]
            },
            {
                "y": 0.8,
                "buttons": [
                    {
                        "label": "Small gap",
                        "method": "restyle",
                        "args": [ "node.pad", 15 ]
                    },
                    {
                        "label": "Large gap",
                        "method": "restyle",
                        "args": [ "node.pad", 20]
                    }
                ]
            },
            {
                "y": 0.7,
                "buttons": [
                    {
                        "label": "Snap",
                        "method": "restyle",
                        "args": [ "arrangement", "snap" ]
                    },
                    {
                        "label": "Perpendicular",
                        "method": "restyle",
                        "args": [ "arrangement", "perpendicular"]
                    },
                    {
                        "label": "Freeform",
                        "method": "restyle",
                        "args": [ "arrangement", "freeform"]
                    },
                    {
                        "label": "Fixed",
                        "method": "restyle",
                        "args": [ "arrangement", "fixed"]
                    }
                ]
            },
            {
                "y": 0.6,
                "buttons": [
                    {
                        "label": "Horizontal",
                        "method": "restyle",
                        "args": [ "orientation", "h" ]
                    },
                    {
                        "label": "Vertical",
                        "method": "restyle",
                        "args": [ "orientation", "v"]
                    }
                ]
            }
        ]
    }
}





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



    #url = 'https://www.rethinkingindus.com/'


#add_select = st.sidebar.selectbox("What data do you want to see?",("OpenStreetMap", "Stamen Terrain","Stamen Toner"))
st.title("Pakistan Energy Dashboard")

#st.subheader("#RethinkingIndus")
st.markdown("This is an interactive dashboard that allow users to understand and visualize the energy sector of Pakistan over the last 3 decades to capture the change over time.Users can select different options from drop down menu.")
#add_select = st.selectbox("What data do you want to see?",("Consu", "Stamen Terrain","Stamen Toner"))
option = st.selectbox(
     'Select Summaries from Menu',
     ('Consumption by Sector','Maximum Demand','Energy Mix','Electricity Generation','Pakistan Energy Balance'))
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
    energysources['2020'] = ['19.60%','4.43%','20.64%','17.25%','7.76%','27.17%','2.03%','0.50%','0.64%']
    energysources['2015'] = ['0.1%','24.37%','7.95%','28.23%','4.1%','33.99%','0.7%','0.27%','0.2%']
    data = energysources[str(summary_year_value2)].tolist()

    #print(energysources.head())
    data = [i.strip('%') for i in data]
    labels = energysources['Sources']
    colors = ['#808080', '#DC143C', '#800000','#228B22', 'violet','#0000FF','cyan','orange','yellow']
    fig2 = go.Figure(data=[go.Pie(labels=['Coal','Oil','RLNG','Natural gas','Nuclear','Hydro','Wind','Biofuels','Solar PV'],
                             values=data)])
    fig2.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors))
    fig2.update_layout(
    autosize=False,
    width=600,
    height=600,
    title={
        'text': "Pakistan Electricity Generation Mix",
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
    y6=df['RLNG']
    y7= df ['Wind']
    y8= df['Solar PV']
    y9= df['Biofuels']

    plot3 = px.Figure()
  
    plot3.add_trace(go.Scatter(
    name = 'Coal',
    x = x,
    y = y1,
    stackgroup='one',
   # fillcolor= "rgba(128,128,128,0.8)"
   
   ))
      
    plot3.add_trace(go.Scatter(
    name = 'Oil',
    x = x,
    y = y2,
    stackgroup='one',
   # fillcolor="rgba(255,0,0,0.6)"
   ))
    plot3.add_trace(go.Scatter(
    name = 'Natural gas',
    x = x,
    y = y3,
    stackgroup='one',
  #  fillcolor="rgba(0,128,0,0.6)"
   ))
    plot3.add_trace(go.Scatter(
    name = 'Nuclear',
    x = x,
    y = y4,
    stackgroup='one',
  #  fillcolor= "rgba(0,255,255,0.6)"
   ))
    
    plot3.add_trace(go.Scatter(
    name = 'Hydro',
    x = x,
    y = y5,
    stackgroup='one',
 #   fillcolor= "rgba(0,0,255,0.6)"
    
   )
)
    plot3.add_trace(go.Scatter(
    name = 'RLNG',
    x = x,
    y = y6,
    stackgroup='one',
  #  fillcolor= "rgba(0,255,255,0.6)"
   ))
    plot3.add_trace(go.Scatter(
    name = 'Wind',
    x = x,
    y = y7,
    stackgroup='one',
  #  fillcolor= "rgba(0,255,255,0.6)"
   ))
    plot3.add_trace(go.Scatter(
    name = 'Solar PV',
    x = x,
    y = y8,
    stackgroup='one',
  #  fillcolor= "rgba(0,255,255,0.6)"
   ))
    plot3.add_trace(go.Scatter(
    name = 'Biofuels',
    x = x,
    y = y9,
    stackgroup='one',
  #  fillcolor= "rgba(0,255,255,0.6)"
   ))
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
if option =='Pakistan Energy Balance':

    opacity = 0.4
    # change 'magenta' to its 'rgba' value to add opacity
    data['data'][0]['node']['color'] = ['rgba(255,0,255, 0.8)' if color == "magenta" else color for color in data['data'][0]['node']['color']]
    data['data'][0]['link']['color'] = [data['data'][0]['node']['color'][src].replace("0.8", str(opacity))
                                        for src in data['data'][0]['link']['source']]

    fig = go.Figure(data=[go.Sankey(
        valueformat = ".3f",
        valuesuffix = "Mtoe",
        # Define nodes
        node = dict(
        pad = 15,
        thickness = 15,
        line = dict(color = "black", width = 0.5),
        label =  data['data'][0]['node']['label'],
        color =  data['data'][0]['node']['color']
        ),
        # Add links
        link = dict(
        source =  data['data'][0]['link']['source'],
        target =  data['data'][0]['link']['target'],
        value =  data['data'][0]['link']['value'],
        label =  data['data'][0]['link']['label'],
        color =  data['data'][0]['link']['color']
    ))])
        
    fig.update_layout(title_text="Pakistan Energy Balance 2020",
                    font_size=10)
    st.write(fig)
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
st.image("logo.png", width=100)
st.markdown("Developed by Haris Mushtaq")
st.text("")


