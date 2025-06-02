from fastapi import FastAPI
import json

def load_dataset():
    with open("patients.json",'r') as file:
        data=json.load(file) 
        return data

app=FastAPI()
@app.get('/')
def hello():
    return {'message':"patient management System API"}

@app.get('/about')
def about():
    return {"message":"A fully functional api to manage your patient records"}

@app.get('/view')
def view():
    data=load_dataset()
    return data