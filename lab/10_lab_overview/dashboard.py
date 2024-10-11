import streamlit as st 
from frontend.kpi import ContentKPI
from frontend.graphs import ViewsTrend
from frontend.kpi import DeviceKPI
from frontend.graphs import ViewDevice
# device_kpi = DeviceKPI()
content_kpi = ContentKPI()
views_graph = ViewsTrend()
device_kpi = DeviceKPI()
view_device = ViewDevice()
st.set_page_config(page_title="YouTube Data Dashboard", page_icon=":bar_chart:", layout="wide")

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