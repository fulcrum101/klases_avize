import streamlit as st
from PIL import Image

from easter_egg import rickroll

def Galvena_lapa():
    # WELCOME TEXT
    st.markdown("```print('Čau!')```")
    st.markdown('Mēs esam Rīgas Valsts 1. ģimnāzijas programmēšanas novirziena 10. klase!')

    main_image = Image.open('images/main_photo.jpeg')
    st.image(main_image, caption='10.E klase mūsu pirmajā pasakumā Mangaļsalā.')
    st.markdown('Un šajā mājās lapā pēc mūsu klases audzinātājas pieprasījuma Jūs varat mūs iepazīt tuvāk!')

    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')

    st.markdown('Varbūt Jums būs noderīgas saites:')
    st.markdown("-  [A.L. apsveikums Ziemassvētkos](https://fulcrum101.github.io/gift_for_teacher/)")
    st.markdown("-  [Mūsu Instagram konts](https://www.instagram.com/rv1g10e/)")
    st.markdown("-  [RV1Ģ Vidusskolēnu domes Instagram konts](https://www.instagram.com/rv1g_vd/)")
    st.markdown("-  [Mūsu skolas kaimiņu Instagram konts](https://www.instagram.com/rv1g10a/)")

    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')

    # BYE BYE TEXT
    st.markdown("```print('Ata!')```")
    st.markdown('#### Novēlējumi no E-Avīzes autoriem: ####')
    st.write('----------')
    ###
    st.markdown('Vēlos Jums visiem pateikties par šiem raibajiem sešiem mēnešiem! Protams, gāja kā pa kalniem, tā pa lejām, bet tas jau arī ir tas, kas padara cilvēku dzīves interesantas. Cerams, ka, dzīvojot tālāk, mūsu klase taps arvien tuvāka, un ikviens šeit jutīsies kā otrajās mājās!')
    st.caption('Jānis Helvijs Jaunzems')
    st.write('----------')
    ###
    st.markdown('Ļoti ceru, ka nākamo divu gadu laikā izdosies piedzīvot daudz aizraujošu un neaizmirstamu mirkļu. Esmu pārliecināts, ka tiksim pāri visām grūtībām un veiksmīgi turpināsim mūsu ceļu!')
    st.caption('Raimonds Vilcāns')
    st.write('----------')
    ###
    st.markdown('Ļoti ceru, ka līdz skolas beigšanai, mūsu klase paliks saliedēta kā mēs esam tagad un vairāk. Es ar nepacietību gaidu nākamos piedzīvojumus ar "skolas ģimeni')
    st.caption('Veronika Lohmanova')
    st.write('----------')
    ###
    st.markdown('Novēlu kārtīgi atpūsties brīvlaikā!')
    st.caption('Ernests Kazakevičs')
    st.write('----------')
    ###
    st.markdown('Es novēlu visiem būt cilvēcīgiem jebkurā dzīves situācijā un respektēt un atbalstīt vienam otru.')
    st.caption('Kristofers Stūris')
    st.write('----------')
    # EASTER EGG
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    password = st.text_input('Secret password', 'ONLY FOR TRUE DEVELOPERS')
    if password == '10E is the best':
        rickroll()

