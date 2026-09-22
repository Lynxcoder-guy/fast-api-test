from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Supaya frontend bisa akses API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Contoh "database" sederhana
registered_names = {"budi", "siti", "andi"}
registered_age = {15, 16, 17}

@app.get("/check")
def check_name(nama: str = Query(...)):
    if nama.lower() in registered_names:
        return {"hewoo": f"Nama '{nama}' terdaftar ✅"}
    else:
        return {"hewoo": f"Nama '{nama}' tidak ditemukan ❌"}

@app.get("/age")
def check_age(age: int = Query(...)):
    if age in registered_age:
        return {"hewoo": f"Age '{age}' terdaftar"}
    else:
        return{"hewoo": f"Age '{age}' tidak ditemukan"}
