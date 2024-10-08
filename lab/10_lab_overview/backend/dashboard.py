#import sys
#sys.path.insert(0, "C:/Users/Noah7/Desktop/Code/fullstack_data_test/Fullstack_data_Noah_Eliasson_/lab/10_lab_overview/frontend" )
import streamlit as st 
# from frontend
from kpi import ContentKPI
from graphs import ViewsTrend
from kpi import DeviceKPI
from graphs import ViewDevice
# device_kpi = DeviceKPI()
content_kpi = ContentKPI()
views_graph = ViewsTrend()
device_kpi = DeviceKPI()
view_device = ViewDevice()
st.set_page_config(page_title="YouTube Data Dashboard", page_icon=":bar_chart:", layout="wide")
st.sidebar.success("Select a page above.")

def layout():

    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i min youtubekanal")
    # device_kpi.display_device_views()
    # device_kpi.display_device_summary()
    content_kpi.display_content()
    views_graph.display_plot()
    device_kpi.display_content()
    view_device.display_plot()
if __name__ == "__main__":
    layout()