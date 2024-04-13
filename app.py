# from flask import Flask, request, render_template, redirect, url_for, flash
# import joblib
# import numpy as np
# from preprocess import preprocess_url
# import logging

# # Initialize logging
# logging.basicConfig(level=logging.INFO)

# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here'

# # Load the model
# model_path = './models/model_pickle'
# model = joblib.load(model_path)
# logging.info("Model loaded successfully.")

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         url = request.form['url']
        
#         # Preprocess the URL to extract features
#         processed_features = preprocess_url(url)
        
#         # Ensure the input is in a 2D shape as expected by the model
#         processed_features_2d = np.array([processed_features])
#         # Before predicting in app.py
#         processed_features = preprocess_url(url)
#         print("Processed features for URL:", processed_features)
#         # Convert test_features to 2D array as expected by the model
#         test_features_2d = [processed_features]

# # Use the model to predict
#         print("Test prediction:", model.predict(test_features_2d))
#         # Make a prediction
#         prediction = model.predict([processed_features])[0]
#         if prediction == 3:  # Example condition, adjust based on your use case
#             flash('Malicious URL detected!', 'danger')
#         else:
#             flash('URL appears to be safe.', 'success')
#           # Redirect to the URL if it's considered safe

#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, request, render_template, redirect, url_for, flash
# import joblib
# import numpy as np
# from preprocess import preprocess_url

# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here'

# # Load the model
# model_path = './models/model_pickle'
# model = joblib.load(model_path)

# # Mapping of model numeric predictions to category names
# category_mapping = {
#     0: 'Benign',
#     1: 'Defacement',
#     2: 'Phishing',
#     3: 'Malware'
# }

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         url = request.form['url']
        
#         # Preprocess the URL and predict
#         processed_features = preprocess_url(url)
#         processed_features_2d = np.array([processed_features])
#         prediction = model.predict(processed_features_2d)[0]  # Assume model.predict returns a list
        
#         # Get the category name from the mapping
#         predicted_category = category_mapping.get(prediction, "Unknown")
        
#         # Provide feedback based on the prediction
#         if predicted_category == "Malware" or predicted_category == "Phishing":
#             flash(f'Dangerous URL detected! Category: {predicted_category}. Please be cautious.', 'danger')
#         elif predicted_category == "Defacement":
#             flash(f'Potentially harmful URL detected! Category: {predicted_category}.', 'warning')
#         else:
#             flash('URL appears to be safe.', 'success')
#             return redirect(url) 
#             # Consider the security implications of redirecting to potentially harmful URLs
#             # return redirect(url)
            
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, render_template, redirect, url_for, flash
import joblib
import numpy as np
from preprocess import preprocess_url

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Load the model
model_path = './models/model_pickle'
model = joblib.load(model_path)

# Mapping of model numeric predictions to category names
category_mapping = {
    0: 'Benign',
    1: 'Defacement',
    2: 'Phishing',
    3: 'Malware'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        
        # Preprocess the URL and predict
        processed_features = preprocess_url(url)
        processed_features_2d = np.array([processed_features])
        prediction = model.predict(processed_features_2d)[0]
        probabilities = model.predict_proba(processed_features_2d)[0]
        predicted_category = category_mapping.get(prediction, "Unknown")
        accuracy = np.max(probabilities)  # Assuming the highest probability as the accuracy
        
        # Provide feedback based on the prediction
        message = f'Category: {predicted_category}. Accuracy: {accuracy:.2%}'
        if predicted_category in ["Malware", "Phishing"]:
            flash(f'Dangerous URL detected! {message}', 'danger')
        elif predicted_category == "Defacement":
            flash(f'Potentially harmful URL detected! {message}', 'warning')
        else:
            flash(f'URL appears to be safe. {message}', 'success')
            return redirect(url) 
            
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
