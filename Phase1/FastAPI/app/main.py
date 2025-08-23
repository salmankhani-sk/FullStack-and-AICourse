from fastapi import FastAPI, status
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

@app.post("/users/", status_code=201)
def create_user(user: User):
    return {"message": "User created successfully", "user": user}


class Feedback(BaseModel):
    user_id: int
    comments: str
    rating: int
@app.post("/feedback/", status_code=status.HTTP_201_CREATED)
def submit_feedback(feedback: Feedback):
    return {"message": "Feedback submitted successfully", "feedback": feedback}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about")
def about():
    return {"About": "This is a sample FastAPI application."}
# Endpoint to get user information
@app.get("/users/{user_id}")
def get_user(user_id: str):
    return {"user_id": user_id, "name": f"WWelcome  {user_id} to our service!"}
@app.get("/search")
def search(query: str):
    return {"query": query, "results": f"Results for {query}"}



# Endpoint to get items