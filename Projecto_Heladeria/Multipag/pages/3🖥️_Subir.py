import pandas as pd
import streamlit as st

st.set_page_config(
    page_title = "Subir.",
    page_icon = ":open_file_folder:",
)

def cargar():
    file = st.file_uploader("Cargar archivo excel", type = ['xlsx'])

    if file is not None:
        df = pd.read_excel(file)
        df.dropna(inplace=True)
        df = df.drop(['Unnamed: 0'], axis=1) 
        st.session_state.file = df
    
        st.session_state['Contador_historia'] = 0
        st.session_state['Contador_sem'] = 0

st.title("Subir archivo :computer:")
st.markdown("Cada vez que se se quiera actualizar los datos, se debe subir nuevamente un archivo actualizado")
cargar()

#st.session_state.file =  st.experimental_data_editor(st.session_state.file, num_rows= "dynamic")
