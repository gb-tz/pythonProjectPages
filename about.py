import streamlit as st
from PIL import Image
def app():
    st.subheader('About is a website created for users to take info about a classroom')
    with st.expander("Information"):
        st.text('A classroom, schoolroom or lecture room is a learning space in which both children \nand adults learn. Classrooms are found in educational institutions\n of all kinds, ranging from preschools to universities, and may \nalso be found in other places where education or \ntraining is provided, such as\n corporations and religious and humanitarian organizations. \nThe classroom provides a space where learning can take place \nuninterrupted by outside distractions.')


    col1, col2, col3 = st.columns(3)
    with col1 :
        st.image("Images/stu1.jpg",caption="Playing",use_column_width=True)

    with col2 :
        st.image("Images/stu2.jpg",caption="Reading",use_column_width=True)

    with col3 :
        st.image("Images/stu3.jpg",caption="Outside",use_column_width=True)

    with st.expander("See Philosophy:"):
        st.write(
            "The philosophy of Greenwood is deeply rooted in the belief that education should extend beyond academic excellence to include the development of character, creativity, and curiosity in every child. The school aims to foster an environment where students are encouraged to explore, inquire, and innovate, enabling them to become lifelong learners and contributors to a global society.")


    img = Image.open('pc2.jpg')
    st.image(img,use_column_width=True)

    st.video('https://www.youtube.com/watch?v=pgk-719mTxM')













