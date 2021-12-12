import streamlit as st
import numpy as np
import pandas as pd
from pages import utils
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def app():
    st.write("""
    #Klasterisasi Gempa Bumi di Indonesia Selama 2021

    Indonesia, terletak tepat di atas cincin api dan pertemuan tiga lempeng tektonik besar yaitu lempeng Eurasia, Indo-Australia, dan Pasifik, menjadikan negara ini rawan bencana alam, khususnya gempa bumi.
    Berdasarkan data USGS (2016), sekitar 90% gempa bumi yang terjadi di dunia termasuk gempa terbesar terjadi di sepanjang cincin api.
    
    
    """)

    st.write("""
    
    Berangkat dari latar belakang dan kondisi geografis di Indonesia ini, kami ingin melakukan project penelitian Tugas Akhir mengenai Clustering Gempa Bumi yang terjadi di Indonesia selama 2021. 
    Output dari penelitian ini adalah mengidentifikasikan / memetakan gempa bumi yang terjadi di Indonesia.

    
    """)

    data = pd.read_csv('data_clean.csv')

    st.bar_chart(data['M'])

    
    st.pyplot(plt)
