from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

documents = ["your", "documents", "here"]

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

print(kmeans.labels_)
