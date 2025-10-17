import streamlit as st

# Title
st.set_page_config(page_title="Image Color Filter App", layout="centered")
st.title("🎨 Image Color Filter App")

# Read your HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Display it inside Streamlit
st.components.v1.html(html_code, height=800, scrolling=True)
