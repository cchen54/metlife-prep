from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. This is the "Structure" of the data we want to grab
class UserData(BaseModel):
    name: str
    email: str
    security_clearance: int

# 2. This is our temporary "Storage" (A simple list)
# In Week 3, we will replace this with a real Database
database = []

@app.get("/")
def home():
    return {"message": "MetLife Data Gateway Online"}

# 3. This is the API "Grabbing" the data and saving it
@app.post("/submit-data")
def grab_data(user: UserData):
    # We take the data from the website/form
    new_entry = user.dict()
    
    # We "Save" it into our list
    database.append(new_entry)
    
    return {"status": "Success", "data_saved": new_entry}

# 4. This lets us check what is currently inside our database
@app.get("/view-all")
def view_data():
    return {"current_database": database}