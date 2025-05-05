import pandas as pd
import random
import pickle
import streamlit as st
import requests
from bs4 import BeautifulSoup
import base64


st.set_page_config(
    page_title="CivDexAI",
    page_icon="🚀",
    layout="wide"
)

# Load model
filename = 'Streamlit/data/Prediction_Model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Load and balance the dataset
df = pd.read_csv('Streamlit/data/dataset_game.csv')
n_samples_per_class = 50
team_rocket_df = df[df['Team Rocket'] == True]
civilian_df = df[df['Team Rocket'] == False]

sampled_team_rocket = team_rocket_df.sample(n=n_samples_per_class, random_state=42)
sampled_civilian = civilian_df.sample(n=n_samples_per_class, random_state=42)

balanced_df = pd.concat([sampled_team_rocket, sampled_civilian]).sample(frac=1, random_state=42).reset_index(drop=True)

# Initialize session state
if 'index' not in st.session_state:
    st.session_state.index = random.randint(0, balanced_df.shape[0] - 1)
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'total' not in st.session_state:
    st.session_state.total = 0
if 'player_guess' not in st.session_state:
    st.session_state.player_guess = None
if 'prediction' not in st.session_state:
    st.session_state.prediction = None
if 'proba_score' not in st.session_state:
    st.session_state.proba_score = None
if 'show_result' not in st.session_state:
    st.session_state.show_result = False

st.subheader(f"🕵️ Team Rocket Detector Game, Round {st.session_state.total+1}")

# Show current data row
current_data = balanced_df.drop(columns=['Team Rocket','Name']).iloc[[st.session_state.index]]

# Get model prediction
X_test = balanced_df.drop(columns=['Team Rocket'])
prediction = loaded_model.predict(X_test.iloc[[st.session_state.index]])
proba = loaded_model.predict_proba(X_test.iloc[[st.session_state.index]])
predicted_class = "Team Rocket" if prediction[0] else "Civilian"
proba_score = round(max(proba[0]) * 100, 2)

# Custom CSS to style the layout
st.markdown("""
    <style>
        .card {
            width: 600px;
            background: linear-gradient(to bottom, #c5f1a4, #ffffff);
            border: 4px solid #8bcf64;
            border-radius: 10px;
            padding: 20px;
            font-family: 'Courier New', monospace;
        }
            
        .card2 {
            width: 600px;
            background: linear-gradient(to bottom, #696FD7, #898FF7);
            border: 4px solid #696FD7;
            border-radius: 10px;
            padding: 10px;
            font-family: 'Courier New', monospace;
        }
        .rowcard2 {
            display: flex;
            justify-content: space-between;
            padding: 5px 0;
            color:white

        }
         .rowdata2 {
        display: flex;
        gap: 40px; /* Adjust spacing between columns */
        color: white;
        margin-bottom: 10px;
    }

        .column {
        width: 250px; /* Fixed width for each column */
    }
            
        .header {
            background: #a0e388;
            color: black;
            padding: 5px;
            border-radius: 5px;
            font-weight: bold;
            font-size: 20px;
            text-align: center;
        }
        .row {
            display: flex;
            justify-content: space-between;
            padding: 5px 0;
            color:black

        }
        .rowdata {
            display: flex;
            justify-content: flex-start;
            gap: 40px; /* or any spacing you want */
            color:black
        }
            

        .badges {
            display: grid;
            grid-template-columns: repeat(8, 1fr);
            gap: 5px;
            margin-top: 20px;
        }
        .badge {
            width: 50px;
            height: 50px;
            border: 2px solid #8bcf64;
            border-radius: 5px;
            background-color: #dafad7;
            display: flex;
            align-items: center;
            justify-content: center;
            color : #dafad7
        }
        .badge-img {
            width: 30px;
            height: 30px;
        }
        .trainer-img {
            width: 125px;
            float: right;
            margin-top: -190px;
            margin-right: 100px;
        }
    </style>
""", unsafe_allow_html=True)




def image_person() :
    url = "https://play.pokemonshowdown.com/sprites/trainers/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    url3 = "https://play.pokemonshowdown.com/sprites/trainers/"

    page = requests.get(url3) #untuk download hmtl

    soup = BeautifulSoup(page.text,'html.parser')
    #merapihkan hasil download html menjadi sesuai div nya, format nya jadi bs4.BeautifulSoup bukan str
    type(soup)

    list_name = [x['src'] for x in soup.findAll('img')][1:]
    random.randint(0,len(list_name))
    choosen = list_name[random.randint(0,len(list_name))]
    link = f"https://play.pokemonshowdown.com/sprites/trainers/{choosen}"
    return link

player_badge_count = balanced_df['Number of Gym Badges'].iloc[st.session_state.index]
num_badges = min(player_badge_count, 8)  # cap at 8 badges

link_badge = [
    'https://archives.bulbagarden.net/media/upload/thumb/d/dd/Boulder_Badge.png/1200px-Boulder_Badge.png',
    'https://archives.bulbagarden.net/media/upload/9/9c/Cascade_Badge.png',
    'https://archives.bulbagarden.net/media/upload/a/a6/Thunder_Badge.png',
    'https://archives.bulbagarden.net/media/upload/b/b5/Rainbow_Badge.png',
    'https://archives.bulbagarden.net/media/upload/7/7d/Soul_Badge.png',
    'https://archives.bulbagarden.net/media/upload/6/6b/Marsh_Badge.png',
    'https://archives.bulbagarden.net/media/upload/1/12/Volcano_Badge.png',
    'https://archives.bulbagarden.net/media/upload/7/78/Earth_Badge.png'
]

