# -*- coding: utf-8 -*-
"""news.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dp5HIJ2EluNM4PfQ5uAAF_DpwwK3XUQH
"""

import kagglehub

# Download latest version
path = kagglehub.dataset_download("rmisra/news-category-dataset")

print("Path to dataset files:", path)

import pandas as pd
import os

# Define the path to the dataset
dataset_path = os.path.join(path, 'News_Category_Dataset_v3.json')

# Load the dataset into a pandas DataFrame
df = pd.read_json(dataset_path, lines=True)

# Combine 'headline' and 'short_description' into a single text field
df['text'] = df['headline'] + ' ' + df['short_description']

# Select relevant columns for analysis
df = df[['category', 'text']]

# Optional: Display the number of articles per category
print(df['category'].value_counts())

from sklearn.model_selection import train_test_split

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['category'], test_size=0.2, random_state=42
)

from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize the TF-IDF Vectorizer
vectorizer = TfidfVectorizer(max_features=5000)

# Fit and transform the training data; transform the testing data
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

from sklearn.linear_model import LogisticRegression

# Initialize the Logistic Regression model
model = LogisticRegression(max_iter=1000)

# Train the model on the TF-IDF-transformed training data
model.fit(X_train_tfidf, y_train)

from sklearn.metrics import classification_report

# Predict categories for the testing data
y_pred = model.predict(X_test_tfidf)

# Display the classification report
print(classification_report(y_test, y_pred))

import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Assuming y_test and y_pred are defined
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
import pandas as pd

# Generate classification report
report = classification_report(y_test, y_pred, output_dict=True)
df_report = pd.DataFrame(report).transpose()

# Select only the classes (excluding 'accuracy', 'macro avg', 'weighted avg')
df_classes = df_report.iloc[:-3, :]

# Plot heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df_classes[['precision', 'recall', 'f1-score']], annot=True, cmap='YlGnBu')
plt.title('Classification Report Heatmap')
plt.ylabel('Classes')
plt.xlabel('Metrics')
plt.show()

import joblib

# Save the trained model
joblib.dump(model, 'news_classifier_model.pkl')

# Save the TF-IDF vectorizer
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')