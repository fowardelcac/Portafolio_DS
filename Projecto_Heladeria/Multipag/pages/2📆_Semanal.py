import streamlit as st
import time

st.set_page_config(
    page_title = "Semanal.",
    page_icon = ":calendar:",
)

def info_sem():
    st.title("Semanales.")
    # creacion datasets
    if 'data_sem' in st.session_state:
        df = st.session_state.data_sem
        st.subheader("Helados mas vendidos de mayor a menor.")
        fecha = st.selectbox("Ingrese fecha: ", df.index)
        df_ordenado = df.loc[str(fecha)].sort_values(ascending = False)
            
        st.write(df_ordenado)
        st.session_state['Contador_sem'] += 1
        
    else:
         df = st.session_state.file
         st.session_state['data_sem'] = df.set_index('Fecha')

if st.session_state.Contador_sem == 0:
    with st.spinner('Cargando'):
        time.sleep(5)
    st.success('Done!')
    info_sem()

else:
    info_sem()


