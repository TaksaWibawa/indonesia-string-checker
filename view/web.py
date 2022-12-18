import streamlit as st
import os
from PIL import Image

from controller.open_file import open_file
from controller.raw_conversion import raw_to_cfg
from controller.cyk_algorithm.cyk_parse import parse


def run_streamlit():
    title = 'Pengecekan Pola Kalimat Bahasa Indonesia Dengan Algoritma CYK'
    titleKelompok = 'Kelompok 3 - Kelas D'

    st.set_page_config(layout='wide', page_title=title)

    # st.title(title)
    st.write(
        f"<h1 style='text-align:center; padding-bottom: 5px; font-size: 45px;'>{title}</h1>", unsafe_allow_html=True)
    st.write(
        f"<h2 style='text-align: center; font-size: 30px; font-weight: 300; padding-bottom: 40px; padding-top: 5px;' >{titleKelompok}</h2>", unsafe_allow_html=True)

    upload_file = st.file_uploader(
        'Upload Set of Rules dalam format .txt', type=['txt'])
    col1, col2 = st.columns(2, gap='small')  # 2 columns

    if upload_file and upload_file.type == 'text/plain':  # check if file is .txt
        if upload_file is not None:
            file = upload_file.getvalue().decode('utf-8')
            with open('model/rules.txt', 'w') as secondFile:
                for line in file:
                    if line != '\n':
                        secondFile.write(line)
            st.success("File berhasil diupload!")
            secondFile.close()
        else:
            st.error("File tidak ada!")

    raw_cfg = open_file('model/rules.txt')
    cnf = raw_to_cfg(raw_cfg)
    st.write(cnf)

    with col1:
        string_input = st.text_input(
            'Kalimat Yang Dicek : ', placeholder='Masukan Kalimat')
        list_string = string_input.split(' ')
        button_click = st.button('Cek Kalimat', type='primary')

        if button_click:
            if len(list_string) <= 1:
                st.error("Kalimat tidak boleh kosong!")
            elif string_input != '':
                st.write('<br><p>Filling Table:</p>', unsafe_allow_html=True)
                parse(cnf, string_input.split(' '))

    with col2:
        st.write("### Set of Rules :")
        # checking if rules.txt is empty
        if os.stat('model/rules.txt').st_size == 0:
            st.info("Upload rules terlebih dahulu!")
            contoh = Image.open('model/contoh.jpg')
            st.image(contoh, caption='Contoh Format Set of Rules')
        else:
            st.write(raw_cfg)
