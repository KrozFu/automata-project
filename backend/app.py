from fastapi import FastAPI, UploadFile, File
from os import getcwd
import program


app = FastAPI()


@ app.get("/")
def read_root():
    return "welcome"


@ app.post('/upload')
async def upload_file(file: UploadFile = File(...)):
    with open(getcwd() + "/" + file.filename, "wb") as myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()
    return "success"


@ app.get("/renderAutomata")
def read_atumata():
    a = program.GraficoAutomata()
    grafo = a.cargarDatos("Inicie_con_tres_ceros.json")
    return grafo
