from fastapi import FastAPI
from app.db import Base, engine
from app.routers import auth, terms, term_selfsame, term_synonym

app = FastAPI(
    title="Term Model Service",
    description="Term Model Service with JWT Authentication",
    version="0.1.0",
)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    print("Database ready")

@app.get("/")
def root():
    return {"message": "Term Model Service is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(auth.router)
app.include_router(terms.router)
app.include_router(term_selfsame.router)
app.include_router(term_synonym.router)
