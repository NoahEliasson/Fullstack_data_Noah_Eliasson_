import streamlit as st
# from utils
from backend.query_database import QueryDatabase

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

class DeviceKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.device_summary").df

    def display_content(self):
        df = self._content
        st.markdown("## KPIer för enhetsinformation")
        df = df.iloc[1:].reset_index(drop=True)

        # Calculate metrics
        kpis = {
            "Totala enheter": len(df),
            "Unika enhetstyper": df["Enhetstyp"].nunique()  # Count of unique device types
        }

        # Display metrics in columns
        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col:
                st.metric(kpi, kpis[kpi]) 

        st.dataframe(df)

class OSKPI:
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


class GenderKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.gender_age").df

    def display_content(self):
        df = self._content

        kpis = {
            "kön antal": len(df),
        }
        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col: 
                st.metric(kpi, round(kpis[kpi]))
        st.dataframe(df)