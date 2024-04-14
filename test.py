import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components

st.title("Mongolian SDG Tracker - Demo")


st.markdown("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
st.divider()
files_info = {
    'deaths-and-missing-persons-due-to-natural-disasters.csv': 'Rate of Deaths and Missing Persons due to Natural Disasters',
    'internally-displaced-persons-from-disasters.csv': 'Internally Displaced Persons from Disasters',
    'natural-disasters.csv': 'Natural Disasters'
}

iframe_urls = {
    'number-homeless-from-natural-disasters.csv': ("Number Homeless from Natural Disasters", "https://ourworldindata.org/grapher/number-homeless-from-natural-disasters"),
    'number-injured-from-disasters.csv': ("Number Injured from Disasters", "https://ourworldindata.org/grapher/number-injured-from-disasters"),
    'total-affected-by-natural-disasters.csv': ("Total Affected by Natural Disasters", "https://ourworldindata.org/grapher/total-affected-by-natural-disasters")
}
@st.cache_data
def load_data(file_name):
    path = f'./csv-dump/{file_name}'
    return pd.read_csv(path)

country = 'Mongolia'

for file_name, title in files_info.items():
    df = load_data(file_name)
    st.subheader(title)
    
    if file_name == 'natural-disasters.csv':
        df['Total deaths from disasters'] = df.filter(regex='Number of deaths from').sum(axis=1)
        filtered_data = df[df['Country name'] == country]
        fig = px.bar(filtered_data, x='Year', y='Total deaths from disasters', title='Total Deaths from Disasters in Mongolia')
        fig.update_traces(hovertemplate="Year: %{x}<br>Total Deaths: %{y}")
        st.plotly_chart(fig)
    else:
        column_name = df.columns[-1]
        filtered_data = df[df['Entity'] == country]
        fig = px.line(filtered_data, x='Year', y=column_name, labels={column_name: 'Count'}, title=f'{title} in {country}')
        fig.update_traces(hovertemplate="Year: %{x}<br>Count: %{y}")
        st.plotly_chart(fig)
        if st.button(f"Show Raw Data for {country} - {title}"):
            st.write(filtered_data)

for file_name, (title, iframe_url) in iframe_urls.items():
    st.subheader(title) 
    components.iframe(iframe_url, height=500)
