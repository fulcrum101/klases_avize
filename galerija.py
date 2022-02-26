import streamlit as st
from PIL import Image

def Galerija_lapa():
    st.header('Galerija')
    Lauki()
    Mangalsala()

def Mangalsala():
    st.subheader('Klases saliedēšanas pasākums Mangaļsalā')
    image_1 = Image.open('images/Mangalsala/1.jpg')
    st.image(image_1, caption='Klases kopēja bilde')
    images = [Image.open('images/Mangalsala/2.jpg'), Image.open('images/Mangalsala/3.jpg'), Image.open('images/Mangalsala/4.jpg'), Image.open('images/Mangalsala/5.jpg')]
    st.image(images)

def Lauki():
    st.subheader('Klases pasākums A.L. laukos')
    images_1 = [Image.open('images/Sk_Lauki/1.jpg'), Image.open('images/Sk_Lauki/2.jpg'), Image.open('images/Sk_Lauki/3.jpg')]
    images_2 = [Image.open('images/Sk_Lauki/4.jpg'), Image.open('images/Sk_Lauki/5.jpg'), Image.open('images/Sk_Lauki/6.jpg')]
    st.image(images_1)
    st.image(images_2)