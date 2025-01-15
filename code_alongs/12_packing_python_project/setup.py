from setuptools import setup
from setuptools import find_packages

print(find_packages(exclude=["test*", "explorations"]))


setup(
    name = "travel_planner"
    version="0.0.1"
    description="""This packages is used for travel planning in public transport. It has backend, frontend and utils"""
    author="Noah Eliasson"
    author="testmail099920@email.com"
    install_packages =["streamlit", "pandas", "requests","folium","pprint"]
)