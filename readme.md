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
. <br>
├── app.py # Streamlit frontend <br>
├── api.py # Flask backend for model prediction <br>
├── final_model/ # Directory containing saved tokenizer and model <br>
├── requirements.txt # Required dependencies <br>
├── README.md # Project documentation (this file) <br>
├── fine-tuning-sota-transformers-for-multi-class-senti.ipynb # Jupyter notebook with training code <br>

## 🧠 Models Trained

| Model Name   | Hugging Face ID          |
|--------------|--------------------------|
| BERT         | `bert-base-uncased`      |
| RoBERTa      | `roberta-base`           |
| DistilBERT   | `distilbert-base-uncased`|
| BERTweet     | `vinai/bertweet-base`    |

---

## Example Metrics 

| Model                | Accuracy  | Macro Precision | Macro Recall | Macro F1  | Eval Loss |
|----------------------|-----------|-----------------|--------------|-----------|-----------|
| `bert-base-uncased`  | 0.8721    | 0.8657          | 0.8658       | 0.8656    | 0.3617    |
| `vinai/bertweet-base`| 0.8703    | 0.8637          | 0.8646       | 0.8640    | 0.3683    |
| `distilbert-base-uncased` | 0.8634 | 0.8569          | 0.8570       | 0.8568    | 0.3835    |
| `roberta-base`       | 0.8625    | 0.8550          | 0.8559       | 0.8553    | 0.3921    |

> **Note:** BERT was selected as the best-performing model.

---


## 🧑‍💻 Author

**Firas Graa**  
AI Engineering Student  
🇹🇳 Tunisia
