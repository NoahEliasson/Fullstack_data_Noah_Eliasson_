import streamlit as st 
from frontend.graphs import ViewOS
from frontend.kpi import OSKPI
os_kpi = OSKPI()
os_graph = ViewOS()
def layout():
    st.title("visningar per operativ system")
    os_kpi.display_content()
    os_graph.display_os_plot()
if __name__ == "__main__":
    layout()