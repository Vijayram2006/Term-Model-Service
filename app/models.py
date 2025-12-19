from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship
from app.db import Base


# =========================
# TERM
# =========================
class Term(Base):
    __tablename__ = "term"

    term_rid = Column(Integer, primary_key=True, index=True)
    turf_rid = Column(Integer, nullable=False)

    term_id = Column(Text, nullable=False)
    language = Column(Text, nullable=False)
    country = Column(Text, nullable=False)

    term_name = Column(Text, nullable=False)
    term_description = Column(Text)
    term_acronym = Column(Text)

    is_machinized_name = Column(Boolean, default=False)
    is_standardized_name = Column(Boolean, default=False)

    # ❗ NO cascade here
    selfsames = relationship("TermSelfsame", back_populates="term")
    # ❗ No relationship for synonym on purpose (business key based)


# =========================
# TERM SELFSAME
# =========================
class TermSelfsame(Base):
    __tablename__ = "term_selfsame"

    term_selfsame_rid = Column(Integer, primary_key=True, index=True)
    term_selfsame_id = Column(Text, nullable=False)
    turf_rid = Column(Integer, nullable=False)

    term_rid = Column(
        Integer,
        ForeignKey("term.term_rid", ondelete="RESTRICT"),
        nullable=False
    )

    # ❗ NO cascade delete
    term = relationship("Term", back_populates="selfsames")


# =========================
# TERM SYNONYM
# =========================
class TermSynonym(Base):
    __tablename__ = "term_synonym"

    term_synonym_rid = Column(Integer, primary_key=True, index=True)
    term_synonym_id = Column(Text, nullable=False)
    turf_rid = Column(Integer, nullable=False)

    # business-key relationship (NOT FK)
    term_id = Column(Text, nullable=False)


# =========================
# USER (AUTH)
# =========================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
