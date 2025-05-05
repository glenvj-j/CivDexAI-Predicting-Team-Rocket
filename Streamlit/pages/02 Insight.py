import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="CivDexAI",
    page_icon="🚀",
    layout="wide"
)

st.markdown('<h1 style="text-align: center; color: white;">📊 Dashboard</h1>', unsafe_allow_html=True)

st.markdown('<div style="text-align: center; color: white;">To help you predict Team Rocket, you can see the dashboard by clicking the link below</div>', unsafe_allow_html=True)
st.markdown('')

image = Image.open("Streamlit/image/Dashboard.png")
st.image(image, use_column_width=True)
st.markdown(""" <div style="text-align: center; color: white;">
    <a href="https://public.tableau.com/app/profile/glen.joy2546/viz/CivDexAIPredictionTools/Dashboard?publish=yes" target="_blank">
        <button class="dashboard-button">🔗 Open Dashboard</button>
    </a>
""", unsafe_allow_html=True)
