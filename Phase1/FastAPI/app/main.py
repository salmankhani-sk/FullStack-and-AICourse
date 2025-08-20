from fastapi import FastAPI
app = FastAPI()
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