from fastapi import FastAPI
app = FastAPI()

@app.get("/health")

def health():
    return{
  "status": "ok",
  "service": "mini-rag"
}
@app.get("/version")
def version():
    return{
  "version": "1.0.0"
}