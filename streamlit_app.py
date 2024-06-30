import streamlit as st 
import pandas as pd 
import pickle

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.sidebar.number_input('Input Tahun Mobil')
mileage = st.sidebar.number_input('Input Km Mobil')
tax = st.sidebar.number_input('Input Pajak Mobil')
mpg = st.sidebar.number_input('Input Konsumsi BBM Mobil')
engineSize = st.sidebar.number_input('Input Engine Size')

def main() : 
    predict = ''
    
    if st.sidebar.button('Estimasi Harga'):
        predict = model.predict(
            [[year, mileage, tax, mpg, engineSize]]
        )
        st.write ('Estimasi harga mobil bekas dalam Ponds : ', predict)
        st.write ('Estimasi harga mobil bekas dalam IDR (Juta) :', predict*16500)
  
if __name__ == '__main__' : 
  main()
