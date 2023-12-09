import streamlit as st

if 'grade' not in st.session_state:
    st.session_state.grade = -1
if 'difficulty' not in st.session_state:
    st.session_state.difficulty = '--'
if 'cgpa' not in st.session_state:
    st.session_state.cgpa = -1
if 'attendance' not in st.session_state:
    st.session_state.attendance = -1

st.title('Adding Input Values')

hw_grade = float(st.text_input('HW Grade', st.session_state.grade))
hw_difficulty = st.selectbox('HW Difficulty', ('--', 'Easy', 'Medium', 'Hard'), index=0 if st.session_state.difficulty == '--' else None)
cgpa = float(st.text_input('CGPA', st.session_state.cgpa))
attendance = float(st.text_input('Attendance', st.session_state.attendance))

submit_btn = st.button("Submit")

if submit_btn:
    if hw_grade != -1 and hw_difficulty != '--' and cgpa != -1 and attendance != -1:
        st.session_state.grade = hw_grade
        st.session_state.difficulty = str.lower(hw_difficulty)
        st.session_state.cgpa = cgpa
        st.session_state.attendance = attendance

        st.info("Data uploaded successfully", icon='ℹ️')
    else:
        st.error("Please insert all data", icon='🚨')
