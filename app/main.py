from typing import List

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


# Retrieving a specific link by its ID.
@app.get("/links/{id}", response_model=schemas.LinkOut)
def get_link(id: int, db: Session = Depends(get_db)):
    # Find the FIRST record in the database whose ID matches the ID we sent.
    link = db.query(models.Link).filter(models.Link.id == id).first()

    # Not found error
    if not link:
        raise HTTPException(status_code=404, detail="Link bulunamadı !!!")
    return link


# A link delete
@app.delete("/links/{id}")
def delete_link(id: int, db: Session = Depends(get_db)):
    # Step 1: First, find this link in the database.
    link = db.query(models.Link).filter(models.Link.id == id).first()

    # Step 2:İf link is not (none), HTTPException throw.(404)
    if not link:
        print("HTTP 404 ")
        raise HTTPException(status_code=404, detail="Silecek bir şey bulamadım!")

    # Step 3:If a link exists, issue the command to delete it from the database.
    db.delete(link)

    # Step 4:Commit the change at database.
    db.commit()

    # Step 5:Return the massage
    return {"message": f"{id} numaralı link başarıyla uçtu!"}
