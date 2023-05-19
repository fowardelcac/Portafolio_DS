import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title = "Historicos",
    page_icon = ":books:",
)

def mensual(df):
    return df.groupby(pd.Grouper(key = 'Fecha', freq = 'M')).sum()
    # Creacion datasets
def historicos():
    st.title("Historicos. :card_index:")
    if 'data_mensual' in st.session_state:
        data_m = st.session_state.data_mensual
        suma_filas = st.session_state.suma_m
            # Muestra
        st.subheader("Hojas de calculo: ")
        dicc = dict({
                'Ventas mensuales':data_m,
                'Ventas totales por mes': suma_filas
                })
            
        hoja = st.selectbox("Que tipo de hoja de calculo desea ver:",
                         dicc.keys()
                         )
        st.write(dicc[str(hoja)])
            
        st.title("Graficos.")
            
        st.subheader("Grafico de lineas. :chart_with_upwards_trend: ")
        st.markdown("Ingrese un gusto y podra ver como ha sido su comportamiento durante el tiempo.")
        sabor = st.selectbox("Ingrese sabor:", data_m.columns)
        st.line_chart(data_m[str(sabor)])
            
        st.subheader("Grafico de barras. :bar_chart:")
        st.markdown("Este grafico muestra las ventas mensuales de una manera mas comprensible.")
        st.bar_chart(suma_filas["Total"])   
        
        
        st.session_state['Contador_historia'] += 1
        
    else:
        df = st.session_state.file
        data_m = mensual(df)
        suma_filas = pd.DataFrame()
        suma_filas["Total"] = data_m.sum(axis=1)
        st.session_state['data_mensual'] = data_m
        st.session_state['suma_m'] = suma_filas

if st.session_state.Contador_historia == 0:
    with st.spinner('Cargando'):
        time.sleep(5)
    st.success('Done!')
    historicos()
else:
    historicos()

