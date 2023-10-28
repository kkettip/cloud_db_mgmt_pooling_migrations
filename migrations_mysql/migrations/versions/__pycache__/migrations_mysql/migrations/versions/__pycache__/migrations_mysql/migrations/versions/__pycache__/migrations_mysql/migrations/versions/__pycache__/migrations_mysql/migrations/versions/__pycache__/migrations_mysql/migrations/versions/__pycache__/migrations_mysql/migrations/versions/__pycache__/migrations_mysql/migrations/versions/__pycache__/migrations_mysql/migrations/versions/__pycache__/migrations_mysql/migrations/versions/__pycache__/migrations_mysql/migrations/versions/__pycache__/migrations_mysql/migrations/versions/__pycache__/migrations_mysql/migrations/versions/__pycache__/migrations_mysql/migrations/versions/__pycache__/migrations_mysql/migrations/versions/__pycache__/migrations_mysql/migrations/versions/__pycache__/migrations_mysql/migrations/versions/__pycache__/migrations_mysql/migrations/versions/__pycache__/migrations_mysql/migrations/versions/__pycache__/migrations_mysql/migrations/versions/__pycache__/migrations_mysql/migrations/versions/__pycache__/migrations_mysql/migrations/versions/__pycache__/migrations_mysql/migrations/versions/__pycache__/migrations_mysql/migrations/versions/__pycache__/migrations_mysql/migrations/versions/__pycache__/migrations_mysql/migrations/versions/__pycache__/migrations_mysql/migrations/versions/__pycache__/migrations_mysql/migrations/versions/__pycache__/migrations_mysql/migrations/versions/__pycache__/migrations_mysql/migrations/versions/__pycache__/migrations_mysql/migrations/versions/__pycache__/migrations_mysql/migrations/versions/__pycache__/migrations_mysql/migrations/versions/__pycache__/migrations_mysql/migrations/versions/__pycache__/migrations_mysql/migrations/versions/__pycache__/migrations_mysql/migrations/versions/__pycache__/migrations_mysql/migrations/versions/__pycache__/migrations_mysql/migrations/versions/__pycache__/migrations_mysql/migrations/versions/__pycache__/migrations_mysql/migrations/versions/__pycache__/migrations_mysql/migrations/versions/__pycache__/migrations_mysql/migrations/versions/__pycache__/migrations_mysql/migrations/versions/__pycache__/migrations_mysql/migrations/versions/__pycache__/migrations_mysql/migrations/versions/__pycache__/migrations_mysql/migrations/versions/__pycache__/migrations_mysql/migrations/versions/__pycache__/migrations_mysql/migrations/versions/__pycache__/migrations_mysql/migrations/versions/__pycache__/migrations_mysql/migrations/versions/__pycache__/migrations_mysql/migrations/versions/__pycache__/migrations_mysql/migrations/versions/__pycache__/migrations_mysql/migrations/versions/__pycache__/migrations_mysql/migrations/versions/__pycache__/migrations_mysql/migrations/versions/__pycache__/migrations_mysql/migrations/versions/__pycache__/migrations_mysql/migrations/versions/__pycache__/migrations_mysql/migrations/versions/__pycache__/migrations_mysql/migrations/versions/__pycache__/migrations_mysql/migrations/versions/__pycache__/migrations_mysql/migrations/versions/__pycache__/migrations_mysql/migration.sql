CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> f5e3a52104ab

ALTER TABLE patients MODIFY contact_number VARCHAR(100) NULL;

INSERT INTO alembic_version (version_num) VALUES ('f5e3a52104ab');

-- Running upgrade f5e3a52104ab -> d9061947fd56

UPDATE alembic_version SET version_num='d9061947fd56' WHERE alembic_version.version_num = 'f5e3a52104ab';

