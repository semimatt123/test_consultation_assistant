

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fonction_ia import function_ia
from script import num_pre
from script2 import fonction_appel_ia, ordi_premier, ordi_premier2

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

response = """
<html>
<head>
<style>
h1 {
    text-align: center;
    font-size: 200px;
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

#@app.get("/", response_class=HTMLResponse)
def read_root():
    return response

@app.get("/users/{user_id}")
def read_user(user_id: int):
    response = num_pre(user_id)
    return {"user_id": response}



@app.get("/ai_premier/{nombre}")
def nombre_(nombre: int):
    response2= function_ia(f"Est-ce que {nombre} est premier ? ")
    return {"nombre": response2}

@app.get("/ordi_premier/{nombre}")
def nombre_ordi(nombre: int):
    response3= ordi_premier(nombre)
    return {"nombre": response3}

@app.get("/ordi_premier2/{nombre}")
def nombre_ordi(nombre: int):
    response4= ordi_premier2(nombre)
    return {"nombre": response4}