badges_html = ''.join([
    f'<div class="badge"><img src="{link_badge[i]}" class="badge-img" /></div>'
    if i < num_badges else f'<div class="badge">{i + 1}</div>'
    for i in range(8)
])


# HTML Layout
st.markdown(f"""
    <div class="card">
        <div class="header">{balanced_df['Name'].iloc[st.session_state.index]}</div>
        <div class="row"><span><strong>Age</strong> {balanced_df['Age'].iloc[st.session_state.index]}</span> <span><strong>N°ID</strong> {st.session_state.index}</span></div>
        <div class="rowdata"><span><strong>City</strong> {balanced_df['City'].iloc[st.session_state.index]}</span></div>
        <div class="row"><span><strong>Profession</strong> {balanced_df['Profession'].iloc[st.session_state.index]}</span></div>
        <div class="rowdata"><span><strong>Avg. Level</strong> {balanced_df['Average Pokemon Level'].iloc[st.session_state.index]}</span>
        <span><strong>Win Ratio</strong> {balanced_df['Win Ratio'].iloc[st.session_state.index]}</span> </div>
        <div class="badges">
            {badges_html}
        </div>
        <img src="{image_person()}" class="trainer-img" />
    </div>
    <p>
""", unsafe_allow_html=True)

# charity participation, rare item holder, pokebal usage
if {balanced_df['Criminal Record'].iloc[st.session_state.index]} == 1:
    criminal = '✅'
else :
    criminal = '❌'

if {balanced_df['Charity Participation'].iloc[st.session_state.index]} == 1:
    charity = '✅'
else :
    charity = '❌'

if {balanced_df['Rare Item Holder'].iloc[st.session_state.index]} == 1:
    rare = '✅'
else :
    rare = '❌'


st.markdown(f"""
    <div class="card2">
        <div class="rowdata2">
            <div class="column"><strong>Most Used Type</strong> {balanced_df['Most Used Pokemon Type'].iloc[st.session_state.index]}</div>
            <div class="column"><strong>Battle Strategy</strong> {balanced_df['Battle Strategy'].iloc[st.session_state.index]}</div>
        </div>
        <div class="rowdata2">
            <div class="column"><strong>Criminal Record</strong> {criminal}</div>
            <div class="column"><strong>Charity Participation</strong> {charity}</div>
        </div>
        <div class="rowdata2">
            <div class="column"><strong>Debt to Kanto</strong> {balanced_df['Debt to Kanto'].iloc[st.session_state.index]:,.0f}</div>
            <div class="column"><strong>Economic Status</strong> {balanced_df['Economic Status'].iloc[st.session_state.index]}</div>
        </div>
        <div class="rowdata2">
            <div class="column"><strong>Pokeball Usage</strong> {balanced_df['PokéBall Usage'].iloc[st.session_state.index]}</div>
            <div class="column"><strong>Rare Item Holder</strong> {rare}</div>
        </div>
    </div>
""", unsafe_allow_html=True)

######################

st.markdown('<br>', unsafe_allow_html=True)

###################

# Button handler
def handle_guess(guess):
    st.session_state.player_guess = guess
    st.session_state.prediction = predicted_class
    st.session_state.proba_score = proba_score
    st.session_state.show_result = True
    st.session_state.total += 1
    if (guess == "Team Rocket" and prediction[0]) or (guess == "Civilian" and not prediction[0]):
        st.session_state.score += 1
    # Update to a new random index
    st.session_state.index = random.randint(0, balanced_df.shape[0] - 1)
st.subheader('is this person Team Rocket?')

# Buttons
col1, col2 = st.columns(2)


# Handle the "Team Rocket" guess
with col1:
    # Team Rocket button
    if st.button("🚀 Team Rocket", key="team_rocket"):
        handle_guess("Team Rocket")  # Call your function when clicked

# Handle the "Civilian" guess
with col2:
    # Civilian button
    if st.button("👤 Civilian", key="civilian"):
        handle_guess("Civilian")  # Call your function when clicked


if st.session_state.show_result:
    st.markdown("### 🧠 Game Result", unsafe_allow_html=True)
    
    # Layout the result in columns for better spacing
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown(f"**Your Guess:** {st.session_state.player_guess}")
        st.markdown(f"**Machine Prediction:** {st.session_state.prediction} ({st.session_state.proba_score}%)")

    with col2:
        if st.session_state.player_guess == st.session_state.prediction:
            st.success("✅ You are Right! You beat the Machine!")
        else:
            st.error("Your prediction was different from the Machine.", icon="❌")
    
    st.session_state.show_result = False  # Hide after one round


# Score display
if st.session_state.total > 0:
    rate = round(st.session_state.score / st.session_state.total * 100)
else:
    rate = 0  # If no games played, set rate to 0%

st.sidebar.markdown(f"### 🎯 Score: {st.session_state.score} / {st.session_state.total}")
st.sidebar.markdown(f"Rate: {rate} %")

st.sidebar.warning('The game results shown are from the previous round.\n\nEach time you make a selection, a new character will be randomly generated.')

