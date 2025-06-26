import streamlit as st

st.set_page_config(page_title="homepage", layout="wide")

def add_bg_image():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.unsplash.com/photo-1578604665675-9aee692f6ddc?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8YWlyJTIwcG9sbHV0aW9ufGVufDB8fDB8fHww");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_image()

# -------- Title --------
st.markdown(
    "<h1 style='text-align: center; color: #ffffff; text-shadow: 2px 2px 4px #000000;'>AQI Prediction</h1>",
    unsafe_allow_html=True
)

button_style = """
    <style>
    div.stButton > button {
        background-color: #1F618D;
        color: white;
        padding: 0.75em 1em;
        font-size: 16px;
        border-radius: 10px;
        width: 100%;
        font-weight: bold;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #154360;
    }
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)




st.markdown(button_style, unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

with col1:
    if st.button("karyavvatom"):
        st.switch_page("pages/aqi.py")

with col2:
    if st.button("Kollam"):
        st.switch_page("pages/kollamaqi.py")

with col3:
    if st.button("Eloor"):
        st.switch_page("pages/elooraqi.py")