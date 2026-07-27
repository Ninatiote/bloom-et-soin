import streamlit as st

# ----------------------------
# CONFIGURATION DE LA PAGE
# ----------------------------
st.set_page_config(
    page_title="Bloom & Soin",
    page_icon="🌹",
    layout="wide",
)

# ----------------------------
# STYLE (ambiance "romance sombre" beauté/bien-être)
# ----------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #14100f;
        color: #f2e9e4;
    }
    h1, h2, h3 {
        font-family: 'Georgia', serif;
        color: #d4af37;
    }
    .product-card {
        background-color: #1f1a18;
        border: 1px solid #3a2e2c;
        border-radius: 10px;
        padding: 18px;
        margin-bottom: 20px;
    }
    .price-tag {
        color: #d4af37;
        font-size: 20px;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #6b1f2a;
        color: #f2e9e4;
        border-radius: 6px;
        border: none;
        padding: 8px 20px;
    }
    .stButton>button:hover {
        background-color: #8a2836;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------
# CATALOGUE DE PRODUITS (exemple)
# ----------------------------
PRODUITS = [
    {
        "id": 1,
        "nom": "Sérum Visage Éclat de Rose",
        "prix": 34.90,
        "description": "Sérum concentré à l'huile de rose musquée, pour une peau lumineuse et repulpée.",
        "image": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400",
    },
    {
        "id": 2,
        "nom": "Baume Lèvres Velours",
        "prix": 12.50,
        "description": "Baume nourrissant au beurre de karité, texture fondante, parfum vanille ambrée.",
        "image": "https://images.unsplash.com/photo-1571781926291-c477ebfd024b?w=400",
    },
    {
        "id": 3,
        "nom": "Huile Corps Nuit Étoilée",
        "prix": 28.00,
        "description": "Huile sèche nourrissante à l'amande douce, absorption rapide, parfum boisé.",
        "image": "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=400",
    },
    {
        "id": 4,
        "nom": "Masque Argile Rouge",
        "prix": 19.90,
        "description": "Masque purifiant à l'argile rouge, resserre les pores et unifie le teint.",
        "image": "https://images.unsplash.com/photo-1570194065650-d99fb4bedf0a?w=400",
    },
    {
        "id": 5,
        "nom": "Bougie Bien-Être Ambre & Cèdre",
        "prix": 24.00,
        "description": "Bougie cire de soja, notes d'ambre et de cèdre, pour un rituel cocooning.",
        "image": "https://images.unsplash.com/photo-1602523961358-f7644823d59f?w=400",
    },
]

# ----------------------------
# ÉTAT DU PANIER
# ----------------------------
if "panier" not in st.session_state:
    st.session_state.panier = {}

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
        total += produit["prix"] * qte
    return total

# ----------------------------
# EN-TÊTE
# ----------------------------
st.title("🌹 Bloom & Soin")
st.markdown("*Rituels de beauté et de bien-être, faits pour vous.*")
st.divider()

# ----------------------------
# NAVIGATION
# ----------------------------
onglet = st.radio("Navigation", ["Boutique", "Mon panier"], horizontal=True, label_visibility="collapsed")

# ----------------------------
# PAGE BOUTIQUE
# ----------------------------
if onglet == "Boutique":
    cols = st.columns(3)
    for i, produit in enumerate(PRODUITS):
        with cols[i % 3]:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            st.image(produit["image"], use_container_width=True)
            st.subheader(produit["nom"])
            st.write(produit["description"])
            st.markdown(f'<span class="price-tag">{produit["prix"]:.2f} €</span>', unsafe_allow_html=True)
            if st.button("Ajouter au panier", key=f"add_{produit['id']}"):
                ajouter_au_panier(produit["id"])
                st.toast(f"{produit['nom']} ajouté au panier ✨")
            st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------
# PAGE PANIER / COMMANDE
# ----------------------------
else:
    if not st.session_state.panier:
        st.info("Votre panier est vide. Ajoutez des produits depuis la boutique !")
    else:
        st.subheader("Votre panier")
        for pid, qte in list(st.session_state.panier.items()):
            produit = next(p for p in PRODUITS if p["id"] == pid)
            c1, c2, c3, c4 = st.columns([3, 1, 1, 1])
            c1.write(produit["nom"])
            c2.write(f"{qte} x {produit['prix']:.2f} €")
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

st.divider()
st.caption("Ceci est une démo. Le paiement en ligne (Stripe, etc.) peut être ajouté par la suite.")
