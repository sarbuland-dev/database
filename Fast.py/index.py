from fastapi import FastAPI
app= FastAPI()
@app.get('/')
def read_something():
    return {'meg':'hello! world '}