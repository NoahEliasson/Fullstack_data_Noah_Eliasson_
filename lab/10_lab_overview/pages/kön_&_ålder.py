import streamlit as st 
from frontend.kpi import GenderKPI
from frontend.graphs import GenderGraph
gender_kpi = GenderKPI()
gender_graph = GenderGraph()
def layout():
    st.title("könsfördelnings data")
    gender_kpi.display_content()
    gender_graph.display_plot()
if __name__ == "__main__":
    layout()