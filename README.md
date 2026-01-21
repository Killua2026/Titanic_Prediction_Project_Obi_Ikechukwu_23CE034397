# 🚢 Titanic Survival Prediction System

A Machine Learning-powered web application that predicts whether a passenger would have survived the Titanic disaster based on their personal information. This project implements a **Random Forest Classifier** served via a **Flask** web interface.

**[🔴 Live Demo Link](https://titanic-prediction-project-obi-ikechukwu.onrender.com)**

---

## 📖 Table of Contents
- [Project Overview](#project-overview)
- [Features Used](#features-used)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation & Local Setup](#installation--local-setup)
- [Model Performance](#model-performance)
- [Deployment](#deployment)
- [Author](#author)

---

## 🧐 Project Overview
The sinking of the Titanic is one of the most infamous shipwrecks in history. This project uses machine learning to analyze passenger data (like age, gender, and socio-economic class) to build a predictive model that determines the likelihood of survival.

**Dataset Source:** [Titanic dataset](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)

---

## 🔢 Features Used
The model was trained on the following 5 key features selected from the original dataset:

1. **Pclass (Passenger Class):** Socio-economic status (1st = Upper, 2nd = Middle, 3rd = Lower).
2. **Sex:** Gender of the passenger (Male/Female).
3. **Age:** Age in years.
4. **SibSp:** Number of siblings or spouses aboard the Titanic.
5. **Fare:** Passenger fare (ticket price).

---

## 🛠 Tech Stack
* **Programming Language:** Python 3.x
* **Web Framework:** Flask
* **Machine Learning:** Scikit-learn, Pandas, NumPy
* **Model Persistence:** Joblib
* **Frontend:** HTML, CSS
* **Deployment:** Render.com

---

## 📂 Project Structure

```text
Titanic_Project_ObiIkechukwuJoseph_23CE034397/
│
├── app.py                   # Main Flask application
├── requirements.txt         # List of dependencies
├── README.md                # Project documentation
│
├── model/
│   ├── model_building.ipynb # Jupyter notebook used to train the model
│   └── titanic_survival_model.pkl # Saved Random Forest model
│
└── templates/
    └── index.html           # HTML Interface for the web app
