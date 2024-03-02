import streamlit as st
import pandas as pd

# Initial page config
title = "GradMove"
st.title(title + " 🎓")
st.write("by Areej, Shreya, Vibha, Mihika")

# Page Configuration
st.set_page_config(
    page_title="GradMove 🎓",
    page_icon="imgs/avatar_streamly.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com/amirani18/GradMove",
        "Report a bug": "https://github.com/amirani18/GradMove",
        "About": """
            ## GradMove
            
            **GitHub**: https://github.com/amirani18/GradMove
            
            Recent college graduates often land their dream job with no idea of how to find housing at their new location. 
            Introducing: GradMove! 
            Your go-to app for finding housing near your dream job, curated based on tastes in housing, price, transport, and access to healthcare.  

        """
    }
)

# user inputs on sidebar
st.sidebar.title("vibes 💖")
S = st.sidebar.slider('How Excited Are You to Be Here?', value = 1, 
                      min_value = 10, max_value = 100)
st.sidebar.write("Excitement Level", S)

# # main body
st.header("Are you a fresh grad who's landed your dream job in a brand new city?")
st.subheader("Introducing: GradMove!")
st.markdown("Your go-to app for finding housing near your dream job, curated based on tastes in housing, price, transport, and access to healthcare.")

# selectbox for cities
df = pd.DataFrame({
    'cities': ["San Francisco", "Chicago", "New York", "Seattle", "Cambridge", "Amsterdam" ],
})

option = st.selectbox(
    'Which city do you plan to move to?',
    df['cities']
)

'You selected: ', option



