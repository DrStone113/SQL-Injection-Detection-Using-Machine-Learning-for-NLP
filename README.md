# SQL Injection Detection using NLP & Streamlit

This project is a web application built with Streamlit, utilizing Machine Learning and Natural Language Processing (NLP) techniques to detect SQL Injection attacks. Users can input a query string, and the application will predict whether the string is malicious or not.

---

✨ **Features**

- **Real-time analysis:** Instantly analyze query strings entered by users.
- **NLP Model:** Uses TF-IDF and Logistic Regression for text classification.
- **User-friendly interface:** Simple and clean UI built with Streamlit.
- **Clear result display:** Results are shown with colors (Red for malicious, Green for safe) and model confidence scores.
- **Easy deployment:** Can be easily deployed on Streamlit Community Cloud.

---

🚀 **Demo**

Below is the interface of the application when analyzing different types of queries.

- Case 1: Detecting malicious queries

  ![Case 1 Screenshot](images/screenshot-1.png)

- Case 2: Confirming safe queries

  ![Case 2 Screenshot](images/screenshot-2.png)

### Live Demo

The application is deployed and accessible online at:

[Streamlit Community Cloud Deployment](https://sql-injection-detection-using-machine-learning-for-nlpgit-75jh.streamlit.app/)

---

🛠️ **Installation and Local Run**

To run this project on your machine, follow these steps.

### 1. Requirements

- Python 3.8+
- Git

### 2. Installation

a. Clone the repository:

Open a terminal and run the following commands to clone the source code:

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

Alternatively, you can clone the original repository this project is based on:

```bash
git clone https://github.com/Shaffaprawira/SQL-Injection-Detection-Using-Machine-Learning-for-NLP.git
```

b. Create and activate a virtual environment:

A virtual environment helps manage project dependencies independently.

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows)
.\.venv\Scripts\activate

# Activate virtual environment (macOS/Linux)
# source .venv/bin/activate
```

c. Install required libraries:

Install all dependencies from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

---

📈 **Usage**

The project includes two main scripts: model training and running the application.

### 1. Model Training (Optional)

The model is pre-trained and saved in the `model/` folder. However, if you want to retrain the model with new data, run:

```bash
python train.py
```

This command will:

- Read data from `data/sqli_dataset.csv`.
- Process and clean the data.
- Train a new Logistic Regression model.
- Save the trained model and vectorizer in the `model/` folder.

### 2. Run the Web Application

To launch the web interface, run:

```bash
streamlit run app.py
```

A new browser tab will open automatically, displaying the application. You can now input queries to test.

---

📂 **Project Structure**

```
.
├── data/
│   └── sqli_dataset.csv      # Dataset for training
├── model/
│   ├── model.pkl             # Trained model file
│   └── vectorizer.pkl        # Saved TF-IDF vectorizer
├── .venv/                   # Virtual environment folder
├── app.py                   # Streamlit application source code
├── train.py                 # Script for training the model
├── requirements.txt         # List of required libraries
└── README.md                # This instruction file
```

---

💻 **Technologies Used**

- **Python:** Main programming language.
- **Scikit-learn:** Used to build and train the Logistic Regression model.
- **Pandas:** Used for data processing and manipulation.
- **NLTK:** Used for natural language processing (e.g., stopword removal).
- **Streamlit:** Used to build the interactive web interface.
- **Joblib:** Used to save and load the trained model.

---

🙏 **Acknowledgments**

This project is developed based on the ideas and dataset from the repository SQL-Injection-Detection-Using-Machine-Learning-for-NLP by Shaffaprawira.

Original repository link: [GitHub - Shaffaprawira/SQL-Injection-Detection-Using-Machine-Learning-for-NLP](https://github.com/Shaffaprawira/SQL-Injection-Detection-Using-Machine-Learning-for-NLP.git)
