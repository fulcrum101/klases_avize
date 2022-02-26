import streamlit as st

def skolenu():
    st.subheader('Skolēnu citāti')
    st.markdown('"Skolotāj, Jūs esat mūsu televīzija."(c) Roberts Leizāns vizuālas mākslas skolotājai')

def skolotaju():
    st.subheader('Skolotāju citāti')

def Citati_lapa():
    st.header('Citāti')
    skolenu()
    skolotaju()
    st.markdown('Vairāk foto sk. [šeit](https://drive.google.com/file/d/10yG1lipqIEtd6k4Xw3HGWnfDyWjHQrNO/view?usp=sharing)')