import re
import string
import joblib
import streamlit as st




st.set_page_config(
    page_title="Customer Review Sentiment Analysis",
    page_icon="💬",
    layout="centered"
)




MODEL_PATH = "model/sentiment_model.joblib"

try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    st.error(
        "Model file not found. "
        "Please make sure 'model/sentiment_model.joblib' exists."
    )
    st.stop()



def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"http\S+|www\.\S+", " ", text)
    text = re.sub(r"\d+", " ", text)
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )
    text = re.sub(r"\s+", " ", text).strip()

    return text




st.title("💬 Customer Review Sentiment Analysis")

st.write(
    "Enter a customer review below and the trained "
    "machine-learning model will predict its sentiment."
)


review = st.text_area(
    "Enter Customer Review:",
    placeholder="Example: The product quality is excellent and I am very happy with my purchase.",
    height=150
)




if st.button("Predict Sentiment"):

    if review.strip() == "":
        st.warning("Please enter a customer review.")

    else:
        cleaned_review = clean_text(review)

        prediction = model.predict([cleaned_review])[0]

        st.subheader("Prediction")

        if prediction == "Positive":
            st.success("😊 Positive")

        elif prediction == "Negative":
            st.error("😞 Negative")

        else:
            st.info("😐 Neutral")

        st.write("**Predicted Sentiment:**", prediction)
