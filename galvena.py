import streamlit as st
from PIL import Image

def Galvena_lapa():
    # WELCOME TEXT
    st.markdown("```print('Čau!')```")
    st.markdown('Mēs esam Rīgas Valsts 1. ģimnāzijas programmēšanas novirziena 10. klase!')

    #main_image = Image.open("C:/Users/misst/OneDrive/Desktop/other/klases_avize/images/main_photo.jpeg")
    #st.image('https://github.com/fulcrum101/klases_avize/blob/11dbbf8e7c61510dbb3e1ef473cb23d31febb4d2/images/main_photo.jpeg', caption='10.E klase mūsu pirmajā pasakumā Mangaļsalā.')
    main_image = Image.open('images/main_photo.jpeg')
    st.image(main_image, caption='10.E klase mūsu pirmajā pasakumā Mangaļsalā.')
    st.markdown('Un šajā mājās lapā pēc mūsu klases audzinātajas pieprasījuma Jūs varat mūs iepazīt tūvāk!')

    st.markdown('\n\n\n')
    st.markdown('Varbūt Jums būs noderīgas saites:')
    st.markdown("-  [A.L. apsveikums Ziemassvētkos](https://fulcrum101.github.io/gift_for_teacher/)")
    st.markdown("-  [Mūsu Instagram konts](https://www.instagram.com/rv1g10e/)")
    st.markdown("-  [RV1Ģ Vidusskolēnu domes Instagram konts](https://www.instagram.com/rv1g_vd/)")
    st.markdown("-  [Mūsu skolas kaimiņu Instagram konts](https://www.instagram.com/rv1g10a/)")
