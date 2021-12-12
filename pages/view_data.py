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
    # Klasterisasi Gempa Bumi di Indonesia Selama 2021

    Indonesia, terletak tepat di atas cincin api dan pertemuan tiga lempeng tektonik besar yaitu lempeng Eurasia, Indo-Australia, dan Pasifik, menjadikan negara ini rawan bencana alam, khususnya gempa bumi.
    Berdasarkan data USGS (2016), sekitar 90% gempa bumi yang terjadi di dunia termasuk gempa terbesar terjadi di sepanjang cincin api.
    
    
    """)

    st.write("""
    
    Berangkat dari latar belakang dan kondisi geografis di Indonesia ini, kami ingin melakukan project penelitian Tugas Akhir mengenai Clustering Gempa Bumi yang terjadi di Indonesia selama 2021. 
    Output dari penelitian ini adalah mengidentifikasikan / memetakan gempa bumi yang terjadi di Indonesia.

    
    """)

    st.subheader('Pengumpulan data')

    st.write("""
    Data yang digunakan dalam proyek ini merupakan data gempa bumi yang terjadi di Indonesia selama tahun 2021 yang diambil dari situs BMKG.

    adapun bentuk data yang diambil adalah sebagai berikut :
    """)

    data_old = pd.read_csv('data.csv', sep=';')

    

    data = pd.read_csv('data_clean.csv')

    st.dataframe(data_old)

    st.markdown('Data diatas merupakan _Raw_ data atau data mentah.')

    st.write("""
    Selanjutnya dilakukan preprocessing pada data sehingga data dapat diolah pada proses klasterisasi.
    """)

    st.subheader('Pengenalan data')

    st.bar_chart(data['M'].value_counts())
    st.caption('intensitas magnitudo gempa bumi yang terjadi di indonesia')

    st.write("""
    Data yang diperolah melalui situs BMKG merupakan data gempa bumi yang terjadi di indonesia selama tahun 2021 yang tercatat pada sistem. Namun, dari keseluruhan data gempa yang diperoleh tidak semua memiliki nilai yang signifikan.
    menurut USSG[1] gempa bumi dapat yang dapat dirasakan oleh manusia berkisar pada magnitudo lebih dari 4 skala richter. Artinya gempa yang memiliki magnitudo lebih kecil dari 4 tidak memiliki nilai yang signifikan sehingga dapat kita abaikan. 
    """)

    df = data.drop(data[data['M'] < 4].index)
    df.reset_index(drop=True)
    st.bar_chart(df['M'].value_counts())

    
    st.pyplot(plt)
