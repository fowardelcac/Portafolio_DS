import streamlit as st

st.set_page_config(
    page_title = "Inicio",
    page_icon = "👋",
)

st.title("Heladeria Cordobesa :icecream:")
st.header("Bienvenido")
st.markdown('''Esta es una aplicación desarrollada para visualizar de manera rápida y sencilla 
  un análisis rápido del negocio.  Cuenta con cuatro pestañas: ''')
st.markdown('''
                - Inicio
                - Historico.
                - Semanal.
                - Carga
        ''')
st.header('Inicio. :sparkles:')
st.markdown(''' Esta es la pestalla principal, donde cuenta con una breve introduccion 
                ''')
                
st.header('Historico. :date:')
st.markdown('''En esta pestaña se podrá visualizar de manera rápida una hoja de cálculo con la cantidad 
            de helado vendido, existe la opción de ingresar determinado mes y recibir una hoja de cálculo 
            con las ventas ordenadas de mayor a menor, incluso ver distintos gráficos.''')
st.header('Semanal. :calendar:')
st.markdown('''En esta pestaña se podrá visualizar a través de una hoja de cálculo las ventas semanales
            ordenadas de manera descendente.''')
            
st.header('Carga. :open_file_folder:')
st.markdown('''Aqui sera donde debe cargar sus datos actualizados''')
            

