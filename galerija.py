import streamlit as st
from PIL import Image

def Galerija_lapa():
    st.header('Galerija')
    Mangalsala()

def Mangalsala():
    st.subheader('Klases saliedēšanas pasākums Mangaļsalā')
    image_1 = Image.open('images/Mangalsala/1.jpg')
    st.image(image_1, caption='Klases kopēja bilde')
    images = [Image.open('images/Mangalsala/1.jpg'), Image.open('images/Mangalsala/2.jpg'), Image.open('images/Mangalsala/3.jpg')]
    st.image(images)