

## What is an API?
An API is like a menu at a restaurant. You (the app) order what you want, and the kitchen (server) sends it back. It helps apps share data without showing how they work inside.

### Why Use APIs?
- Connect your app to other services (e.g., get weather info).
- Make coding faster by reusing tools.
- Build apps that work on phones, websites, and more.

**Example**: Your phone app uses an API to show Google Maps.

## Setting Up FastAPI
FastAPI is a simple tool to make APIs in Python. It's fast and easy!

### Install It
Open your terminal and type:
```bash
pip install fastapi uvicorn
```

### Your First API
Create a file called `main.py` and add this code:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from my API!"}
```

- Run it: `uvicorn main:app --reload`
- Open in browser: `http://localhost:8000` (see the message).
- Test page: `http://localhost:8000/docs` (click to try it out).

## Types of APIs
There are different ways to build APIs, like different languages for talking. We'll learn REST most, but know the others too.

### 1. REST API
- **What**: Uses web links (URLs) and actions like GET (read data) or POST (add data).
- **Why**: Easy and works for most apps.
- **When to Use**: For getting or saving info, like in a shopping app.

**Example: To-Do List API**
Code in `main.py`:
```python
from fastapi import FastAPI

app = FastAPI()

todos = ["Buy milk"]  # Our list

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def add_todo(task: str):
    todos.append(task)
    return {"message": "Added: " + task}
```

- Test: In `/docs`, try GET to see the list, POST to add "Read book".

### 2. SOAP API
- **What**: Sends data in a strict format (like XML letters).
- **Why**: For safe, big company stuff.
- **When to Use**: Banks or old systems.

**Example** (Just to see, not code):
Send:
```xml
<GetInfo>
  <Name>Alice</Name>
</GetInfo>
```
Get back XML with info.

(Not easy in FastAPI – we use REST instead.)

### 3. GraphQL API
- **What**: Ask for exactly what data you want from one link.
- **Why**: No extra data waste.
- **When to Use**: Apps with lots of details, like social media.

**Example Code** (Add `pip install strawberry-graphql`):
```python
from fastapi import FastAPI
from strawberry import Schema, type
from strawberry.fastapi import GraphQLRouter

app = FastAPI()

@type
class Book:
    title: str

@type
class Query:
    def get_book(self) -> Book:
        return Book(title="Harry Potter")

schema = Schema(query=Query)
app.include_router(GraphQLRouter(schema), prefix="/graphql")
```

- Test at `/graphql`: Ask for `query { getBook { title } }` and get just the title.

### 4. gRPC API
- **What**: Super fast data sending for big systems.
- **Why**: Quick and efficient.
- **When to Use**: Games or many connected apps.

**Example** (Not full code):
Define:
```proto
service Chat {
  rpc SayHello (HelloRequest) returns (HelloReply);
}
```

(FastAPI can do it, but REST is simpler for us.)

### 5. WebSocket API
- **What**: Keeps a chat open for real-time messages.
- **Why**: Instant updates.
- **When to Use**: Chat apps or live scores.

**Example Code**:
```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/chat")
async def chat(websocket: WebSocket):
    await websocket.accept()
    while True:
        msg = await websocket.receive_text()
        await websocket.send_text("You said: " + msg)
```

- Test with a web page that connects and sends messages.

### 6. Webhook API
- **What**: Apps send you data when something happens.
- **Why**: No need to keep asking for updates.
- **When to Use**: Get alerts, like new email.

**Example Code**:
```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("Got data:", data)
    return {"ok": True}
```

- Test: Use a tool to send fake data to this link.

## Why We Focus on REST
- It's simple: Like using web buttons (GET, POST).
- FastAPI makes it fun with auto-tests.
- Used in real jobs for web and phone apps.

## Fun Project: Build a To-Do App
1. Use the REST example above for the backend.
2. Make a simple web page (HTML) to show and add to-dos.

HTML code:
```html
<body>
  <ul id="list"></ul>
  <input id="task">
  <button onclick="add()">Add</button>
  <script>
    async function show() {
      let res = await fetch('http://localhost:8000/todos');
      let data = await res.json();
      document.getElementById('list').innerHTML = data.map(t => `<li>${t}</li>`).join('');
    }
    async function add() {
      let task = document.getElementById('task').value;
      await fetch('http://localhost:8000/todos?task=' + task, {method: 'POST'});
      show();
    }
    show();
  </script>
</body>
```

- Run and play: Add tasks and see them!

## Tips for You
- Test everything in `/docs`.
- Ask questions if stuck.
- Practice by making your own API for a game or list.

