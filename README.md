# Movie Rating Predictor - Flask Web App

## 1. Project Description
This project is a web application built with Flask that deploys a trained Random Forest machine learning model. It allows users to input specific movie details and provides a predicted IMDB rating in real-time.

## 2. Installation Instructions
1. Clone this repository to your local machine.
2. Open your command prompt/terminal and navigate to the project folder.
3. Create a virtual environment:
   `python -m venv venv`
4. Activate the virtual environment:
   * Windows: `venv\Scripts\activate`
   * Mac/Linux: `source venv/bin/activate`
5. Install the required packages:
   `pip install -r requirements.txt`

## 3. Execution Instructions
To run the server, ensure your virtual environment is activated and run the following command in your terminal:
`python api.py`

## 4. Application Access
Once the server is running, open your web browser and go to:
http://localhost:5000

## 5. Required Input Fields & Expected Values
* **Release Year (`startYear`):** Integer year of release. Expected range ~1888-2030 (e.g., 1994).
* **Runtime in Minutes (`runtimeMinutes`):** Positive integer, typically 1-400 (e.g., 142).
* **Genres (`genres`):** Comma-separated list of genres (e.g., Drama, Crime). Used to derive the number of genres, the primary genre, and the `is_drama` / `is_comedy` / `is_documentary` flags.
* **Production Countries (`Country`):** Comma-separated list of countries (e.g., United States, UK). Used to derive `is_US` and the number of production countries.
* **Plot Summary (`plot`):** Free text describing the plot. The number of words in the text is used as a feature (`plot_length`).
**Note on Project Structure:**
* The HTML page is located in the `templates/` folder, as required by Flask's `render_template()`.
* The trained model (`trained_model.pkl`) was trained with scikit-learn 1.6.1, which is pinned in `requirements.txt` so the model loads correctly.
