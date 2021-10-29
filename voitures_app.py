import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Analyses voitures')

st.write("Données :")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_voitures = pd.read_csv(link)
st.write(df_voitures)

st.write("Corrélations :")


viz_correlation = sns.heatmap(df_voitures.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)

continent = df_voitures['continent'].drop_duplicates()
continent_choice = st.sidebar.selectbox('Select your continent:', continent)

st.write("Distribution :")


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(df_voitures["year"],df_voitures["weightlbs"])
ax.set_xlabel("Year")
ax.set_ylabel("Weightlbs")

st.write(fig)


