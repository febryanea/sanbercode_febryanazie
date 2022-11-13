import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json, requests, re
import tweepy
import string
import requests 
from bs4 import BeautifulSoup 
from urllib.request import urlopen
import preprocessor as p
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist


option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('Home','Dataframe','Chart')
)

if option == 'Home' or option == '':
    st.write("""# Halaman Utama""") #menampilkan halaman utama
elif option == 'Dataframe':
    st.write("""## Data Source""") #menampilkan judul halaman dataframe
    df = pd.read_csv('news_resesi.csv')

    df #menampilkan dataframe
elif option == 'Chart':
    st.write("""## Draw Charts""") #menampilkan judul halaman 

    #membuat variabel chart data yang berisi data dari dataframe
    #data berupa angka acak yang di-generate menggunakan numpy
    #data terdiri dari 2 kolom dan 20 baris
    chart_data = pd.DataFrame(
        np.random.randn(20,2), 
        columns=['a','b']
    )
    #menampilkan data dalam bentuk chart
    st.line_chart(chart_data)
    #data dalam bentuk tabel
    chart_data