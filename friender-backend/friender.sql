\echo 'Delete and recreate lunchly db?'
\prompt 'Return for yes or control-C to cancel > ' 

DROP DATABASE IF EXISTS friender;
CREATE DATABASE friender;
\connect friender;


-- CREATE TABLE users (

--     )

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
  );