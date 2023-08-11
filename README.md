# NEWS Classifier
 Classify news into Categories
 
# News Category Classification using Streamlit

This is a simple Streamlit web application that uses a trained model to predict the category of news articles based on user-provided headlines and descriptions.

## Prerequisites

Before running the application, ensure you have the following dependencies installed:

```bash
pip install tensorflow streamlit numpy
```
Getting Started

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/news-category-classification.git
```
Place the trained model (the_model.h5), label encoder (encoder_kaggle.pkl), and tokenizer (tokenizer_kaggle.pkl) files in the same directory as the app.py script.
# Installation

Before running the code, you'll need to make sure you have the required libraries installed. You can install them using the following commands:

```bash
pip install pandas numpy matplotlib seaborn wordcloud nltk keras tensorflow
```
Additionally, some libraries require additional data to be downloaded. Run the following commands to download the required data:

```bash
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
```
These commands will download the NLTK's stopwords and WordNet data, which are necessary for text preprocessing.

Please ensure that you have the necessary dependencies installed before running the code.

After installing the required python modules run the textclassification file
```bash
python textclassification.ipynb
```
After running this file we will get the following files
```bash
the_model.h5
the-weight.h5
encoder_kaggle.pkl
tokenizer_kaggle.pkl
```

After that run the Streamlit app:

```bash
streamlit run app.py
```
This will launch a local development server and open the app in your default web browser.

# How to Use

1. Once the app is running, you will see the input fields for the headline and description of a news article.

2. Enter the headline and description of the news article you want to classify.

3. Click the "Predict" button to see the predicted category for the provided news article.

# Custom Styling
The app features custom CSS styles for the button. If you'd like to modify the styles, you can do so in the app.py file, where the CSS styles are defined in the markdown function.
