import streamlit as st
import pickle
import numpy as np
import pandas as pd



st.set_page_config(page_title="Pankreatit'te progresyon tahminleme modeli")
tabs=["Pankreatit Nedir?","Tahminleme Modeli","Tablolar","Hakkında"]
page = st.sidebar.radio("Sekmeler",tabs)

model = pickle.load(open('https://github.com/the-maintain/pythonProject/blob/main/pankreatit/model.pk1', 'rb'))

b= pd.DataFrame(columns=['SEX', 'AGE', 'WBC', 'NEU', 'LYM', 'HGB', 'PLT', 'NEU*PLT', 'SII', 'GLU', 'UREA', 'CREA', 'AST', 'ALT', 'LDH', 'AMYLASE', 'LIPASE', 'CRP', 'PLR', 'NLR', 'RADIO_SCORE', 'NEW_AMY_LIP', 'NEW_WBC_EQL', 'NEW_AMY_UREA', 'NEW_AMY_CREA'],data=[[1.0,81.0,12.9,11.44,0.96,10.9,132.0,1510.08,1573.0,111.0,36.4,0.61,43.0,25.0,229.0,2615.0,3225.0,2.53,137.0,11.0,81.0,5840.0,0.5,0.01392,4286.885246]])


if page == "Tahminleme Modeli":
    st.markdown("<h1 style='text-align:center;'>Pankreatit</h1>",unsafe_allow_html=True)
    st.write(""" Acil Serviste Akut Pankreatit Tanısı Alan Hastaların Progresyon  Tahmini""")

    SEX = st.selectbox('PATIENTS SEX',('FEMALE', 'MALE'))
    AGE = st.number_input("AGE")
    WBC = st.number_input("Lökosit Miktarı")
    NEU = st.number_input("Nötrofil Miktarı")
    LYM = st.number_input("Lenfosit Miktarı")
    HGB = st.number_input("HGB Seviyesi")
    PLT = st.number_input("Trombosit Miktarı")
    GLU = st.number_input("Kan Glukoz Düzeyi")
    UREA = st.number_input("Üre Miktarı")
    CREA = st.number_input("Kreatinin Seviyesi")
    AST = st.number_input("AST")
    ALT = st.number_input("ALT")
    LDH = st.number_input("LDH")
    AMYLASE = st.number_input("AMYLASE")
    LIPASE = st.number_input("LIPASE")
    CRP = st.number_input("CRP")
    RADIO = st.selectbox(
        'Radyolojik görüntülenmesine göre pankreas görünümü',
        ('Hafif', 'Orta', 'Ağır'))

    a = pd.DataFrame(data=[[0 if SEX == "FEMALE" or RADIO == "MALE" else 1,AGE,WBC,NEU,LYM,HGB,PLT,NEU*PLT,NEU*PLT/LYM,GLU,
                           UREA,CREA,AST,ALT,LDH,AMYLASE,LIPASE,CRP,PLT/LYM,NEU/LYM,
                          0 if  RADIO=="Hafif" or RADIO=="Orta" else 1,AMYLASE+LIPASE,AST*ALT,AMYLASE/UREA,AMYLASE/CREA]],
                    columns=['SEX', 'AGE', 'WBC', 'NEU', 'LYM', 'HGB','PLT','NEU*PLT', 'SII', 'GLU',
                             'UREA', 'CREA','AST', 'ALT', 'LDH', 'AMYLASE', 'LIPASE', 'CRP','PLR', 'NLR',
                              'RADIO_SCORE','NEW_AMY_LIP','NEW_WBC_EQL', 'NEW_AMY_UREA', 'NEW_AMY_CREA'])


    button=st.button("Tahmin Et")
    if button==True:
        with st.spinner("Tahmin yapılıyor,Lütfen Bekleyiniz..."):
            output = model.predict(a)
            st.write(output)
            st.write("Patient's progress is getting {}".format("worse" if output==1 else "better"))



if page == "Pankreatit Nedir?":
    st.markdown("<h1 style='text-align:center;'>PANKREAS ENZİMLERİNİN PANKREAS İÇİNDE AKTİVASYONUDUR</h1>",unsafe_allow_html=True)




