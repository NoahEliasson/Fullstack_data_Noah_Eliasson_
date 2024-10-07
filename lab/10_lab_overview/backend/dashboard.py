import sys
sys.path.insert(0, "C:/Users/Noah7/Desktop/Code/fullstack_data_test/Fullstack_data_Noah_Eliasson_/lab/10_lab_overview/frontend" )
import streamlit as st 
from kpi import ContentKPI
from graphs import ViewsTrend

# device_kpi = DeviceKPI()
content_kpi = ContentKPI()
views_graph = ViewsTrend()

def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i min youtubekanal")
    # device_kpi.display_device_views()
    # device_kpi.display_device_summary()
    content_kpi.display_content()
    views_graph.display_plot()

if __name__ == "__main__":
    layout()