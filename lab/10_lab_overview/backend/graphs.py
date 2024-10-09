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
class ViewDevice:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.device_summary").df
    
    def display_plot(self):

        graph_type = st.selectbox("Välj en kpi att visa", options=["Visningar", "Visnings timmar", "Visningslängd genomsnitt"])
        if graph_type == "Visningar":
            fig = px.bar(self.df, x="Enhetstyp", y="Visningar", title="totala visningsar per enhet")
        elif graph_type == "Visnings timmar":
            fig = px.bar(self.df, x="Enhetstyp", y="Visningstid_timmar", title="total visningstid timmar per enhet")
        elif graph_type == "Visningslängd genomsnitt":
            fig = px.bar(self.df, x="Enhetstyp", y="Visningslängd_genomsnitt", title="genomsnittlig visningtid per enhet")
        st.plotly_chart(fig)

class ViewOS:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.operationsystem_view;").df

    def display_os_plot(self): 
        fig = px.bar(self.df, x="Operativsystem", y="total_visningar")
        st.plotly_chart(fig)