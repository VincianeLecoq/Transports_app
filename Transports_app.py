import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title('Analyses Villo & Cambio Bruxelles')


st.header("Villo")  

st.image(
            "https://o3.ldh.be/image/thumb/5a254b7bcd70b488fb03fb6e.jpg",
            width=400
        )

st.subheader("Informations stations Villo et disponibilités des vélos partagés par Jour/Heure") 

villos_final = pd.read_csv('Villos_Final.csv')
villos_final = villos_final.drop(columns ='Unnamed: 0')

tableau_villos = villos_final
tableau_villos = tableau_villos.drop(columns=['position.lat', 'position.lng', 'taux_remplissage'])
tableau_villos = tableau_villos.rename(columns={"name": "Station", "address": "Adresse", "bike_stands": "Supports vélos", "available_bike_stands": "Supports vélos disponibles" })

st.write(tableau_villos)

Timestamp = villos_final['Timestamp'].drop_duplicates()
Timestamp_choice = st.sidebar.selectbox('Select your Timestamp :', Timestamp)

st.subheader("Nombre de vélos disponibles par station par Jour/Heure") 

fig2 = px.scatter_mapbox(villos_final, lat="position.lat", lon="position.lng", size='Vélos disponibles',
                  size_max=20,zoom=12, hover_name='name', animation_frame='Timestamp', animation_group='name',
                  hover_data = ['Vélos disponibles'])
fig2.update_layout(mapbox_style='carto-positron')
fig2.layout.height = 800

st.plotly_chart(fig2)

st.write("Observations : Le centre de Bruxelles semble se vider de vélos en début de matinée et se remplir le soir")

st.subheader("Moyenne du nombre de vélos disponibles dans toutes les stations par heure") 

df_moyenne_villo = pd.read_csv('Villos_Moyenne.csv')

fig4 = plt.figure()
plt.bar(data = df_moyenne_villo, x= 'heure', height = 'Vélos disponibles')
plt.ylim([3000,4000])
plt.xlabel('Heure')
plt.ylabel('Nombre de vélos disponibles')

st.pyplot(fig4)

st.write("Observations : Les vélos sont principalement utilisés entre 5h - 10h et 17h - 20h ")

st.subheader("Taux de remplissage de vélos par station par Jour/Heure") 

fig1 = px.scatter_mapbox(villos_final, lat="position.lat", lon="position.lng", 
                  zoom=12, hover_name='name', animation_frame='Timestamp', animation_group='name',
                  hover_data = ['Vélos disponibles'], color = 'Taux de remplissage',
                  color_discrete_sequence = ['green','orange','red'])
fig1.update_traces(marker=dict(size=12))
fig1.update_layout(mapbox_style='carto-positron')
fig1.layout.height = 800

st.plotly_chart(fig1)

st.write("Observations : Cohérence avec les graphiques précédents")

st.header("Cambio")  

st.image(
            "https://ds1.static.rtbf.be/image/media/object/default/16x9/1248x702/a/b/b/abbb7fe1bcfb4a18afb7619ef9de8bea.jpg",
            width=400
        )
  
st.subheader("Informations stations Cambio et disponibilités des voitures partagées par Jour/Heure") 

cambios_final = pd.read_csv('Cambio_Final.csv')
cambios_final = cambios_final.drop(columns ='Unnamed: 0')


tableau_cambios = cambios_final
tableau_cambios = tableau_cambios.drop(columns=['address.postalCode', 'geoposition.longitude', 'geoposition.latitude'])
tableau_cambios = tableau_cambios.rename(columns={"name": "Station", "address.streetAddress": "Rue", "address.streetNumber": "Numéro", "address.addressLocation": "Commune" })

st.write(tableau_cambios)

st.subheader("Nombre de voitures disponibles par station par Jour/Heure") 

fig3 = px.scatter_mapbox(cambios_final, lat="geoposition.latitude", lon="geoposition.longitude", 
                        size='Nombre de Cambio disponibles',size_max=20,
                        zoom=12, hover_name='name', animation_frame='Timestamp', animation_group='name',
                        hover_data = ['Nombre de Cambio disponibles'])
fig3.update_layout(mapbox_style='carto-positron')
fig3.layout.height = 800

st.plotly_chart(fig3)

st.write("Observations : Les données n'ont changé qu'une seule fois ce qui ne parait pas cohérent -> Revoir le système de récolte de données ?")

