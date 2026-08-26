import streamlit as st

# 1. Configuration de la page
st.set_page_config(
    page_title="Thaï 101 - Apprendre à lire le Thaï",
    page_icon="🇹🇭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS Personnalisé (thème sombre + responsive mobile)
st.markdown("""
<style>
    .stApp {
        background-color: #0E1117;
        color: #E0E0E0;
    }

    /* Titres */
    h1 { font-size: 2.2rem; }
    h2 { font-size: 1.6rem; }
    h3 { font-size: 1.3rem; }

    /* Cartes de consonnes */
    .letter-card {
        background-color: #1A1D24;
        border: 1px solid #2A2E37;
        border-left: 4px solid #E63946;
        border-radius: 10px;
        padding: 16px;
        margin-bottom: 14px;
    }
    .thai-char {
        font-size: 3rem;
        line-height: 1;
        margin-bottom: 6px;
    }
    .letter-name {
        font-weight: 600;
        color: #FFFFFF;
        font-size: 1.05rem;
    }
    .letter-sound {
        color: #B0B0B0;
        font-size: 0.9rem;
    }
    .letter-tip {
        color: #9AA0A6;
        font-size: 0.85rem;
        margin-top: 6px;
        font-style: italic;
    }

    /* Onglets adaptés au tactile */
    button[data-baseweb="tab"] {
        font-size: 0.95rem;
        padding: 10px 14px;
    }

    /* Mobile : réduire les marges et tailles */
    @media (max-width: 640px) {
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            padding-top: 1.5rem;
        }
        .thai-char { font-size: 2.4rem; }
        h1 { font-size: 1.6rem; }
        h2 { font-size: 1.3rem; }
    }
</style>
""", unsafe_allow_html=True)

# 3. Navigation par onglets
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🔤 Consonnes",
    "🔊 Voyelles",
    "🎵 Tons",
    "📖 Lecture guidée",
    "🧩 Exercices"
])

# 4. Fonction d'affichage d'une carte de lettre
def afficher_lettre(thai, nom, son, astuce):
    st.markdown(f"""
    <div class="letter-card">
        <div class="thai-char">{thai}</div>
        <div class="letter-name">{nom}</div>
        <div class="letter-sound">Son : {son}</div>
        <div class="letter-tip">💡 {astuce}</div>
    </div>
    """, unsafe_allow_html=True)

# 5. Onglet Consonnes
with tab1:
    st.title("🔤 Les Consonnes Thaïes")
    st.write(
        "On commence par un premier groupe de consonnes très fréquentes, "
        "choisies pour leur simplicité visuelle. Pas besoin de retenir leur "
        "classe tonale pour l'instant — on se concentre uniquement sur la forme et le son."
    )
    st.divider()

    st.subheader("Groupe 1 — Les incontournables")

    col1, col2 = st.columns(2)

    with col1:
        afficher_lettre("ก", "Ko Kai", "\"k\" (comme dans kayak)", "Ressemble à une petite poule qui picore.")
        afficher_lettre("ด", "Do Dek", "\"d\" (comme dans dodo)", "Un rond avec une petite queue vers le haut.")

    with col2:
        afficher_lettre("ต", "To Tao", "\"t\" (comme dans tortue)", "Ressemble à ด mais avec une antenne différente.")
        afficher_lettre("บ", "Bo Baimai", "\"b\" (comme dans bébé)", "Une bosse simple, facile à repérer.")

    st.divider()
    
    st.subheader("Groupe 2 — Les sons qui durent")
    st.caption("Contrairement au groupe 1 (sons coupés), ces consonnes ont des sons qu'on peut prolonger.")

    col1, col2 = st.columns(2)

    with col1:
        afficher_lettre("ม", "Mo Ma", "\"m\" (comme dans maman)", "Un rond avec une petite boucle sur le côté, comme une tête ronde.")
        afficher_lettre("ล", "Lo Ling", "\"l\" (comme dans lune)", "Ressemble à un petit hameçon qui remonte.")

    with col2:
        afficher_lettre("น", "No Nu", "\"n\" (comme dans nature)", "Une vague qui se termine par une petite boucle en bas.")
        afficher_lettre("ว", "Wo Waen", "\"w\" / \"ou\" (comme dans wagon)", "Un rond presque parfait, facile à repérer.")

    st.divider()
    st.info("D'autres groupes de consonnes arrivent bientôt dans cet onglet !")

with tab2:
    st.title("🔊 Les Voyelles")
    st.write("Contenu à venir — une fois les premières consonnes bien assimilées.")

with tab3:
    st.title("🎵 Les Tons")
    st.write("Contenu à venir.")

with tab4:
    st.title("📖 Lecture guidée")
    st.write("Contenu à venir.")

with tab5:
    st.title("🧩 Exercices")
    st.write("Contenu à venir.")
