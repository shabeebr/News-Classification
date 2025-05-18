# News-Classification
![image](https://github.com/user-attachments/assets/55c6bb3c-2213-43fa-bd8a-7ad2122278f8)
# News Category Classification

This project implements a text classification model to categorize news articles into different categories using the **News Category Dataset** by R. Misra. The model combines news headlines and short descriptions, vectorizes the text data using TF-IDF, and classifies the categories using Logistic Regression.

---

## Dataset

- **Source:** [News Category Dataset](https://www.kaggle.com/rmisra/news-category-dataset) on Kaggle
- **Format:** JSON lines file with fields like `headline`, `short_description`, and `category`.

---

## Features

- Combines the `headline` and `short_description` into a single text field for better context.
- Uses TF-IDF vectorization for text feature extraction.
- Logistic Regression for multi-class classification.
- Evaluation includes classification report and confusion matrix visualization.
- Saves the trained model and vectorizer for later use.



## Requirements

- Python 3.7+
- pandas
- scikit-learn
- matplotlib
- seaborn
- joblib
- kagglehub (for downloading the dataset)

You can install the required packages using:

```bash
pip install pandas scikit-learn matplotlib seaborn joblib kagglehub

