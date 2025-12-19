CREATE TABLE term (
    term_rid SERIAL PRIMARY KEY,
    turf_rid INTEGER NOT NULL,
    term_id TEXT NOT NULL,
    language TEXT NOT NULL,
    country TEXT NOT NULL,
    term_name TEXT NOT NULL,
    term_description TEXT,
    term_acronym TEXT,
    is_machinized_name BOOLEAN DEFAULT FALSE,
    is_standardized_name BOOLEAN DEFAULT FALSE
);

CREATE TABLE term_selfsame (
    term_selfsame_rid SERIAL PRIMARY KEY,
    term_selfsame_id TEXT NOT NULL,
    turf_rid INTEGER NOT NULL,
    term_rid INTEGER NOT NULL,
    CONSTRAINT fk_selfsame_term
        FOREIGN KEY (term_rid)
        REFERENCES term(term_rid)
        ON DELETE RESTRICT
);

CREATE TABLE term_synonym (
    term_synonym_rid SERIAL PRIMARY KEY,
    term_synonym_id TEXT NOT NULL,
    turf_rid INTEGER NOT NULL,
    term_id TEXT NOT NULL
);








