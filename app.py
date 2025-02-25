
import streamlit as st

# Set page config
st.set_page_config(page_title="Growth Mindset Project", page_icon="🌙")

# Title and description
st.title("Growth Mindset AI Project: Web App With Streamlit")
st.header("🚀 Welcome to Your Growth Journey!")
st.write("A growth mindset is the belief that abilities can be developed through dedication and hard work. It encourages embracing challenges, learning from mistakes, and viewing effort as a path to success and improvement ★.")

# Growth Mindset Quote
st.header("💡 Growth Mindset Quote")
st.write("'Failure is not the opposite of success; it’s part of success.' — Arianna Huffington")

# User input for challenge
st.header("💪 What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

# Condition to display challenge message
if user_input:
    st.success(f"💪 You are facing: {user_input}. Keep pushing, because every step forward, no matter how small, brings you closer to your goal.")
else:
    st.warning("Tell me about your Challenge to get started!")

# Reflecting on learning
st.header("Reflect on Your Learning")
reflection = st.text_area("Write your outcome here")

if reflection:
    st.success(f"🌟 Great Insight! Your reflection: {reflection} 🌟")
else:
    st.info("Reflection on past experiences helps you grow! Share your difficulties or insights.")

# Celebrating achievements
st.header("Celebrate Your Wins!")
achievement = st.text_input("Share something you have recently accomplished:")

if achievement:
    st.success(f"🎉 Amazing! You achieved: {achievement}")
else:
    st.info("Big achievements count! Share one now! 🌟")

# Footer
st.write("___")
st.write("Success is the sum of small efforts, repeated day in and day out.")
st.write("😇⭐⭐⭐ Created By Syeda Naila ⭐⭐⭐")
