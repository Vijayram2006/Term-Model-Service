from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app import models, schemas

router = APIRouter(
    prefix="/term-synonym",
    tags=["term_synonym"]
)

@router.get("/")
def list_synonyms(db: Session = Depends(get_db)):
    return db.query(models.TermSynonym).all()

@router.post("/")
def create_synonym(
    data: schemas.TermSynonymCreate,
    db: Session = Depends(get_db)
):
    obj = models.TermSynonym(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.delete("/{term_synonym_rid}")
def delete_synonym(term_synonym_rid: int, db: Session = Depends(get_db)):
    obj = db.query(models.TermSynonym).get(term_synonym_rid)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(obj)
    db.commit()
    return {"deleted": True}
