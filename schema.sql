CREATE TABLE IF NOT EXISTS term (
  term_rid SERIAL PRIMARY KEY,
   
  turf_rid INTEGER NOT NULL,
  term_id TEXT NOT NULL,
  language TEXT,
  country TEXT,
  term_name TEXT,
  term_description TEXT,
  term_acronym TEXT,
  is_machinized_name BOOLEAN DEFAULT FALSE,
  is_standardized_name BOOLEAN DEFAULT FALSE,
  UNIQUE (turf_rid, term_id)
);


CREATE TABLE IF NOT EXISTS term_selfsame (
  term_selfsame_rid SERIAL PRIMARY KEY,
  term_selfsame_id TEXT NOT NULL,
  turf_rid INTEGER NOT NULL,
  term_rid INTEGER NOT NULL,
  FOREIGN KEY (term_rid) REFERENCES term(term_rid)
);

CREATE TABLE IF NOT EXISTS term_synonym (
  term_synonym_rid SERIAL PRIMARY KEY,
  term_synonym_id TEXT NOT NULL,
  turf_rid INTEGER NOT NULL,
  term_rid INTEGER NOT NULL,
  FOREIGN KEY (term_rid) REFERENCES term(term_rid)
);