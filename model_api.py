# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 18:59:00 2022

@author: CLAUDIO SOTO
"""

# se intala boto3 
# se instala flask para conectarse con AWS 
import boto3
from flask import Flask, request
import joblib


client = boto3.client("s3")

print('PyCharm')

response = client.list_buckets()


print(response['Buckets'])

## Establece la conexion al servidor 

app = Flask(__name__)
@app.route("/")

def index():
    return "Hi Flask"

@app.route("/predict", methods=["POST"])
def predict():
    request_data = request.get_json()
    age = request_data["age"]
    sex = request_data["sex"]
    credit_amount = request_data["credit_amount"]
    duration = request_data["duration"]
    purpose = request_data["purpose"]
    housing = request_data["housing"]
    prediction=model.predict([[age,sex,credit_amount,duration,purpose,housing]])
    model.transform([[age,credit_amount,duration,sex,purpose,housing]])
    ##return f"{age}, {sex}, {credit_amount}, {duration}, {purpose}, {housing}"
    return jsonify({"prediction":prediction.tolist()})




if __name__ == '__main__':
    app.run()
    
s3 = boto3.resource('s3')

s3.meta.client.download_file('germancreditcsr','Modelo/model.joblib','model.joblib') 

model = joblib.load('model.joblib')   
    