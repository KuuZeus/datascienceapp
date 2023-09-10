import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px

####@@@@@@ Malaria Data analysis #######
st.header('Global Under 5 Mortality due Malaria Analysis')

st.subheader('Mortality in all African countries in 2019')

df= pd.read_csv('malaria-death-rates-by-age.csv')

# print(df.head())

# print(df.columns)
## under 5 deaths due to malaria in 2019
df= df[['Entity','Year', 'Deaths - Malaria - Sex: Both - Age: Under 5 (Rate)']]

df.rename(columns={'Entity':'Country','Deaths - Malaria - Sex: Both - Age: Under 5 (Rate)': 'Malaria Deaths'}, inplace=True)

df_2019=df[df['Year']==2019]

# selecting countries without the regions
df_all =df_2019[df_2019['Country'].str.contains('WHO|Bank|World')==False]

# Top 50 countries

df_all_top50 = df_all.sort_values('Malaria Deaths', ascending=False).head(50)

st.write(df_all_top50)
#Average mortality
# avg_deaths = df_all_top50['Malaria Deaths'].mean()
#
# print(avg_deaths)
#

# st.metric(label='Pointer',  value= avg_deaths, delta= avg_deaths )

# Trend of malaria deaths #####
#countries in the top 50 countries wih the highest malaria mortality
countries= df_all_top50['Country'].tolist()
list_df= []
for country in countries:
    list_df.append(df[df['Country']==country])
df_trend = pd.concat(list_df)

# print(len(df_trend))
country_drilldown = st.selectbox('Filter by country',(countries))
fig = px.line(df_trend[df_trend['Country']==country_drilldown], x='Year',y='Malaria Deaths', color='Country')
st.write(fig)





# The malaria mortality in the 5 WHO regions

st.subheader('Mortality in the 5 WHO Regions')
df_who= df_2019[df_2019['Country'].str.contains('Region')]

st.write(df_who.sort_values('Malaria Deaths', ascending=False))

st.subheader('Mortality in the 4 World Bank Regions')
# The malaria mortality in the 4 world bank regions
df_bank = df_2019[df_2019['Country'].str.contains('Bank')]

st.write(df_bank.sort_values('Malaria Deaths', ascending= False))


