import utils
import streamlit as st
import time
import pandas as pd

st.title('Predicting Cheating Probability')

data = utils.read_data_from_json('input.json')

if ('grade' and 'difficulty' and 'cgpa' and 'attendance') in st.session_state:
    grade = st.session_state['grade']
    difficulty = st.session_state['difficulty']
    cgpa = st.session_state['cgpa']
    attendance = st.session_state['attendance']

    r_attendance = utils.range_attendance(attendance)
    r_cgpa = utils.range_cgpa(cgpa)
    r_grade = utils.range_grade(grade)

    pov = data['pov | cgpa, attendance'][f'({r_cgpa[0]}-{r_cgpa[1]}, {r_attendance[0]}-{r_attendance[1]})']
    hw = data['homework | hw_grade, hw_difficulty'][f'({r_grade[0]}-{r_grade[1]}, {difficulty})']
    cheat = data['cheat | pov, homework'][f'({list(pov.keys())[0]}, {list(hw.keys())[0]})']

    predict_btn = st.button("Predict")

    if predict_btn:
        progress_text = "Prediction in progress ..."
        my_bar = st.sidebar.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        my_bar.empty()
        result = utils.cheat_probability(cheat, hw, pov)

        df = pd.DataFrame({"Type": ["Homework Status", "Professor's Impression", "Cheating Likelihood"],
                           "Impression": [result['hw'][0], result['pov'][0], result['cheat'][0]],
                           "Probability": [result['hw'][1], result['pov'][1], result['cheat'][1]]})
        st.write(df)
        st.markdown("---")

        st.success("Cheating Probability: " + result["output"], icon="✅")
else:
    st.error("Data is not submitted in the Input page", icon='🚨')