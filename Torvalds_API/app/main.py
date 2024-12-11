from fastapi import FastAPI
from app.core.cors import CorsConfig 
from app.api.v1.email import router

app = FastAPI()

CorsConfig.add_cors(app)

app.include_router(router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome to Torvalds API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)