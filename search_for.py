import streamlit as st

def app(my_class_room):
    st.subheader('Search for Student')

    fname = st.text_input('ENTER FIRST NAME ')
    lname = st.text_input('ENTER LAST NAME')

    if st.button('SEARCH',use_container_width=True):
        find_students = my_class_room.search_students(fname,lname)
        if find_students.empty:
            st.warning('NOT STUDENTS FOUND')

        else:
            st.dataframe(find_students)








