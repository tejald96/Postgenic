#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from flask import Flask, request, render_template 
import pickle
import numpy as np
import sys

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/capstone', methods =["POST"])
def capstone():
        
    feature =  [x for x in request.form.values()]
    feature = feature[:-1]
    features = [int(i) for i in feature]
    print(features, file=sys.stderr)
    final_features = np.array([features])
    prediction = model.predict(final_features)
    print(prediction, file=sys.stderr)
	# username = request.form.get("username")
	# followers = request.form.get("followers")
	# following = request.form.get("following")
	# likes = request.form.get("likes")
	# day = request.form.get("day")
	# type = request.form.get("type")
	# prediction = model.predict(followers,following,likes,day,type)
    if prediction[0] == 1:
        predict = "Morning"
    elif prediction[0] == 2:
        predict = "Evening"
    elif prediction[0] == 3:
        predict = "Night"
    else:
        predict = "Undetermined"
    return render_template('index.html', predicted_time='You should post at {}'.format(predict))
   
@app.route('/results',methods=["POST"])
def results():
    data = request.get_json(force=True)
    prediction = model.predict(followers,following,likes,day,type)
    return jsonify(prediction)

  
if __name__=='__main__':
   app.run(debug=True)



