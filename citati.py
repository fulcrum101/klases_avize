import streamlit as st

def skolenu():
    st.subheader('Skolēnu citāti')
    st.markdown('"Skolotāj, Jūs esat mūsu televīzija."(c) Roberts')
    st.write('----------')
    st.markdown('"Skolotāj, jūs šodien labi izskatāties." (c) Maksis')
    st.write('----------')
    st.markdown('"Suicide is just rerolls in life" (c) Roberts')


def skolotaju():
    st.subheader('Skolotāju citāti')
    st.markdown('"Šito sakni nevajag. Atspārdam, tinās miglā." (c) Sk. Kriķis')
    st.write('----------')
    st.markdown('"Apzīmēšana ir tāpat kā tu būtu nomainījis uzvārdu un pēc tam uzzini, ka mantojumā ir miljons, un tad centies nomainīt uzvārdu atpakaļ." (c) Sk. Kriķis')
    st.write('----------')
    st.markdown('"Skolotāja kā televīzija." (c) Sk. Savicka')

def dialogi():
    st.subheader('Zeltie dialogi')
    st.markdown('"- Ar ko jūs neesat apmierināti?!?!?! - Ar pašreizējo sistēmu" (c) Sk. Vasiļevska un Raimonds')
    st.write('----------')
    st.markdown('"-.... Or just plug 12V to 3.7  - Plug computer into nuclear reactor. No user = no problem" (c) Roberts un Veronika')
    st.write('----------')

def Citati_lapa():
    st.header('Citāti')
    skolenu()
    skolotaju()
    dialogi()
    st.caption('Citātus savāca Ernests Kazakevičs un Kristofers Stūris')