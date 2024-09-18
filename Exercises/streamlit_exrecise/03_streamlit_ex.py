import streamlit as st 
import pandas as pd 
from pathlib import Path
import plotly.express as px

def read_data():
    data_path = Path(__file__).parents[1] / "data"
    df = pd.read_csv(data_path / "employye_table.csv", index_col=0, parse_dates=[0])
    return df



def layout():
    df = read_data()
    # to fix streamlits comma for thousands
    st.markdown("# employee dashboard")

    st.markdown("This is a simple dashboard about employees")

    st.markdown("## Raw data")
    st.markdown("This data shows number of started educations per region and per year") 
    st.dataframe(df)

    st.markdown("## Trends per region")


if __name__ == "__main__":
    layout()