
""" streamlit container-like for both backend and frontend
    pandas for data access
    pygwalker for a Tableau-like UI
"""
import streamlit as st
import pandas as pd
import pygwalker as pyg

# Set page configuration
st.set_page_config(
    page_title="PyGWalker Demo",
    page_icon=":snake:",
    layout="wide",
    initial_sidebar_state="expanded",
)

@st.cache_data
def load_data(url):
    """ load_data returns dataframe using URL param """
    dataframe = pd.read_csv(url)
    return dataframe
# df = load_data("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
df=pd.read_csv("data/orders.csv")
# Set title and subtitle
st.title('PyGWalker Demo App')
st.subheader('A demonstration of the PyGWalker Python library')

def load_config(file_path):
    """ load_config displays PyGWalker UI """
    with open(file_path, 'r', encoding='UTF-8') as config_file:
        config_str = config_file.read()
    return config_str
# config = load_config('config.json')
# pyg.walk(df, env='Streamlit', dark='dark', spec=config)
pyg.walk(df, env='Streamlit', dark='dark')
