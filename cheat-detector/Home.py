import streamlit as st

st.title('AI Project - Cheat Detector using Bayesian Nets')

st.markdown("---")

st.image("bayes-nets-ai.png", caption="Cheat Detector Bayes Nets", use_column_width=True)

st.markdown("---")


st.subheader("Introduction")
st.write("""
    In recent years, academic integrity has become a critical concern in educational 
    institutions. The rise of remote learning and online assessments has increased the 
    challenges associated with detecting cheating behaviors among students. Our proposed 
    project aims to address this issue by leveraging Bayesian networks to create a robust 
    cheating detection system.
""")

st.subheader("Motivation")
st.write("""
    The motivation behind choosing this area stems from the increasing need 
    for advanced and accurate cheating detection mechanisms. By employing Bayesian 
    networks, which are adept at handling probabilistic relationships, we aim to create a 
    more nuanced and effective solution compared to existing methods.
""")

st.subheader("Expected Results")
st.write("""
    Our project aims to provide a reliable cheating detection 
    system that considers the complex interplay of various factors. 
    The Bayesian network should yield probability distributions for the
    likelihood of cheating based on the observed variables.
""")