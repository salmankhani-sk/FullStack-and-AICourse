from fastapi import FastAPI, status
from pydantic import BaseModel
app = FastAPI()

fk_users = {
    1: {"name": "Salman", "email": "salmank.developer@gmail.com"},
    2: {"name": "Bob", "email": "Bob@gmail.com"},
    3: {"name": "Charlie", "email": "ch@gmail.com"}
}

@app.delete("/users/{user_id}", status_code= 200)
def delete_user(user_id: int):
    if user_id in fk_users:
        delelted_user = fk_users.pop(user_id)
        return {"message": "User deleted successfully", "user": delelted_user}
    return {"error": "User not found"}


@app.delete("/users/{user_id}", status_code=204)
def delete_user_no_content(user_id: int):
    if user_id in fk_users:
        fk_users.pop(user_id)
        return
    return {"error": "User not found"}

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


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id in fk_users:
        fk_users[user_id] = user.dict()
        return {"message": "User updated successfully", "user": fk_users[user_id]}
    return {"error": "User not found"}
@app.patch("/users/{user_id}")
def partial_update_user(user_id: int, user: User):
    if user_id in fk_users:
        stored_user_data = fk_users[user_id]
        update_data = user.dict(exclude_unset=True)
        stored_user_data.update(update_data)
        fk_users[user_id] = stored_user_data
        return {"message": "User partially updated successfully", "user": fk_users[user_id]}
    return {"error": "User not found"}

# Endpoint to get items