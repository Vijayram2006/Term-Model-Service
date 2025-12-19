from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.dependencies import get_db, get_current_user

router = APIRouter(
    prefix="/terms",
    tags=["terms"],
)

# ---------------------------
# GET /terms/  (List Terms)
# ---------------------------
@router.get("/", response_model=list[schemas.TermOut])
def list_terms(db: Session = Depends(get_db)):
    return db.query(models.Term).all()


# ---------------------------
# POST /terms/ (Create Term)
# 🔒 Protected
# ---------------------------
@router.post(
    "/",
    response_model=schemas.TermOut,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(get_current_user)],
)
def create_term(term: schemas.TermCreate, db: Session = Depends(get_db)):
    db_term = models.Term(**term.dict())
    db.add(db_term)
    db.commit()
    db.refresh(db_term)
    return db_term


# ---------------------------
# GET /terms/{term_rid}
# ---------------------------
@router.get("/{term_rid}", response_model=schemas.TermOut)
def get_term(term_rid: int, db: Session = Depends(get_db)):
    term = db.query(models.Term).filter(models.Term.term_rid == term_rid).first()
    if not term:
        raise HTTPException(status_code=404, detail="Term not found")
    return term


# ---------------------------
# PUT /terms/{term_rid}
# 🔒 Protected
# ---------------------------
@router.put(
    "/{term_rid}",
    response_model=schemas.TermOut,
    dependencies=[Depends(get_current_user)],
)
def update_term(
    term_rid: int,
    term_data: schemas.TermCreate,
    db: Session = Depends(get_db),
):
    term = db.query(models.Term).filter(models.Term.term_rid == term_rid).first()
    if not term:
        raise HTTPException(status_code=404, detail="Term not found")

    for key, value in term_data.dict().items():
        setattr(term, key, value)

    db.commit()
    db.refresh(term)
    return term


# ---------------------------
# DELETE /terms/{term_rid}
# 🔒 Protected
# ---------------------------
@router.delete(
    "/{term_rid}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(get_current_user)],
)
def delete_term(term_rid: int, db: Session = Depends(get_db)):
    term = db.query(models.Term).filter(models.Term.term_rid == term_rid).first()
    if not term:
        raise HTTPException(status_code=404, detail="Term not found")

    db.delete(term)
    db.commit()
    return None
