# 💬 Customer Review Sentiment Analysis

Welcome to the Customer Review Sentiment Analysis repository! This project is an end-to-end Machine Learning and Natural Language Processing (NLP) application built to decode customer feedback and predict sentiments in real time.

---

## ✨ About the Project
Customer feedback holds the key to product improvement and user satisfaction, but sifting through thousands of reviews manually is a challenge. This project automates that process by taking raw customer reviews, cleaning the text, exploring underlying patterns, and deploying an interactive web app where you can test live predictions instantly.

---

## 🛠️ What's Inside & Workflow
* **Data Cleansing & Normalization**: Standardized text data by converting it to lowercase, and stripping HTML tags, URLs, and punctuation[cite: 1].
* **Exploratory Data Analysis (EDA)**: Analyzed review length distributions, word counts, and sentiment class balance across positive, neutral, and negative categories[cite: 1].
* **TF-IDF Feature Extraction**: Converted unstructured review text into meaningful numerical feature matrices using unigrams and bigrams (`ngram_range=(1, 2)`).
* **Machine Learning Models**: Trained and evaluated models like **Logistic Regression**, **Multinomial Naive Bayes**, and **LinearSVC** to achieve strong classification performance.
* **Streamlit Web Application**: Brought the model to life with an interactive, user-friendly UI (`app.py`) for real-time inference.

---

## 🧰 Tech Stack
* **Programming Language**: Python[cite: 1]
* **Data Handling**: Pandas, NumPy[cite: 1]
* **Machine Learning**: Scikit-learn[cite: 1]
* **Visualization**: Seaborn, Matplotlib
* **Web Interface**: Streamlit[cite: 1]

---

## 📂 Project Structure
```text
├── Group-6 NLP sentiment analysis.ipynb # Jupyter notebook detailing EDA and model training
├── app.py                              # Streamlit web application script
├── sentiment_model.joblib              # Saved machine learning model
├── P652-Dataset.xlsx                   # Customer review dataset
└── README.md                           # Project documentation
