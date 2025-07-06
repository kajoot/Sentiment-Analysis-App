# Sentiment Analysis App

This project demonstrates a complete pipeline for multi-class sentiment analysis (Positive, Neutral, Negative) using state-of-the-art transformer models. The best-performing model is deployed via a Flask API, and a Streamlit frontend allows interactive user input.

---

## 🚀 Features

- Fine-tuned transformer models: bert-base-uncased, roberta-base,  distilbert-base-uncased, and vinai/bertweet-base

- Custom training loop with Hugging Face's Trainer

- Evaluation on accuracy, precision, recall, and F1-score

- Best model auto-saving via custom callback

- Inference API built with Flask

- UI for predictions using Streamlit

- Tested on Kaggle with GPU (T4)

---

## Project Structure
.
├── app.py # Streamlit frontend
├── api.py # Flask backend for model prediction
├── final_model/ # Directory containing saved tokenizer and model
├── requirements.txt # Required dependencies
├── README.md # Project documentation (this file)
└── fine-tuning-sota-transformers-for-multi-class-senti.ipynb # Jupyter notebook with training code

---

## 🧠 Models Trained

| Model Name   | Hugging Face ID          |
|--------------|--------------------------|
| BERT         | `bert-base-uncased`      |
| RoBERTa      | `roberta-base`           |
| DistilBERT   | `distilbert-base-uncased`|
| BERTweet     | `vinai/bertweet-base`    |

---

## Example Metrics (Sample)

| Model             | Accuracy | Macro F1 |
|-------------------|----------|----------|
| `bert-base-uncased`| 0.91     | 0.89     |
| `roberta-base`     | 0.90     | 0.88     |
| `distilbert-base`  | 0.88     | 0.86     |
| `bertweet-base`    | 0.89     | 0.87     |

> **Note:** BERT was selected as the best-performing model.

---


## 🧑‍💻 Author

**Firas Graa**  
AI Engineering Student  
🇹🇳 Tunisia