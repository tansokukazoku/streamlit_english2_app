import streamlit as st
from PIL import Image

st.title('さほのえいご学習')
st.subheader(":blue[さあ、今日もがんばりましょう]")

img = Image.open('./data/english_pic.jpg')
st.image(img,width=900)

st.markdown("""
            ### ファイト！ ## ファイト！！ # ファイト！！！
            """)
