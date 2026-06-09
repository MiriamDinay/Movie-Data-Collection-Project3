from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib
from assets_data_prep import prepare_data

app = Flask(__name__)

try:
    model = joblib.load('trained_model.pkl')
except Exception as e:
    print(f"Error loading model: {e}")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        required_fields = ['startYear', 'runtimeMinutes', 'genres', 'Country', 'plot']
        
        for field in required_fields:
            if field not in data or data[field] == '':
                return jsonify({'error': f'Missing field: {field}'}), 400
        
        try:
            float(data['startYear'])
            float(data['runtimeMinutes'])
        except ValueError:
            return jsonify({'error': 'Invalid value: Year and Runtime must be numeric'}), 400
            
        df = pd.DataFrame([data])
        
        try:
            X_prepared = prepare_data(df)
        except Exception as e:
            return jsonify({'error': f'Error in data preparation: {str(e)}'}), 400
            
        prediction = model.predict(X_prepared)[0]
        
        return jsonify({'predicted_rating': round(prediction, 1)}), 200
        
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)