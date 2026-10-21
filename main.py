from fastapi import FastAPI

app = FastAPI(title="Biblioteca API")

@app.get("/")
async def root():
    return {"hola"}