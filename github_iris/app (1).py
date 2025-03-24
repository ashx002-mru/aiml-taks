#!/usr/bin/env python
# coding: utf-8

# In[9]:


# app.py

from flask import Flask, render_template, request
import joblib
import numpy as np

#Initialise flask app
app = Flask(__name__)

#Load trained model
model = joblib.load('iris_model.pkl')
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    #Get data from foem
    try:
        features = [float(request.form[f'features{i}']) for i in range(1, 5)]
    except ValueError:
        return render_template('result.html', prediction="Invalid input. Please enter numeric values.")
    # Make prediction
    prediction = model.predict([features])[0]

# Map prediction to class name
    class_name = ['setosa', 'Versicolor', 'Virginica']
    result = class_names[prediction]

    return render_templates('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug =True)
    


# In[ ]:




