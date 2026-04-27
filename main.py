from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.get("/health")
def read_health():
        return {"message": "healthy"}

@app.get ("/me")
def read_me():
       return {
  "name": "Martins Obaseki",
  "email": "yuwa619@gmail.com",
  "github": "https://github.com/yuwa619"
}