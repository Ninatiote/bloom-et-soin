import streamlit as st

# ----------------------------
# CONFIGURATION DE LA PAGE
# ----------------------------
st.set_page_config(
    page_title="Maison Wig (démo)",
    page_icon="💇🏾‍♀️",
    layout="wide",
)

# ----------------------------
# STYLE (élégant, noir & or, univers perruques/beauté)
# ----------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #faf7f2;
        color: #2b2320;
    }
    h1, h2, h3 {
        font-family: 'Georgia', serif;
        color: #1a1a1a;
    }
    .product-card {
        background-color: #ffffff;
        border: 1px solid #ece4d8;
        border-radius: 14px;
        padding: 16px;
        margin-bottom: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    .price-tag {
        color: #a67c27;
        font-size: 20px;
        font-weight: bold;
    }
    .old-price {
        color: #999;
        text-decoration: line-through;
        font-size: 14px;
        margin-left: 8px;
    }
    .badge-promo {
        background-color: #a83246;
        color: white;
        padding: 2px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }
    .badge-cat {
        background-color: #f1e9da;
        color: #6b5a3a;
        padding: 2px 10px;
        border-radius: 20px;
        font-size: 12px;
        margin-right: 6px;
    }
    .stButton>button {
        background-color: #1a1a1a;
        color: #f1e9da;
        border-radius: 6px;
        border: none;
        padding: 8px 20px;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #a67c27;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------
# CATALOGUE DE PRODUITS (exemple, à remplacer par tes vraies perruques)
# ----------------------------
PRODUITS = [
    {
        "id": 1,
        "nom": "RIVIÈRE - Lace HD Lisse",
        "categorie": "Lace HD",
        "longueur": "Long",
        "texture": "Lisse",
        "prix": 280.00,
        "prix_promo": None,
        "description": "Lace frontale HD 13x6, cheveux naturels lissés, effet cuir chevelu indétectable.",
        "image": "https://images.unsplash.com/photo-1595163752371-27d8235f0f3e?w=400",
    },
    {
        "id": 2,
        "nom": "SOLÈNE - Closure Bouclée",
        "categorie": "Closure",
        "longueur": "Mi-long",
        "texture": "Curly",
        "prix": 150.00,
        "prix_promo": 99.00,
        "description": "Closure 5x5, boucles définies naturelles, base souple et confortable au quotidien.",
        "image": "https://images.unsplash.com/photo-1580618672591-eb180b1a973f?w=400",
    },
    {
        "id": 3,
        "nom": "AALIYAH - Raw Hair Ondulée",
        "categorie": "Raw Hair",
        "longueur": "Long",
        "texture": "Wavy",
        "prix": 450.00,
        "prix_promo": None,
        "description": "Cheveux 100% naturels non traités, ondulation body wave, tenue longue durée.",
        "image": "https://images.unsplash.com/photo-1519699047748-de8e457a634e?w=400",
    },
    {
        "id": 4,
        "nom": "MYA - Bob Closure HD",
        "categorie": "Closure HD",
        "longueur": "Court",
        "texture": "Lisse",
        "prix": 220.00,
        "prix_promo": 180.00,
        "description": "Coupe bob tendance, lace HD indétectable, idéale pour un look quotidien discret.",
        "image": "https://images.unsplash.com/photo-1560869713-7d0a29430803?w=400",
    },
    {
        "id": 5,
        "nom": "INAYA - Lace Classique Wavy",
        "categorie": "Lace Classique",
        "longueur": "Mi-long",
        "texture": "Wavy",
        "prix": 130.00,
        "prix_promo": None,
        "description": "Lace frontale classique, texture ondulée naturelle, excellent rapport qualité-prix.",
        "image": "https://images.unsplash.com/photo-1605980776566-0486c3ac7617?w=400",
    },
    {
        "id": 6,
        "nom": "ZOÉ - Closure Frisée",
        "categorie": "Closure",
        "longueur": "Court",
        "texture": "Curly",
        "prix": 160.00,
        "prix_promo": None,
        "description": "Closure 4x4, texture kinky curly, volume naturel et racines indétectables.",
        "image": "https://images.unsplash.com/photo-1554519515-242161756769?w=400",
    },
]

CATEGORIES = ["Toutes"] + sorted(set(p["categorie"] for p in PRODUITS))
LONGUEURS = ["Toutes"] + sorted(set(p["longueur"] for p in PRODUITS))
TEXTURES = ["Toutes"] + sorted(set(p["texture"] for p in PRODUITS))

# ----------------------------
# ÉTAT DU PANIER
# ----------------------------
if "panier" not in st.session_state:
    st.session_state.panier = {}

def prix_final(produit):
    return produit["prix_promo"] if produit["prix_promo"] else produit["prix"]

def ajouter_au_panier(produit_id):
    st.session_state.panier[produit_id] = st.session_state.panier.get(produit_id, 0) + 1

def retirer_du_panier(produit_id):
    if produit_id in st.session_state.panier:
        st.session_state.panier[produit_id] -= 1
        if st.session_state.panier[produit_id] <= 0:
            del st.session_state.panier[produit_id]

def total_panier():
    total = 0
    for pid, qte in st.session_state.panier.items():
        produit = next(p for p in PRODUITS if p["id"] == pid)
        total += prix_final(produit) * qte
    return total

# ----------------------------
# EN-TÊTE
# ----------------------------
st.title("💇🏾‍♀️ Maison Wig")
st.markdown("*Nom de marque temporaire — perruques lace & closures haut de gamme.*")
st.divider()

# ----------------------------
# NAVIGATION
# ----------------------------
onglet = st.radio("Navigation", ["Boutique", "Mon panier", "FAQ"], horizontal=True, label_visibility="collapsed")

# ----------------------------
# PAGE BOUTIQUE
# ----------------------------
if onglet == "Boutique":
    st.markdown("#### Filtrer le catalogue")
    f1, f2, f3 = st.columns(3)
    with f1:
        filtre_cat = st.selectbox("Catégorie", CATEGORIES)
    with f2:
        filtre_longueur = st.selectbox("Longueur", LONGUEURS)
    with f3:
        filtre_texture = st.selectbox("Texture", TEXTURES)

    produits_filtres = [
        p for p in PRODUITS
        if (filtre_cat == "Toutes" or p["categorie"] == filtre_cat)
        and (filtre_longueur == "Toutes" or p["longueur"] == filtre_longueur)
        and (filtre_texture == "Toutes" or p["texture"] == filtre_texture)
    ]

    st.divider()

    if not produits_filtres:
        st.info("Aucune perruque ne correspond à ces filtres.")
    else:
        cols = st.columns(3)
        for i, produit in enumerate(produits_filtres):
            with cols[i % 3]:
                st.markdown('<div class="product-card">', unsafe_allow_html=True)
                st.image(produit["image"], use_container_width=True)

                badges = f'<span class="badge-cat">{produit["categorie"]}</span>'
                if produit["prix_promo"]:
                    badges += '<span class="badge-promo">PROMO</span>'
                st.markdown(badges, unsafe_allow_html=True)

                st.subheader(produit["nom"])
                st.caption(f"{produit['longueur']} · {produit['texture']}")
                st.write(produit["description"])

                if produit["prix_promo"]:
                    st.markdown(
                        f'<span class="price-tag">{produit["prix_promo"]:.2f} €</span>'
                        f'<span class="old-price">{produit["prix"]:.2f} €</span>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(f'<span class="price-tag">{produit["prix"]:.2f} €</span>', unsafe_allow_html=True)

                if st.button("Ajouter au panier", key=f"add_{produit['id']}"):
                    ajouter_au_panier(produit["id"])
                    st.toast(f"{produit['nom']} ajoutée au panier ✨")
                st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------
# PAGE PANIER / COMMANDE
# ----------------------------
elif onglet == "Mon panier":
    if not st.session_state.panier:
        st.info("Votre panier est vide. Ajoutez des perruques depuis la boutique !")
    else:
        st.subheader("Votre panier")
        for pid, qte in list(st.session_state.panier.items()):
            produit = next(p for p in PRODUITS if p["id"] == pid)
            c1, c2, c3, c4 = st.columns([3, 1, 1, 1])
            c1.write(produit["nom"])
            c2.write(f"{qte} x {prix_final(produit):.2f} €")
            if c3.button("➖", key=f"minus_{pid}"):
                retirer_du_panier(pid)
                st.rerun()
            if c4.button("➕", key=f"plus_{pid}"):
                ajouter_au_panier(pid)
                st.rerun()

        st.divider()
        st.markdown(f"### Total : {total_panier():.2f} €")

        st.divider()
        st.subheader("Finaliser la commande")
        with st.form("commande_form"):
            nom = st.text_input("Nom complet")
            email = st.text_input("Email")
            adresse = st.text_area("Adresse de livraison")
            submit = st.form_submit_button("Valider la commande")

            if submit:
                if not nom or not email or not adresse:
                    st.error("Merci de remplir tous les champs.")
                else:
                    st.success(f"Merci {nom} ! Votre commande de {total_panier():.2f} € a bien été enregistrée. "
                                f"Une confirmation sera envoyée à {email}.")
                    st.session_state.panier = {}
                    st.balloons()

# ----------------------------
# PAGE FAQ
# ----------------------------
else:
    st.subheader("Questions fréquentes")

    with st.expander("Quel est le délai de livraison ?"):
        st.write("Nos perruques sont confectionnées à la main : comptez 5 à 10 jours ouvrés avant expédition, "
                  "puis 2 à 5 jours pour la livraison.")

    with st.expander("Lace Classique ou HD, quelle différence ?"):
        st.write("La lace HD offre un effet cuir chevelu quasi invisible, plus discrète mais aussi plus coûteuse. "
                  "La lace Classique reste très naturelle à un prix plus accessible.")

    with st.expander("Puis-je retourner une perruque ?"):
        st.write("Retours acceptés sous 14 jours, pour les articles non portés et non altérés.")

st.divider()
st.caption("Ceci est une démo de test. Le paiement en ligne (Stripe) sera ajouté dans une prochaine étape.")
