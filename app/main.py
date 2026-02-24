from fastapi import FastAPI
from app.db.session import engine, Base
from app.api.v1.auth_routes import router as auth_router
from app.api.v1.invoice_routes import router as invoice_router
from app import models



app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)


# home route
@app.get("/")
def home():
    return {"message": "Server running"}

# auth router
app.include_router(auth_router)
app.include_router(invoice_router)