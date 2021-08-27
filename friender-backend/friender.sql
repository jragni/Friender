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
    description TEXT,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    zipcode TEXT NOT NULL,
    friend_radius INTEGER NOT NULL
  );

CREATE TABLE likes (
    from_id INTEGER NOT NULL,
    likes_id INTEGER NOT NULL
  );


CREATE TABLE rejections (
    from_id INTEGER NOT NULL,
    rejections_id INTEGER NOT NULL
  );

CREATE TABLE matches (
    id SERIAL,
    first_id INTEGER NOT NULL,
    second_id INTEGER NOT NULL
  );


CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    sender_id INTEGER NOT NULL,
    receiver_id INTEGER NOT NULL,
    timestamp TIMESTAMP NOT NULL
  );

