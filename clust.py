import numpy as np
import scipy.stats
from matplotlib import pyplot
import matplotlib.pyplot as plt
import math
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

def clustering(df,k):
	# k-means: inputs (lat, long)
	data = list((zip( df['delivery latitude'], df['delivery longtitude'])))
	aux = []
	index = []
	
	for i in range(2,k):
        	km = KMeans(n_clusters=i)
        	km.fit(data)
        	score = silhouette_score(data, km.labels_, metric='euclidean')
        	aux.append(score)
        	index.append(i)

	bestK = max(list(zip(aux, index)))
	#print(bestK)

	kmeans = KMeans(n_clusters=bestK[1])
	kmeans.fit(data)

	df['clusters'] = kmeans.labels_
	#print(df)
	result = [] # list of clustering lists 

	for y in range(0,bestK[1]):
		cluster_aux = df[df['clusters'] == y]
		cluster = cluster_aux.drop(['clusters'], axis=1)
		cluster_list = cluster.values.tolist()
		result.append(cluster_list)

	print(result[0][1])
	
	return result