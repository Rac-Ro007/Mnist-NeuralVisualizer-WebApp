
import streamlit as st
import json
import requests
import matplotlib.pyplot as plt
import numpy as np

URI = 'http://127.0.0.1:5000'

st.title('Neural Network Visualizer')
st.sidebar.markdown('## Input Image')

if st.button('Get Random Prediction'):
  response = requests.post(URI, data={})
  response = json.loads(response.text)
  preds = response.get('prediction')
  image = response.get('image')
  image = np.reshape(image, (28,28))

  st.image(image, width=150)  