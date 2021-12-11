import streamlit as st
import numpy as np
import pandas as pd
from pages import utils
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_folium import folium_static
import folium


def app():
    data = pd.read_csv('../data_clean.csv')

    df = data.drop(data[data['M'] < 4].index)
    df.reset_index(drop=True)

    n = folium.Map(location=(-00.7893000, 116.9213000), zoom_start=4.2)

    for i in range(len(df)):
        folium.Circle(
            location=[df.iloc[i]['Lat'], df.iloc[i]['Lon']],
            radius=10,
        ).add_to(n)

    folium_static(n,width=800, height=500)