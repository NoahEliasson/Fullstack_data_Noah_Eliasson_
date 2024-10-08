import plotly.express as px
import streamlit as st 
# from utils
from query_database import QueryDatabase

class ViewsTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.views_per_date").df
        print(self.df)

    def display_plot(self):
        fig = px.line(self.df, x="Datum", y="Visningar")
        st.markdown("## Antal visningar under senaste månaden")
        st.plotly_chart(fig)

# create more graphs here

class ViewOS:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.operationsystem_view;").df

    def display_os_plot(self): 
        fig = px.bar(self.df, x="Operativsystem", y="total_visningar")
        st.plotly_chart(fig)