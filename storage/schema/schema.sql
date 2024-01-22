BEGIN;

CREATE TABLE Author
(
    id         SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name  VARCHAR,
    UNIQUE (first_name, last_name)
);

CREATE TABLE Source
(
    id        SERIAL PRIMARY KEY,
    name      VARCHAR                    NOT NULL,
    author_id INT REFERENCES Author (id) NOT NULL,
    year      INT                        NOT NULL,
    UNIQUE (name, author_id, year)
);

CREATE TABLE Quote
(
    id        SERIAL PRIMARY KEY,
    text      VARCHAR                    NOT NULL,
    source_id INT REFERENCES Source (id) NOT NULL,
    UNIQUE (text, source_id)
);

CREATE TABLE User
(
    id      SERIAL PRIMARY KEY,
    user_id INT NOT NULL UNIQUE,
);

CREATE TABLE Subscription
(
    id                 SERIAL PRIMARY KEY,
    user_id            INT REFERENCES User (id) NOT NULL UNIQUE,
    last_seen_quote_id INT                      NOT NULL DEFAULT -1,
);

COMMIT;