import streamlit as st
import pandas as pd
import numpy as np
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

    st.write("""## Data Clean""") #menampilkan judul halaman dataframe
    def preprocess(row):
    text = row['title']
    text = p.clean(text)
    return text

    #menjalankan function preprocess
    df['clean_title'] = df.apply(preprocess, axis=1)
    df['clean_title'] = df['clean_title'].str.lower()
    df['clean_title'] = df['clean_title'].str.replace('\d+', '')
    df['clean_title'] = df['clean_title'].str.translate(str.maketrans("","",string.punctuation))
    df['clean_title'] = df['clean_title'].str.replace('\n', '')
    df['clean_title'] = df['clean_title'].str.replace('\t', '')
    df['clean_title'] = df['clean_title'].str.replace(r'\b(\w{1,3})\b', '')
    df
    
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