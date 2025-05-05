import streamlit as st
import base64

st.set_page_config(
    page_title="CivDexAI",
    page_icon="🚀",
    layout="wide"
)
def set_background(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:/image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function with your file path
set_background("https://raw.githubusercontent.com/glenvj-j/CivDexAI-Predicting-Team-Rocket/refs/heads/main/Streamlit/image/bg.png")

# with st.sidebar:
#     st.text('Main Menu')


left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("image/Headline.png")

st.markdown("<h1 style='text-align: center; color: white;'>Welcome!</h1>", unsafe_allow_html=True)
st.markdown("""
    <style>
        .centered-text {
            text-align: center;
            color: white;
        }
    </style>
    <div class="centered-text">
        CivDexAI is a program that will help you find the Team Rocket lurking in Kanto Region, <p>
            Let's help the Global Police to find the Team Rocket!
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="info-box" style='text-align: center; color: white;'>
        <p><b>👈 Start the program from the left sidebar</b></p>
    </div>
""", unsafe_allow_html=True)


# Custom CSS for full card styling
st.markdown("""
    <style>
    .info-box {
        background-color: #ffffff;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        height: 100%;
        color: black;  /* This will set the font color to black for all text in the info-box */
    }
    .info-box h4 {
        margin-top: 0;
        font-size: 20px;
        color: black;  /* Ensure h4 text is black */
    }
    .info-box hr {
        margin: 10px 0;
        border: none;
        border-top: 1px solid #ccc;
    }
    .info-box p {
        margin-bottom: 0;
        font-size: 16px;
        color: black;  /* Ensure p text is black */
    }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="info-box">
            <h4>🕵🏻‍♂️ Help the Detective!</h4>
            <hr>
            <p>Team Rocket is infiltrated Kanto, use this tool and predict which citizen is secretly Team Rocket!</p>
        </div>
    """, unsafe_allow_html=True)


with col2:
    st.markdown("""
    <div class="info-box">
        <h4>🛠️ Powered by Decision Tree</h4>
        <hr>
        <p>This tool is trained from 4,000 data from Kaggle. <p>
        <a href="https://www.kaggle.com/datasets/kotsop/pokmon-detective-challenge/data" target="_blank">Click here</a> for more details.</p>
    </div>
""", unsafe_allow_html=True)


with col3:
    st.markdown("""
        <div class="info-box">
            <h4>🧠 Test your skill!</h4>
            <hr>
            <p>Examine the data, make your guess—Team Rocket or not—and see if the machine agrees. Can you outsmart the model?</p>
        </div>
    """, unsafe_allow_html=True)

