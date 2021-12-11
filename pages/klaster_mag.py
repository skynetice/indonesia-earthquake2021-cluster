import streamlit as st
import numpy as np
import pandas as pd
from pages import utils
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def app():
    data = pd.read_csv('data_clean.csv')

    df = data.drop(data[data['M'] < 4].index)
    df.reset_index(drop=True)

    data_cluster_mag = df.iloc[:, [2, 3]].values

    kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
    y_kmeans = kmeans.fit_predict(data_cluster_mag)
    
    plt.scatter(data_cluster_mag[y_kmeans == 0, 0], data_cluster_mag[y_kmeans == 0, 1], s = 10, c = 'blue', label = 'Cluster 1')
    plt.scatter(data_cluster_mag[y_kmeans == 1, 0], data_cluster_mag[y_kmeans == 1, 1], s = 10, c = 'red', label = 'Cluster 2')
    plt.scatter(data_cluster_mag[y_kmeans == 2, 0], data_cluster_mag[y_kmeans == 2, 1], s = 10, c = 'magenta', label = 'Cluster 3')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 100, c = 'yellow', label = 'Centroids')
    plt.title('Cluster gempa bumi di indonesia 2021 dengan KNN n=2')
    plt.xlabel('Kedalaman (Depth)')
    plt.ylabel('Magnitudo (M)')
    plt.legend()

    
    st.pyplot(plt)
