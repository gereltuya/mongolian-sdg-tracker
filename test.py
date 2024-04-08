import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_resource
def load_data():
    df = pd.read_csv('C:\\Users\\anuba\\Documents\\Greendot\\csv-dump\\deaths-and-missing-persons-due-to-natural-disasters.csv')
    return df

df = load_data()

st.title('Deaths and Missing Persons due to Natural Disasters')

filtered_data = df.copy() #filter data

#line plot
country = 'Mongolia'
filtered_data_mongolia = df[df['Entity'] == country]
fig_mongolia = px.line(filtered_data_mongolia, x='Year', y='13.1.1 - Number of deaths and missing persons attributed to disasters per 100,000 population (number) - VC_DSR_MTMP', labels={'13.1.1 - Number of deaths and missing persons attributed to disasters per 100,000 population (number) - VC_DSR_MTMP': 'Count'}, title=f'Deaths and Missing Persons in {country}')
fig_mongolia.update_traces(hovertemplate="Year: %{x}<br>Count: %{y}")
st.plotly_chart(fig_mongolia)

#toggle raw data
if st.button("Show Raw Data for Mongolia"):
    st.write(filtered_data_mongolia)

#map
fig_global_map = px.choropleth(data_frame=filtered_data,
                               locations='Entity',
                               locationmode='country names',
                               color='13.1.1 - Number of deaths and missing persons attributed to disasters per 100,000 population (number) - VC_DSR_MTMP',
                               title='Global Map - Deaths and Missing Persons',
                               projection='natural earth')

# center map to mongolia
fig_global_map.update_geos(center_lon=103.8467, center_lat=46.8625)

fig_global_map.update_layout(height=400, margin={"r":0,"t":30,"l":0,"b":0}, coloraxis_colorbar=dict(title=""))

#year slider + map
year_slider = st.slider("Year", min_value=min(df['Year']), max_value=max(df['Year']), value=min(df['Year']), step=1)
filtered_data_year = filtered_data[filtered_data['Year'] == year_slider]
fig_global_map.data[0].update(z=filtered_data_year['13.1.1 - Number of deaths and missing persons attributed to disasters per 100,000 population (number) - VC_DSR_MTMP'])
st.plotly_chart(fig_global_map)
