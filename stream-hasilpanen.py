import pickle
import streamlit as st

# Membaca Model
hasilpanen_model = pickle.load(open("hasilpanenmlt_model.sav", "rb"))

# Judul Web
st.title("Prediksi Hasil Panen Melati")

# Membagi Kolom
col1, col2 = st.columns(2)

with col1:
    HPK = st.number_input("Input Nilai Hasil Panen Mlt Kecil (Kg)")

with col2:
    HPB = st.number_input("Input Nilai Hasil Panen Mlt Besar (Kg)")

with col1:
    LL = st.number_input("Input Luas Lahan Panen")

with col2:
    FC = st.number_input("Input Faktor Cuaca")

with col1:
    Pestisida = st.number_input("Input Pemakaian Pestisida")

with col2:
    Pupuk = st.number_input("Input Pemberian Pupuk")

# Code Untuk Prediksi
hasilpanen_predict = ""

# Membuat Tombol Prediksi
if st.button("Prediksi Hasil Panen"):
    hasilpanen_predict = hasilpanen_model.predict(
        [[HPK, HPB, LL, FC, Pestisida, Pupuk]]
    )

    if hasilpanen_predict[0] == 1:
        hasilpanen_predict = "Hasil Panen Meningkat"
    else:
        hasilpanen_predict = "Hasil Panen Menurun"

    st.success(hasilpanen_predict)


# Keterangan
st.write(
    """

# Keterangan :

    FAKTOR CUACA :
        2 = Panas
        3 = Hujan
    LUAS LAHAN :
        4 = 4000 m2
        5 = 6000 m2
    PESTISIDA :
        6 = Tidak Pakai
        7 = Pakai
    PUPUK :
        8 = Tidak
        9 = Ya
"""
)
