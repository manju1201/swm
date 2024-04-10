# Sentiment Analysis

## Overview
This project aims to perform sentiment analysis on text data, utilizing various preprocessing techniques and state-of-the-art algorithms. The Sentiment 140 dataset from Twitter and the SemEval-2014 dataset were employed for this purpose.

## Data Preprocessing
The following preprocessing steps were applied to the dataset:
- Removal of HTML tags
- Removal of URLs
- Lowercasing
- Removal of whitespace
- Removal of local chat words

## Algorithms Used
We experimented with several algorithms for sentiment analysis:
1. Hugging Face BERTweet
2. Deep Neural Network (DNN)
3. Support Vector Machine (SVM)

## Evaluation Metrics
We evaluated the performance of each algorithm using the following metrics:
- Accuracy
- Precision
- Recall
- F1 Score

## Results
### Logistic Regression:
- Accuracy: 0.62
- Precision: 0.62
- Recall: 0.62
- F1 Score: 0.62

### Support Vector Machine (SVM):
- Accuracy: 0.65
- Precision: 0.64
- Recall: 0.64
- F1 Score: 0.64

### Random Forest:
- Accuracy: 0.65
- Precision: 0.64
- Recall: 0.64
- F1 Score: 0.64

### Deep Neural Network (DNN):
- Accuracy: 0.72
- Precision: 0.70
- Recall: 0.70
- F1 Score: 0.70

### RoBERTa:
- Accuracy: 0.69
- Precision: 0.69
- Recall: 0.69
- F1 Score: 0.69

### BERTweet:
- Accuracy: 0.73
- Precision: 0.70
- Recall: 0.71
- F1 Score: 0.72

## User Interface (UI)
The project includes a user interface where users can input text data, such as tweets or sentiment-based sentences. After inputting the text, users can click on the "Analyze Sentiment" button. The UI then displays the sentiment analysis result:
- Positive sentiment (POS)
- Negative sentiment (NEG)
- Neutral sentiment (NEU)
