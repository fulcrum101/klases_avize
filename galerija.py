import streamlit as st
from PIL import Image

def Galerija_lapa():
    st.header('Galerija')
    Savicka()
    Iesvetibas()
    Modes_nedela()
    Kvests()
    Lauki()
    Mangalsala()
    st.markdown('Vairāk foto skatīt [šeit](https://drive.google.com/drive/folders/1-8uUPxiBRxLGadHia5gIDDDJ3n4GIDOv?usp=sharing)')

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
    st.image(Image.open('images/Sk_Lauki/7.jpg').rotate(270))

def Modes_nedela():
    st.subheader('RV1Ģ Modes nedeļa 2022')
    images_1 = [Image.open('images/Modes_nedela/1.jpg'), Image.open('images/Modes_nedela/2.jpg')]
    images_2 = [Image.open('images/Modes_nedela/3.JPG'), Image.open('images/Modes_nedela/4.JPG')]
    st.image(images_1)
    st.image(images_2)

def Iesvetibas():
    st.subheader('RV1Ģ 10. klašu iesvētības 2022')
    st.video('https://youtu.be/XXMnTQ010XY')

def Kvests():
    st.subheader('Klase A.L. kvestā Rīgas Centrā')
    images_1 = [Image.open('images/Kvests/1.jpeg'), Image.open('images/Kvests/2.jpeg')]
    images_2 = [Image.open('images/Kvests/3.jpeg'), Image.open('images/Kvests/4.jpeg')]
    st.image(images_1)
    st.image(images_2)

def Savicka():
    st.subheader('Sk. Savickas un 10E klases gleznas "Pēdējais vakarēdiens" interpretācija')
    images = [Image.open('images/savickas_stunda/maksla_1.jpeg'), Image.open('images/savickas_stunda/maksla_2.jpeg')]
    st.image(images)