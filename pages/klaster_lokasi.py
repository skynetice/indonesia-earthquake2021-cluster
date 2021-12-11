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
    data = pd.read_csv('../data_clean.csv')

    df = data.drop(data[data['M'] < 4].index)
    df.reset_index(drop=True)

    data_cluster = df.iloc[:, [1, 0]].values

    X = data_cluster

    db = DBSCAN(eps=2.5, min_samples=55).fit(X)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)

    clusters = labels

    colors = ['royalblue', 'maroon', 'forestgreen', 'mediumorchid', 'tan', 'deeppink', 'olive', 'goldenrod', 'lightcyan', 'navy', 'black']
    vectorizer = np.vectorize(lambda x: colors[x % len(colors)])

    plt.figure(figsize=(12,6))
    plt.scatter(X[:,0], X[:,1], c=vectorizer(clusters))

    
    st.pyplot(plt)