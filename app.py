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

def afficher_voyelle(notation, nom, son, exemple, astuce):
    st.markdown(f"""
    <div class="letter-card">
        <div class="thai-char">{notation}</div>
        <div class="letter-name">{nom}</div>
        <div class="letter-sound">Son : {son}</div>
        <div class="letter-sound">Exemple : {exemple}</div>
        <div class="letter-tip">💡 {astuce}</div>
    </div>
    """, unsafe_allow_html=True)

# 5. Onglet Consonnes
with tab1:
    st.title("🔤 Les Consonnes Thaïes")
    st.write(
        "On progresse par groupes de sons, en commençant par les plus fréquents. "
        "Pas besoin de retenir leur classe tonale pour l'instant."
    )
    st.divider()

    # Structure : (titre du groupe, sous-titre, liste de (thai, nom, son, astuce))
    groupes = [
        ("Groupe 1 — Les incontournables", "Sons coupés", [
            ("ก", "Ko Kai", '"k" (comme dans kayak)', "Ressemble à une petite poule qui picore."),
            ("ต", "To Tao", '"t" (comme dans tortue)', "Ressemble à ด mais avec une antenne différente."),
            ("ด", "Do Dek", '"d" (comme dans dodo)', "Un rond avec une petite queue vers le haut."),
            ("บ", "Bo Baimai", '"b" (comme dans bébé)', "Une bosse simple, facile à repérer."),
        ]),
        ("Groupe 2 — Les sons qui durent", "Sons continus", [
            ("ม", "Mo Ma", '"m" (comme dans maman)', "Un rond avec une petite boucle sur le côté."),
            ("ล", "Lo Ling", '"l" (comme dans lune)', "Ressemble à un petit hameçon qui remonte."),
            ("น", "No Nu", '"n" (comme dans nature)', "Une vague qui se termine par une boucle en bas."),
            ("ว", "Wo Waen", '"w" / "ou" (comme dans wagon)', "Un rond presque parfait."),
        ]),
        ("Groupe 3 — Sons distincts fréquents", "À apprendre séparément", [
            ("ง", "Ngo Ngu", '"ng" (comme dans parking)', "Un rond avec une grande boucle qui pend en dessous."),
            ("ย", "Yo Yak", '"y" (comme dans yaourt)', "Une boucle avec une longue queue vers le bas."),
            ("ร", "Ro Ruea", '"r" roulé (à l\'espagnole)', "Ressemble à un petit crochet pointu."),
            ("ห", "Ho Hip", '"h" (comme dans hôtel)', "Une forme arrondie avec un pic sur le côté."),
        ]),
        ("Groupe 4 — La famille \"P\"", "Nuances p / ph / f", [
            ("ป", "Po Pla", '"p" sec, non-aspiré', "Un pic pointu avec un petit crochet au sommet."),
            ("ผ", "Pho Phueng", '"ph" aspiré (souffle d\'air)', "Ressemble à ป mais avec une boucle en plus."),
            ("พ", "Pho Phan", '"ph" aspiré (souffle d\'air)', "Une grande boucle ouverte sur la gauche."),
            ("ฟ", "Fo Fan", '"f" (comme dans fleur)', "Ressemble à ฝ, avec une petite antenne au sommet."),
        ]),
        ("Groupe 5 — La famille \"Kh / Th\"", "Sons aspirés fréquents", [
            ("ค", "Kho Khwai", '"kh" aspiré (comme dans loch)', "Une forme arrondie avec une queue basse."),
            ("ข", "Kho Khai", '"kh" aspiré', "Ressemble à ค mais plus anguleux."),
            ("ท", "Tho Thahan", '"th" aspiré (pas comme "the" anglais)', "Une boucle avec une longue queue horizontale."),
            ("ถ", "Tho Thung", '"th" aspiré', "Une forme simple avec un petit chapeau."),
        ]),
        ("Groupe 6 — La famille \"Ch / S\"", "Sifflantes et chuintantes", [
            ("จ", "Cho Chan", '"tch" (comme dans tchèque)', "Une boîte avec une petite queue qui dépasse."),
            ("ช", "Cho Chang", '"tch" aspiré', "Ressemble à ข avec une forme plus arrondie."),
            ("ซ", "So So", '"s" (comme dans soleil)', "Une double boucle qui ondule."),
            ("ส", "So Suea", '"s" (le plus courant des \"s\")', "Une forme en zigzag avec une queue."),
        ]),
    ]

    for titre, sous_titre, lettres in groupes:
        st.subheader(titre)
        st.caption(sous_titre)
        col1, col2 = st.columns(2)
        for i, (thai, nom, son, astuce) in enumerate(lettres):
            with (col1 if i % 2 == 0 else col2):
                afficher_lettre(thai, nom, son, astuce)
        st.divider()

    # Groupe bonus : lettres rares, sons déjà connus
    st.subheader("Groupe Bonus — Lettres plus rares")
    st.caption("Tu les croiseras occasionnellement, mais elles partagent un son déjà appris ci-dessus. Pas besoin de les mémoriser en priorité.")

    rares = [
        ("ฆ", "kh (comme ค)"), ("ฌ", "tch (comme ช)"), ("ญ", "y (comme ย)"),
        ("ฎ", "d (comme ด)"), ("ฏ", "t (comme ต)"), ("ฐ", "th (comme ถ)"),
        ("ฑ", "th (comme ท)"), ("ฒ", "th (comme ท)"), ("ณ", "n (comme น)"),
        ("ธ", "th (comme ท)"), ("ฝ", "f (comme ฟ)"), ("ภ", "ph (comme พ)"),
        ("ศ", "s (comme ส)"), ("ษ", "s (comme ส)"), ("ฬ", "l (comme ล)"),
        ("อ", "muet / support de voyelle"), ("ฮ", "h (comme ห)"),
    ]

    cols = st.columns(4)
    for i, (thai, note) in enumerate(rares):
        with cols[i % 4]:
            st.markdown(f"""
            <div style="text-align:center; padding:10px; background-color:#1A1D24; border-radius:8px; margin-bottom:10px;">
                <div style="font-size:2rem;">{thai}</div>
                <div style="font-size:0.8rem; color:#9AA0A6;">{note}</div>
            </div>
            """, unsafe_allow_html=True)

    st.divider()
    st.success("✅ Tu as maintenant vu les 42 consonnes ! Direction l'onglet Voyelles pour commencer à former des syllabes.")

