from fastapi import FastAPI

# fastAPI app starting
app = FastAPI(title="LinkVault API")


# Homapage (Root)
@app.get("/")
def read_root():
    return {"message:LinkVault API başarıyla çalışıyor! Merhaba genç"}
