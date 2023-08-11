import re
import streamlit as st
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import streamlit.components.v1 as components

# Load the trained model
model = tf.keras.models.load_model('the_model.h5')

# Load the label encoder and tokenizer
encoder = pickle.load(open('encoder_kaggle.pkl', 'rb'))
tokenizer = pickle.load(open('tokenizer_kaggle.pkl', 'rb'))

# Function to preprocess text input
def preprocess_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    words = text.split()
    preprocessed_text = ' '.join(words)
    return preprocessed_text

# Function to predict the category
def predict_category(text):
    preprocessed_text = preprocess_text(text)
    sequence = tokenizer.texts_to_sequences([preprocessed_text])
    padded_sequence = pad_sequences(sequence, maxlen=130)
    predicted_probs = model.predict(padded_sequence)[0]
    predicted_label = encoder.inverse_transform([np.argmax(predicted_probs)])
    return predicted_label[0]

# Streamlit app
def main():
    # Set page configuration
    st.set_page_config(
        page_title="News Category Classification",
        page_icon=":newspaper:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Custom CSS styles
    st.markdown(
        """
        <style>
        .stButton > button {
            background-color: #F63366;
            color: white;
            font-weight: bold;
            padding: 0.7rem 2rem;
            border-radius: 0.4rem;
            transition: background-color 0.3s;
        }
        .stButton > button:hover {
            background-color: #DB3066;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Page layout
    st.title("News Category Classification")
    st.write("Enter a news headline and description below:")

    # User input
    headline = st.text_input("Headline:")
    description = st.text_input("Description:")

    # Predict category
    if st.button("Predict"):
        with st.spinner("Predicting..."):
            text = headline + " " + description
            category = predict_category(text)
            st.success("Predicted Category:")
            st.markdown(f"<h2 style='color: #F63366;'>{category}</h2>", unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.write("Made with :heart: by Dhanush Devadiga")

if __name__ == '__main__':
    main()
