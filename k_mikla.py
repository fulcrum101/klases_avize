import streamlit as st
from PIL import Image
import base64
import time

def k_mikla_lapa():
    st.header('Krustvārdu mīkla')
    image = Image.open('images/crossword/10E_crossword.png')
    image_answer = Image.open('images/crossword/10E_crossword_answer.png')
    st.image(image, caption='Krustvārdu mīkla par 10E. Autors: Jaunzems Jānis Helvijs')
    #FileDownloader(image, text='Lejuplādēt krustvārdu mīklu').download()
    #FileDownloader(image, filename='10E_crossword_answer', text='Lejuplādēt krustvārdu mīklas atbildi').download()
    st.download_button(
        label="Lejuplādēt krustvārdu mīklu",
        data=image,
        file_name='10E_crossword.png',
    )
    st.download_button(
        label="Lejuplādēt krustvārdu mīklas atbildi",
        data=image,
        file_name='10E_crossword_anwer.png',
    )


timestr = time.strftime("%Y%m%d-%H%M%S")


class FileDownloader(object):

    def __init__(self, data, text, filename='10E_crossword', file_ext='png'):
        super(FileDownloader, self).__init__()
        self.data = data
        self.filename = filename
        self.file_ext = file_ext
        self.text = text

    def download(self):
        b64 = base64.b64encode(self.data.encode()).decode()
        new_filename = "{}_{}_.{}".format(self.filename, timestr, self.file_ext)
        st.markdown(f"#### {self.text} ###")
        href = f'<a href="data:file/{self.file_ext};base64,{b64}" download="{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)