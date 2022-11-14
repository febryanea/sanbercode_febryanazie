import streamlit as st
import pandas as pd
import numpy as np


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
    df2 = pd.read_csv('df_clean.csv')
    df2 #menampilkan dataframe

    st.write("""## Data Sentimen""") #menampilkan judul halaman dataframe
    df3 = pd.read_csv('df_final.csv')
    df3 #menampilkan dataframe
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