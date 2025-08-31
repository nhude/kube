import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Optional: allow .env locally without affecting prod
try:
    # If python-dotenv is not installed in runtime, this import will fail silently
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()  # does nothing if no .env present
except Exception:
    pass

app = FastAPI()

# Read port once for the startup log (defaults to 8000)
PORT = int(os.getenv("PORT", "8000"))

@app.on_event("startup")
async def on_startup():
    # Exact required message:
    print(f"Server started in port {PORT}", flush=True)

@app.get("/health")
async def health():
    return JSONResponse({"status": "ok"})
