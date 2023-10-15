import streamlit as st

def app(my_class_room):
    st.title("Edit Student Data")
    student_id = st.number_input("ENTER ID TO SEARCH",1,1000)
    student = my_class_room.get_student_by_id(student_id)
    if student :
        with st.form("edit_form"):
            st.subheader(f"Edit data for student id : {student.id} ")
            fname = st.text_input("Fist Name",value=student.fname)
            lname = st.text_input("Last Name", value=student.lname)
            dateBirth = st.date_input('Birth Date', value=student.dateBirth)
            gender = st.radio('Gender', ['Male', 'Female'], index=(0 if student.gender == 'Male' else 1))
            weight = st.slider('Weight', 30, 150, value=student.weight)
            height = st.slider('Height', 130, 200, value=student.height)

            submitted = st.form_submit_button("Save Changes", use_container_width=True)
            if submitted:
                my_class_room.update_student(student_id, fname, lname, dateBirth, height, weight, gender)
                st.success('Student data updated successfully!')

    else:
        st.warning("NONE STUDENT FOUND WITH THIS ID")


