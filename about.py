import streamlit as st
from PIL import Image
def app(my_class_room):
    st.subheader('Info is a website created for users to take info about a classroom')

    st.text('A classroom, schoolroom or lecture room is a learning space in which both children \nand adults learn. Classrooms are found in educational institutions\n of all kinds, ranging from preschools to universities, and may \nalso be found in other places where education or \ntraining is provided, such as\n corporations and religious and humanitarian organizations. \nThe classroom provides a space where learning can take place \nuninterrupted by outside distractions.')


    img = Image.open('pc2.jpg')
    st.image(img,width=700)
    st.video('https://www.youtube.com/watch?v=pgk-719mTxM')













