import streamlit as st

def skolenu():
    st.subheader('Skolēnu citāti')
    st.markdown('"Skolotāj, Jūs esat mūsu televīzija."(c) Roberts')
    st.markdown('"Skolotāj, jūs šodien labi izskatāties." (c) Maksis')

def skolotaju():
    st.subheader('Skolotāju citāti')
    st.markdown('"Šito sakni nevajag. Atspārdam, tinās miglā." (c) Sk. Kriķis')
    st.markdown('"Apzīmēšana ir tāpat kā tu būtu nomainījis uzvārdu un pēc tam uzzini, ka mantojumā ir miljons, un tad centies nomainīt uzvārdu atpakaļ." (c) Sk. Kriķis')
    st.markdown('"Skolotāja kā televīzija." (c) Sk. Savicka')

def dialogi():
    st.subheader('Zeltie dialogi')
    st.markdown('"- Ar ko jūs neesat apmierināti?!?!?! - Ar pašreizējo sistēmu" (c) Sk. Vasiļevska un Raimonds')

def Citati_lapa():
    st.header('Citāti')
    skolenu()
    skolotaju()
    dialogi()