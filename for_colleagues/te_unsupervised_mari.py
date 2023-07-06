# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3
#     name: python3
# ---

# + id="6x9Y8nkK2837" colab_type="code" outputId="ee8fc2ec-ca87-4397-e309-5c24e9671423" colab={"base_uri": "https://localhost:8080/", "height": 122}
from google.colab import drive
drive.mount('/content/drive')

# + id="Y85Xq2aibdal" colab_type="code" outputId="38979504-b19f-4374-be3c-95b2dd7bd66c" colab={"base_uri": "https://localhost:8080/", "height": 153}
# !pip3 install biopython
from sklearn import cluster, datasets
import numpy as np
import pandas as pd
from numpy import array
from numpy import argmax
from Bio import SeqIO
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import tensorflow
from keras.preprocessing.sequence import pad_sequences


# + id="FO2WX4U1cNI4" colab_type="code" colab={}
def fasta_frame(fasta_file):
  identifiers = []
  sequences = []
  with open(fasta_file) as f_f:
    for seq_record in SeqIO.parse(f_f, 'fasta'):
        identifiers.append(seq_record.id)
        sequences.append(seq_record.seq.lower())
  s1 = pd.Series(identifiers, name='ID')
  s2 = pd.Series(sequences, name='sequence')
  fasta_frame = pd.DataFrame(dict(ID=s1, sequence=s2))
  return(fasta_frame)
  
def ohe_fun(coluna):
  integer_encoder = LabelEncoder()  
  one_hot_encoder = OneHotEncoder(categories='auto')   
  input_features = []

  for linha in coluna[coluna.columns[1]]:
    integer_encoded = integer_encoder.fit_transform(list(linha))
    integer_encoded = np.array(integer_encoded).reshape(-1, 1)
    one_hot_encoded = one_hot_encoder.fit_transform(integer_encoded)
    input_features.append(one_hot_encoded.toarray())
  input_features=pad_sequences(input_features, padding='post')
  input_features = np.stack(input_features)
  return(input_features)
  
def flatten_sequence(pred_fasta_flat):
  dimensoes=pred_fasta_flat.shape
  n_samples=dimensoes[0]
  n_x=dimensoes[1]
  n_y=dimensoes[2]
  n_xy=(n_x * n_y)
  pred_fasta_flat=pred_fasta_flat.reshape(n_samples,n_xy)
  return(pred_fasta_flat)


# + id="knyvVK3xcggd" colab_type="code" outputId="158e28ae-1254-4bd1-cf39-ba0aba7a7a4e" colab={"base_uri": "https://localhost:8080/", "height": 424}
db_te = fasta_frame('159.fasta')
db_te

# + id="4G2c7cI2x6g4" colab_type="code" colab={}
db_te.to_csv('unsup_df.csv', index=False)

# + id="v5s21LJMewrs" colab_type="code" colab={}
integer_encoder = LabelEncoder()  
one_hot_encoder = OneHotEncoder(categories='auto')   
input_features = []

for coluna, linha in db_te['sequence'].iteritems():
  integer_encoded = integer_encoder.fit_transform(list(linha))
  integer_encoded = np.array(integer_encoded).reshape(-1, 1)
  one_hot_encoded = one_hot_encoder.fit_transform(integer_encoded)
  input_features.append(one_hot_encoded.toarray())


# + id="zRkMopIq3yW4" colab_type="code" colab={}
for arr in input_features:
  # print(input_features)
  # print(arr.shape)

# + id="1AvQKxoXew_n" colab_type="code" colab={}
input_features = pad_sequences(input_features, padding='post')
input_features = np.stack(input_features)

# + id="zfNLXbDpAGiu" colab_type="code" colab={}
# for arr in input_features:
#   print(arr.shape)

# + id="qFx4L0rYuGww" colab_type="code" colab={}
flat_seqs = flatten_sequence(input_features)

# + id="54-rA9XEzMhY" colab_type="code" colab={}
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline 
from sklearn.cluster import KMeans
from sklearn import datasets

distortions = []
K = range(1,10)
for k in K:
    kmeanModel = KMeans(n_clusters=k)
    kmeanModel.fit(flat_seqs)
    distortions.append(kmeanModel.inertia_)

# + id="kB0XwdGIzn-6" colab_type="code" outputId="c35c90b7-dba3-4940-ab1c-405d7720464a" colab={"base_uri": "https://localhost:8080/", "height": 533}
    plt.figure(figsize=(16,8))
    plt.plot(K, distortions, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Distortion')
    plt.title('The Elbow Method showing the optimal k')
    plt.show()

# + [markdown] id="oLNSBYUbtLgP" colab_type="text"
# No PCA

# + id="89YQSGjw5fWR" colab_type="code" colab={}
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

k_means = cluster.KMeans(n_clusters=5,
                         random_state=13,
                         algorithm='auto',
                         max_iter = 600,
                         verbose=0)
k_means.fit(flat_seqs)
predicted = k_means.predict(flat_seqs)

# + [markdown] id="EkoMMAR5tNVJ" colab_type="text"
# PCA

# + id="H2XQ9JMHtIZf" colab_type="code" colab={}
import sys
import numpy
from sklearn.decomposition import PCA
numpy.set_printoptions(threshold=sys.maxsize)

sklearn_pca = PCA(n_components = 2)
Y_sklearn = sklearn_pca.fit_transform(flat_seqs)

k_means = cluster.KMeans(n_clusters=3,
                         random_state=13,
                         algorithm='auto',
                         max_iter = 1200,
                         verbose=0)
k_means.fit(Y_sklearn)
labels = k_means.predict(Y_sklearn)

# + id="crvA_gxY6dWc" colab_type="code" outputId="17a00b5a-439b-47a8-c4bd-1a2835cd0512" colab={"base_uri": "https://localhost:8080/", "height": 643}
pd.set_option('display.max_rows', -1)
labSer=pd.Series(predicted)
db_te['group'] = labSer
columnsTitles = ['ID', 'group', 'sequence']
db_te = db_te.reindex(columns=columnsTitles)
db_te.sample(10)

# + id="Wr6FRMoe9GRq" colab_type="code" colab={}
db_te.to_csv('clustered_seqs.csv',index=False)

# + id="oIapdK9oJnVc" colab_type="code" colab={}
import pickle

pickle.dump(k_means,open("k_means_model.pkl", "wb"))
