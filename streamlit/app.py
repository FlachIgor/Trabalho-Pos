import streamlit as st
import requests

st.set_page_config(page_title = "Trabalho Eng. ML",layout = 'wide')

def perform_inference(data1,data2,data3,data4,data5,data6,url= 'http://127.0.0.1:5001/invocations'):
    data = {
        "dataframe_records": [
            {'lat': data1,
            'lon': data2,
            'minutes_remaining': data3,
            'period': data4,
            'playoffs': data5,
            'shot_distance': data6}
        ]
    }

    results = requests.post(url,json = data)
    results = results.json()
    pred = results['predictions'][0]
    return pred

intro = """"
# Kobe Bryant Shot Predictor

Trabalho para a disciplina de engenharia de machine learning.
Insira as variáveis para fazer a predição do acerto da cesta.
"""

st.write(intro)

entradalat= st.text_input("Insira a variável lat")
entradalon= st.text_input("Insira a variável lon")
entradaminutes_remaining= st.text_input("Insira a variável minutes_remaining")
entradaperiod= st.text_input("Insira a variável period")
entradaplayoffs= st.text_input("Insira a variável playoffs")
entradashot_distance= st.text_input("Insira a variável shot_distance")

if entradalat and entradalon and entradaminutes_remaining and entradaperiod and entradaplayoffs and entradashot_distance:
    pred = perform_inference(entradalat,entradalon,entradaminutes_remaining,entradaperiod,entradaplayoffs,entradashot_distance)
    st.write(f"A predicao e: {pred}")
