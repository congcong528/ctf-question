DROP TABLE IF EXISTS credentials;

CREATE TABLE credentials(
    username VARCHAR(20) PRIMARY KEY,
    password VARCHAR(20) NOT NULL
);

INSERT INTO credentials VALUES ('MrHacker', 'H@x0RPW');

