from pathlib import Path
import importlib
import streamlit as st
import joblib
import pandas as pd

def main():
    html_temp = """<h1>Email Spam Prediction</h1>"""
    model = joblib.load("email_spam_linear_model.joblib")
    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown("This website helps you predict whether an email is spam or not.")

    p1 = st.number_input("Email Length", min_value=0.0, value=100.0, step=1.0)
    p2 = st.number_input("Number of Links", min_value=0.0, value=1.0, step=1.0)
    p3 = st.number_input("Number of Special Characters", min_value=0.0, value=3.0, step=1.0)
    p4 = st.number_input("Capital Words", min_value=0.0, value=5.0, step=1.0)
    p5 = st.selectbox("Has Attachment", [0, 1])

    data_new = pd.DataFrame(
        {
            "Email_Length": p1,
            "Num_Links": p2,
            "Num_Special_Chars": p3,
            "Capital_Words": p4,
            "Has_Attachment": p5,
        },
        index=[0],
    )

    if st.button("Predict"):
        pred = model.predict(data_new)
        score = float(pred[0])
        if score >= 0.5:
            st.success(f"Spam email. Score: {score:.3f}")
        else:
            st.info(f"Not spam. Score: {score:.3f}")


if __name__ == '__main__':
    main()
