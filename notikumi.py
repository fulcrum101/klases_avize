import streamlit as st
from PIL import Image

def Notikumi_lapa():
    st.header('Notikumi')
    ### INTRO
    st.markdown('Nav šaubu, ka no 1. septembra mēs kopā kā vienota klase esam piedzīvojuši neticami daudz interesantu notikumu. Mūsu klases audzinātāja A.L. padara skumjo skolēnu ikdienu par pilno ar piedzīvojumiem filmu.')
    ###
    Mangalsala()
    Lauki()
    Modes_nedela()
    ###
    st.markdown('Šeit noteikti mūsu klases piedzīvojumu grāmata nebeidzas un mēs ar nepacietību gaidām jaunus izaicinājumus un jautrus piedzīvojumus, kurus mūsu dzīves ceļā pretī liks liktenis!')
    st.caption('Raksta autore Veronika Lohmanova')

def Mangalsala():
    st.subheader('Klases saliedēšanās pasākums Mangaļsalā')
    st.markdown('Pēc A.L. iniciatīvas pirmais pasākums bija mūsu ekskursija, klases saliedēšanas pasākums Mangaļsalā. 2022. gada 20. septembrī pēc stundām mēs visi kopā devāmies jaunajā, pārsteidzošajā ceļojumā. Ar 24. autobusu (Abrenes iela – Mangaļsala) mēs braucām no Inženieru ielas līdz Mangaļsalai. Tur mūs jau gaidīja jautrie pasākuma vadītāji un tā mēs sākam rakstīt mūsu klases piedzīvojumu grāmatu.')
    image = Image.open('images/Mangalsala/5.jpg')
    st.image(image)
    st.write('----------')

def Lauki():
    st.subheader('Ceļojums A.L. laukos')
    st.markdown('Nākamais izaicinājums bija ceļojums uz klases audzinātājas laukiem Ogres apkārtnē. Viss sākas 1. oktobrī. Tur mēs tikām ar vilcienu Rīga-Ogre un tad ar kājām. Daļa no klases saputrojas meža un purva vidū, tomēr mēs atradām ceļu atpakaļ. Tas bija īsts izaicinājums, jo mēs paši braucām – klases audzinātāju satikām jau tikai laukos. Jau noguruši atradām mūsu dārgo skolotāju. Visi sāk jau atpūsties, bet piegāja vēl viens izaicinājums – ēdiena pagatavošana. Draudzīgi, kā īsta ģimene, mēs pārvarējām šo izaicinājumu. Visi piekrita, ka dzīvē nekad nebija ēduši šādu garšīgu soļanku un banānus ar šokolādi. Pirmā diena [un nakts] beidzās ar burvīgo pulcēšanas pie ugunskura.')
    image = Image.open('images/notikumi/ugunskuris.jpg').rotate(270)
    st.image(image)
    st.markdown('Un pēc salīdzinoši īsa miega modinātājs, dažiem par nelaimi, zvana! Sešos no rīta jau vilciens klāt. Noguruši, tomēr laimīgi, mēs atbraucām atpakaļ uz mūsu mīļo skolu. Šī bija otrā lapa mūsu klases piedzīvojumu grāmatā. Kā gudri ļaudis saka – viena piedzīvojuma beigas ir otra sākums.')
    st.write('----------')

def Modes_nedela():
    st.subheader('RV1Ģ Modes nedēļa 2022 un 10. klašu iesvētības')
    st.markdown('Protams, mūsu skolas Vidusskolēnu dome nevarēja neizdomāt kaut ko jaunu un aizraujošu skumīgajām un depresīvajām, un nogarlaikotajām 10. klasēm. Tādēļ mūsu grāmata atkal pāršķīra lapu.')
    st.markdown(' ')
    st.markdown('Nav šaubu, ka modes nedēļa ir viena no iespaidīgākajiem notikumiem skolas dzīvē. Katru gadu vienas nedēļas laikā skolēni var īsti izpausties – izskatu diktē tikai viņi paši. Mūsu klase noteikti nepalaida garām iespēju parādīt sevi.')
    images = [Image.open('images/notikumi/modes_nedela_1.jpeg'), Image.open('images/notikumi/modes_nedela_2.jpeg'), Image.open('images/notikumi/modes_nedela_3.jpeg')]
    st.image(images)
    st.markdown(' ')
    st.markdown('Beep-boop-boop. Saņemts uzdevums no RV1Ģ VD. Mūsu klases izaicinājums bija nofilmēt veikala "RIMI" reklāmu. Skolas ģimenes fantāzija arī šoreiz nepievīla. Žūrija pat piešķīra mums Viszvaigžņotākās reklāmas titulu! Mēs visi priekpilni pavadījām laiku un pat saņemam kādu īpašu balvu! Tik foršs piedzīvojums!')
    st.video('https://youtu.be/XXMnTQ010XY')
    st.video('https://youtu.be/MZkHay8L8Lk')
    st.write('----------')

def Ziemassvetki():
    st.subheader('Ziemassvētki ir klāt!')
    st.markdown('''Zvani skan, zvani skan,
                Ziemassvētki brauc:
                Dāvanas būs tev un man,
                Visi bērni sauc!''')
    image = Image.open('images/notikumi/ziemassvetki.jpeg')
    st.image(image)
    st.markdown('Vēl viena sirdi sildoša diena maza skolēnu dzīvē. Klases audzinātāja A.L. padarīja svētku laiku vēl omulīgāku! Apmainoties ar vissiltākajiem novēlējumiem un vissaldākajām dāvanām, ar tīro sirdi mēs devāmies ziemas brīvlaikā!')
    st.write('----------')
