from fastapi import FastAPI,Path,HTTPException
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

@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(...,description="ID of the patient should be in DB",example="P0001")):
    data=load_dataset()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=400,details="patient not found in the database")