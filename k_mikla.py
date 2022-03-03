import streamlit as st
from PIL import Image

def K_mikla_lapa():
    st.header('Krustvārdu mīkla')
    image = Image.open('images/crossword/10E_crossword.png')
    st.image(image, caption='Krustvārdu mīkla par 10E. Autors: Jaunzems Jānis Helvijs')
    with open("images/crossword/10E_crossword.png", "rb") as file:
        btn = st.download_button(
            label="Lejuplādēt krustvārdu mīklu",
            data=file,
            file_name="10E_crossword.png",
            mime="image/png"
        )
    with open("images/crossword/10E_crossword_answer.png", "rb") as file:
        btn = st.download_button(
            label="Lejuplādēt krustvārdu mīklas atbildi",
            data=file,
            file_name="10E_crossword_answer.png",
            mime="image/png"
        )