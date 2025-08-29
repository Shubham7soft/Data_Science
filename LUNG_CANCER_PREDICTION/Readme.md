# 🏥 Lung Cancer Prediction System
This project focuses on developing a robust machine learning model to predict the presence of lung cancer based on various health indicators. Leveraging a comprehensive dataset, this system aims to assist in early detection by identifying high-risk individuals with a focus on minimizing false negatives.

## 🎯 Project Goal
The primary objective of this project is to build an accurate and reliable classification model that can predict whether an individual has lung cancer. Special emphasis is placed on optimizing for recall (sensitivity) for the positive class (individuals with cancer), as missing a positive case (false negative) can have more severe consequences in a medical context than a false positive.

## 📊 Dataset
The project utilizes the lung_cancer.csv dataset, which includes various demographic and health-related features.

# Key Features:

GENDER

AGE

SMOKING

YELLOW_FINGERS

ANXIETY

PEER_PRESSURE

CHRONIC DISEASE

FATIGUE

ALLERGY

WHEEZING

ALCOHOL CONSUMING

COUGHING

SHORTNESS OF BREATH

SWALLOWING DIFFICULTY

CHEST PAIN

LUNG_CANCER (Target Variable: YES/NO)

# 🛠️ Technologies & Libraries
Python: The core programming language.

Jupyter Notebooks: For interactive development and analysis.

Pandas: For data manipulation and analysis.

NumPy: For numerical operations.

Scikit-learn (Sklearn): For machine learning model implementation and evaluation.

Classification Algorithms: Logistic Regression, Support Vector Machine (SVM), Multilayer Perceptron (MLP).

Matplotlib & Seaborn: For data visualization and exploratory data analysis (EDA).

# 🧪 Methodology
The project follows a standard machine learning pipeline:

##  1.Data Loading and Initial Exploration:

.Loading the lung_cancer.csv dataset.

.Inspecting data types, summary statistics, and initial data structure.

## 2.Data Preprocessing:

.Handling Missing Values: Addressing any missing data points.

.Categorical Feature Encoding: Converting categorical variables (e.g., GENDER, SMOKING, LUNG_CANCER) into numerical formats suitable for machine learning models.

.Outlier Management: Identifying and managing outliers in numerical features (e.g., AGE using methods like IQR).

## 3.Exploratory Data Analysis (EDA):

.Visualizing feature distributions (e.g., age, gender, smoking habits).

.Analyzing correlations between features and the target variable (LUNG_CANCER).

.Generating insights into the dataset characteristics.

## 4.Model Building and Evaluation:

.Splitting the data into training and testing sets.

.Implementing and training various classification models:

   .Logistic Regression: A robust linear model.

   .Support Vector Machine (SVM): Effective for high-dimensional data.

   .Multilayer Perceptron (MLP): A basic neural network approach.

.Model Evaluation: Assessing model performance using key metrics, with a strong focus on:

   .Recall (Sensitivity) for Class 1 (Lung Cancer 'YES').

   .Precision, F1-score, and Accuracy.

.Model Selection: Identifying the best-performing model (Logistic Regression was highlighted for its balanced performance).

# ✨ Key Findings
.The project successfully developed a classification system capable of predicting lung cancer.

.Logistic Regression emerged as an optimal model, demonstrating strong accuracy and a favorable balance between precision and recall, which is vital for medical diagnostic support.

.The emphasis on recall for Class 1 ensures that the model is effective in detecting as many actual positive cases as possible, minimizing the risk of missed diagnoses.