with tab2:
    st.title("🔊 Les Voyelles Thaïes")
    st.write(
        "Contrairement aux consonnes, les voyelles peuvent se placer avant, après, "
        "au-dessus, en dessous, ou même tout autour de la consonne. "
        "Le tiret (-) dans chaque symbole représente la place de la consonne. "
        "On utilise ก (Ko Kai) comme exemple dans toutes les cartes."
    )
    st.divider()

    groupes_voyelles = [
        ("Groupe 1 — Voyelles courtes simples", "Position fixe autour de la consonne", [
            ("-ะ", "Sara A", '"a" court (comme dans "patte")', "กะ", "Se place juste après la consonne."),
            ("-ิ", "Sara I", '"i" court (comme dans "ici")', "กิ", "Petit trait au-dessus de la consonne."),
            ("-ึ", "Sara Ue", '"eu" court, bouche étirée', "กึ", "Au-dessus, ressemble à -ิ mais avec deux pics."),
            ("-ุ", "Sara U", '"ou" court (comme dans "coup")', "กุ", "Petite boucle sous la consonne."),
        ]),
        ("Groupe 2 — Voyelles longues simples", "Versions allongées des précédentes", [
            ("-า", "Sara Aa", '"a" long (comme dans "pâte")', "กา (= corbeau !)", "Trait vertical après la consonne."),
            ("-ี", "Sara Ii", '"i" long (comme dans "midi")', "กี", "Comme -ิ mais avec une petite queue en plus."),
            ("-ือ", "Sara Uea", '"eu" long, bien étiré', "กือ", "Combine -ื et อ ensemble."),
            ("-ู", "Sara Uu", '"ou" long (comme dans "loup")', "กู", "Comme -ุ mais la boucle descend plus bas."),
        ]),
        ("Groupe 3 — Voyelles qui entourent la consonne", "Avant + après la consonne", [
            ("เ-ะ", "Sara E (court)", '"é" court', "เกะ", "Trait avant la consonne, ะ après."),
            ("เ-", "Sara E (long)", '"é" long (comme "été")', "เก", "Juste devant la consonne, seule."),
            ("แ-ะ", "Sara Ae (court)", '"è" court', "แกะ (= mouton !)", "Deux traits obliques devant."),
            ("แ-", "Sara Ae (long)", '"è" long (comme "père")', "แก", "Comme au-dessus, sans le ะ final."),
            ("โ-ะ", "Sara O (court)", '"o" court', "โกะ", "Trait vertical devant, rond après."),
            ("โ-", "Sara O (long)", '"o" long (comme "rose")', "โก", "Trait vertical devant, seul."),
            ("เ-าะ", "Sara O (ouvert court)", '"o" ouvert court (comme "botte")', "เกาะ (= île !)", "Combinaison เ + าะ."),
            ("-อ", "Sara Aw (long)", '"o" ouvert long (comme "or")', "กอ", "Après la consonne, ressemble à อ."),
            ("เ-อะ", "Sara Oe (court)", '"eu" ouvert, court', "เกอะ", "Rare — combinaison เ + อะ."),
            ("เ-อ", "Sara Oe (long)", '"eu" ouvert long (comme "peur")', "เกอ", "Combinaison เ + อ."),
        ]),
        ("Groupe 4 — Diphtongues", "Voyelles composées de deux sons", [
            ("เ-ีย", "Sara Ia", '"ia" (comme dans "Provencia")', "เกีย", "Combine เ, -ี et ย."),
            ("เ-ือ", "Sara Uea", '"euua" glissé', "เกือ", "Combine เ, -ื et อ."),
            ("-ัว", "Sara Ua", '"oua" (comme dans "ouate")', "กัว", "Petit crochet au-dessus + อ après."),
        ]),
        ("Groupe 5 — Voyelles spéciales", "À mémoriser telles quelles", [
            ("-ำ", "Sara Am", '"am"', "กำ (= faire, tenir !)", "Combine -ั et ม en un seul symbole."),
            ("ใ-", "Sara Ai (type 1)", '"aï" (comme dans "ail")', "ใจ (= cœur !)", "Se place avant. N'apparaît que dans ~20 mots fixes."),
            ("ไ-", "Sara Ai (type 2)", '"aï" (comme dans "ail")', "ไก่ (= poulet !)", "Se place avant. Bien plus fréquent que ใ-."),
            ("เ-า", "Sara Ao", '"ao" (comme dans "Mao")', "เกา (= gratter !)", "Combine เ et า autour de la consonne."),
        ]),
    ]

    for titre, sous_titre, voyelles in groupes_voyelles:
        st.subheader(titre)
        st.caption(sous_titre)
        col1, col2 = st.columns(2)
        for i, (notation, nom, son, exemple, astuce) in enumerate(voyelles):
            with (col1 if i % 2 == 0 else col2):
                afficher_voyelle(notation, nom, son, exemple, astuce)
        st.divider()

    st.success("✅ Tu connais maintenant toutes les voyelles principales ! Direction l'onglet Tons pour la dernière brique avant de lire couramment.")

with tab3:
    st.title("🎵 Les Tons")
    st.write("Contenu à venir.")

with tab4:
    st.title("📖 Lecture guidée")
    st.write("Contenu à venir.")

with tab5:
    st.title("🧩 Exercices")
    st.write("Contenu à venir.")
