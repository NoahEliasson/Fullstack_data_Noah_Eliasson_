import streamlit as st
# from utils
from query_database import QueryDatabase

class ContentKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.content_view_time;").df

    def display_content(self):
        df = self._content
        st.markdown("## KPIer för videor")
        st.markdown("Nedan visas KPIer för totalt antal")

        kpis = {
            "videor": len(df),
            "visade timmar": df["Visningstid_timmar"].sum(),
            "prenumeranter": df["Prenumeranter"].sum(),
            "exponeringar": df["Exponeringar"].sum(),
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col: 
                st.metric(kpi, round(kpis[kpi]))
        st.dataframe(df)

# os kpi not device change"!!! #####
class DeviceKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.operationsystem_view;").df

    def display_content(self):
        df = self._content
        st.markdown("Nedan visas KPIer för totalt antal")
        
        kpis = {
            "olika operativsystem": len(df),
        }
        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col: 
                st.metric(kpi, round(kpis[kpi]))
        st.dataframe(df)