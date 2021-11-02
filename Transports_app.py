import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title('Analyses Transports Bruxelles')

st.write("Données Villo")

villos_final = pd.read_csv('Villos_Final.csv')
villos_final = villos_final.drop(columns ='Unnamed: 0')
st.write(villos_final)

Timestamp = villos_final['Timestamp']
Timestamp_choice = st.sidebar.selectbox('Select your Timestamp :', Timestamp)

fig2 = px.scatter_mapbox(villos_final, lat="position.lat", lon="position.lng", size='Vélos disponibles',
                  size_max=20,zoom=12, hover_name='name', animation_frame='Timestamp', animation_group='name',
                  hover_data = ['Vélos disponibles'],
                  title = 'Nombre de vélos disponibles par station')
fig2.update_layout(mapbox_style='carto-positron')
fig2.layout.height = 800

st.plotly_chart(fig2)

st.write("Blablabla :")

fig1 = px.scatter_mapbox(villos_final, lat="position.lat", lon="position.lng", 
                  zoom=12, hover_name='name', animation_frame='Timestamp', animation_group='name',
                  hover_data = ['Vélos disponibles'], color = 'Taux de remplissage',
                  color_discrete_sequence = ['green','orange','red'],
                  title = 'Taux de remplissage de vélos par station')
fig1.update_traces(marker=dict(size=12))
fig1.update_layout(mapbox_style='carto-positron')
fig1.layout.height = 800

st.plotly_chart(fig1)

st.write("Blablabla :")

st.write("Données Cambio :")

cambios_final = pd.read_csv('Cambio_Final.csv')
cambios_final = cambios_final.drop(columns ='Unnamed: 0')


st.write(cambios_final)

fig3 = px.scatter_mapbox(cambios_final, lat="geoposition.latitude", lon="geoposition.longitude", 
                        size='Nombre de Cambio disponibles',size_max=20,
                        zoom=12, hover_name='name', animation_frame='Timestamp', animation_group='name',
                        hover_data = ['Nombre de Cambio disponibles'], 
                        title = 'Nombre de voitures disponibles par station')
fig3.update_layout(mapbox_style='carto-positron')
fig3.layout.height = 800

st.plotly_chart(fig3)

st.write("Blablabla :")

