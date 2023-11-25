import streamlit as st

def app(my_class_room):
    st.title(" Update Grades")
    updated = False
    student_id = st.number_input('Enter Student ID',min_value=1,value=1,placeholder="Enter to apply or press Search button")
    student = my_class_room.get_student_by_id(student_id)

    if st.button('Search'):
        student = my_class_room.get_student_by_id(student_id)

    if student:
        st.write(f"Found:{student.fname}{student.lname}")
        updated = upgrade_values(student)

    else:
        st.write("Students not found")

    if updated:
        st.success("Grades updated sucessfully!")

def upgrade_values(student):
    updated = False
    with st.form(key="grades_form"):
        courses = student.courses
        math_grade = st.number_input("Grade for Math",min_value=-1,max_value=20,value=courses['Math'])
        history_grade = st.number_input("Grade for history",min_value=-1,max_value=20,value=courses['History'])
        physics_grade = st.number_input("Grade for Physics",min_value=-1,max_value=20,value=courses['Physics'])
        english_grade = st.number_input("Grade for English",min_value=-1,max_value=20,value=courses['English'])
        biology_grade = st.number_input("Grade for Biology", min_value=-1, max_value=20, value=courses['Biology'])


        submited = st.form_submit_button("Update Grades")

    if submited:
        student.add_grade('Math',math_grade)
        student.add_grade('History', history_grade)
        student.add_grade('Physics', physics_grade)
        student.add_grade('English', english_grade)
        student.add_grade('Biology', biology_grade)

        updated = True
    return updated


