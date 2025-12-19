from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app import models, schemas

router = APIRouter(
    prefix="/term-selfsame",
    tags=["term_selfsame"]
)

@router.get("/")
def list_selfsame(db: Session = Depends(get_db)):
    return db.query(models.TermSelfsame).all()

@router.post("/")
def create_selfsame(
    data: schemas.TermSelfsameCreate,
    db: Session = Depends(get_db)
):
    obj = models.TermSelfsame(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.delete("/{term_selfsame_rid}")
def delete_selfsame(term_selfsame_rid: int, db: Session = Depends(get_db)):
    obj = db.query(models.TermSelfsame).get(term_selfsame_rid)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(obj)
    db.commit()
    return {"deleted": True}

