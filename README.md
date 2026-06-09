# Movie Rating Predictor - Flask Web App

## 1. Project Description
This project is a web application built with Flask that deploys a trained Random Forest machine learning model. It allows users to input specific movie details and provides a predicted IMDB rating in real-time.

## 2. Installation Instructions
1. Clone this repository to your local machine.
2. Open your command prompt/terminal and navigate to the project folder.
3. Create a virtual environment:
   python -m venv venv
4. Activate the virtual environment:
   Windows: venv\Scripts\activate
   Mac/Linux: source venv/bin/activate
5. Install the required packages:
   pip install -r requirements.txt

## 3. Execution Instructions
To run the server, ensure your virtual environment is activated and run the following command in your terminal:
python api.py

## 4. Application Access
Once the server is running, open your web browser and go to:
http://localhost:5000

## 5. Required Input Fields & Expected Values
* **Release Year:** A numeric value for the release year (e.g., 2023).
* **Runtime (Minutes):** A numeric value representing duration (e.g., 120).
* **Genres:** A comma-separated list of genres (e.g., Action, Drama).
* **Production Countries:** A comma-separated list of countries (e.g., United States, UK).
* **Plot Summary:** Free text describing the plot. The backend calculates the length of the text as a feature for the model.
