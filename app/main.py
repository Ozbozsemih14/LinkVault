from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import database, models, schemas

# Create database table

models.Base.metadata.create_all(bind=database.engine)
# fastAPI app starting
app = FastAPI(title="LinkVault API")


# Database connection
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Homapage (Root) test
@app.get("/")
def read_root():
    return {"status": "Sistem Hazır", "message": "Veritabanı bağlantısı kuruldu!"}


# Create a new link
@app.post("/links", response_model=schemas.LinkOut)
def create_link(link: schemas.LinkCreate, db: Session = Depends(get_db)):
    # 1.Convert incoming data (schemas) into database model
    new_link = models.Link(title=link.title, url=link.url)

    # 2.Add to database
    db.add(new_link)

    # 3.Confirm the change
    db.commit()

    # Pull the new state of database
    db.refresh(new_link)

    return new_link


# List all links
@app.get("/links", response_model=list[schemas.LinkOut])
def get_links(db: Session = Depends(get_db)):
    links = db.query(models.Link).all()
    return links
