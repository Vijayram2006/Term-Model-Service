from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserCreate(BaseModel):
    username: str
    password: str


class TermCreate(BaseModel):
    turf_rid: int
    term_id: str
    language: str | None = None
    country: str | None = None
    term_name: str | None = None
    term_description: str | None = None
    term_acronym: str | None = None
    is_machinized_name: bool = False
    is_standardized_name: bool = True


class TermOut(TermCreate):
    term_rid: int

    class Config:
        from_attributes = True


class TermSelfsameCreate(BaseModel):
    term_selfsame_id: str
    turf_rid: int
    term_rid: int


class TermSynonymCreate(BaseModel):
    term_synonym_id: str
    turf_rid: int
    term_id: str
