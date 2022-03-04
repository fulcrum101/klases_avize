import streamlit as st

from galvena import Galvena_lapa
from notikumi import Notikumi_lapa
from intervijas import Intervijas_lapa
from fakti import Fakti_lapa
from citati import Citati_lapa
from joki import Joki_lapa
from k_mikla import K_mikla_lapa
from galerija import Galerija_lapa



def main():
    st.set_page_config(
        page_title="E-Avīze",
        page_icon="🧊"
    )

    st.title('E-Avīze')
    st.caption('10E klases avīze')
    st.sidebar.title("Sadaļa")
    menu = "Galvenā"
    menu = st.sidebar.selectbox("Izvēlāties, kādu sadaļu Jūs gribat aplūkot.",
                                    ["Galvenā", "Notikumi", "Intervijas", "Fakti", "Citāti", "Joki", "Krustvārdu mīkla", "Galerija"])
    if menu == "Galvenā":
        Galvena_lapa()
    elif menu == "Notikumi":
        Notikumi_lapa()
    elif menu == "Intervijas":
        Intervijas_lapa()
    elif menu == "Fakti":
        Fakti_lapa()
    elif menu == "Citāti":
        Citati_lapa()
    elif menu == "Joki":
        Joki_lapa()
    elif menu == "Krustvārdu mīkla":
        K_mikla_lapa()
    elif menu == "Galerija":
        Galerija_lapa()



if __name__ == '__main__':
    main()