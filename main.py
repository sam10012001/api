from fastapi import FastAPI, HTTPException

app = FastAPI()

# Base de datos en memoria
carros = [
    {"id": 1, "marca": "Toyota", "modelo": "Corolla", "año": 2022, "precio": 25000, "stock": 5},
    {"id": 2, "marca": "Honda", "modelo": "Civic", "año": 2023, "precio": 27000, "stock": 3},
    {"id": 3, "marca": "Ford", "modelo": "Mustang", "año": 2021, "precio": 40000, "stock": 2},
    {"id": 4, "marca": "Chevrolet", "modelo": "Camaro", "año": 2022, "precio": 42000, "stock": 4},
    {"id": 5, "marca": "Tesla", "modelo": "Model 3", "año": 2023, "precio": 50000, "stock": 6}
]

carrito = []

# Operaciones para Carros
@app.get("/carros")
def listar_carros():
    return carros

@app.post("/carros")
def agregar_carro(carro: dict):
    carro["id"] = max(c["id"] for c in carros) + 1 if carros else 1
    carros.append(carro)
    return {"mensaje": "Carro agregado", "carro": carro}

@app.get("/carros/{id}")
def obtener_carro(id: int):
    carro = next((c for c in carros if c["id"] == id), None)
    if not carro:
        raise HTTPException(status_code=404, detail="Carro no encontrado")
    return carro

@app.put("/carros/{id}")
def actualizar_carro(id: int, datos: dict):
    carro = next((c for c in carros if c["id"] == id), None)
    if not carro:
        raise HTTPException(status_code=404, detail="Carro no encontrado")
    carro.update(datos)
    return {"mensaje": "Carro actualizado", "carro": carro}

@app.delete("/carros/{id}")
def eliminar_carro(id: int):
    global carros
    carros = [c for c in carros if c["id"] != id]
    return {"mensaje": f"Carro {id} eliminado"}