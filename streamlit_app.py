import streamlit as st 
import pandas as pd 
import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Km Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Engine Size')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write ('Estimasi harga mobil bekas dalam Ponds : ', predict)
    st.write ('Estimasi harga mobil bekas dalam IDR (Juta) :', predict*16500)
  
##Membuat sidebar
st.sidebar.title("Sidebar")
input_text = st.sidebar.text_input("Masukkan sesuatu:")
input_number = st.sidebar.number_input("Masukkan angka:", min_value=0, max_value=100)

###Tombol untuk memindahkan konten
if st.sidebar.button("Tampilkan di Mainbar"):
    st.session_state['show_content'] = True
else:
    st.session_state['show_content'] = False

#Menampilkan hasil di mainbar
st.title("Mainbar")
if 'show_content' in st.session_state and st.session_state['show_content']:
    st.write(f"Teks dari sidebar: {input_text}")
    st.write(f"Angka dari sidebar: {input_number}")
else:
    st.write("Tidak ada konten untuk ditampilkan.")

def main() : 
  
if __name__ == '__main__' : 
  main()
