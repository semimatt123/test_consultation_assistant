

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from script import num_pre

app = FastAPI()

response = """
<html>
<head>
<style>
h1 {
    text-align: center;
    font-size: 100px;
}
h2 {
    text-align: center;
}
img {
    width: 300px;
}
</style>
</head>
<body>
<h1 style="color: #6D1D40;">Site web</h1>

<h2 style="color: black;">banane</h2>

<img src="https://www.u-run.fr/wp-content/uploads/2015/02/banane.jpg" alt="image"/>

</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def read_root():
    return response

@app.get("/users/{user_id}")
def read_user(user_id: int):
    response = num_pre(user_id)
    return {"user_id": response}


