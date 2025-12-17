# Multiple_Result_Prediction_NB

🎯 Objective

The objective of this project is to predict whether a student will Pass or Fail based on:

Number of subjects

Study hours

Attendance percentage

Previous result

🧠 Algorithm Used

Gaussian Naive Bayes (GaussianNB)

A supervised machine learning algorithm

Works well with small datasets

Assumes features follow a normal distribution

📄 Project Description

This project uses a Naive Bayes classification model from scikit-learn to predict student performance.

Steps involved:

Created a small dataset of students with features like hours studied, attendance, and previous results.

Split the data into training and testing sets.

Trained the model using GaussianNB.

Evaluated the model using accuracy score.

Predicted results (Pass/Fail) for new students in different subjects like Maths, Physics, Chemistry, English, and Hindi.

📊 Outcome

The model successfully predicts whether a student will Pass or Fail.

Accuracy score is displayed after testing.

New student predictions are printed subject-wise.

Output is easy to understand (pass or fail).

🛠️ Technologies Used

Python

Scikit-learn

Naive Bayes Algorithm

▶️ How to Run the Project

Install required libraries:

pip install scikit-learn


Run the Python file:

python student_prediction.py

📌 Sample Output
Accuracy: 1.0
[2, 60, 1]
pass
[2, 60, 0]
fail

🔗 GitHub Repository

👉 GitHub Repo Link:

https://github.com/your-username/student-pass-fail-prediction


(Replace your-username with your actual GitHub username)

📝 Short Project Summary (For Viva / Resume)

Project Name: Student Pass/Fail Prediction

Objective: Predict student performance using machine learning

Algorithm: Gaussian Naive Bayes

Input: Study hours, attendance, previous result

Output: Pass or Fail

Result: Accurate predictions with simple dataset
