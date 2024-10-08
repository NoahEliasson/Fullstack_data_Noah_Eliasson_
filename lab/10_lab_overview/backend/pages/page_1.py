import streamlit as st 
from graphs import ViewOS
from kpi import DeviceKPI
os_kpi = DeviceKPI()
os_graph = ViewOS()
def layout():
    st.title("visningar per operativ system")
    os_kpi.display_content()
    os_graph.display_os_plot()
if __name__ == "__main__":
    layout()