-- Role: vmbUser

-- DROP ROLE "vmbUser";

CREATE ROLE "vmbUser" LOGIN
  ENCRYPTED PASSWORD 'md59e70d7d5a1f4379e5a51ec8281230199'
  SUPERUSER INHERIT NOCREATEDB CREATEROLE NOREPLICATION;

- Database: vmb_db

-- DROP DATABASE vmb_db;

CREATE DATABASE vmb_db
  WITH OWNER = "vmbUser"
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'en_US.UTF-8'
       LC_CTYPE = 'en_US.UTF-8'
       CONNECTION LIMIT = -1;

-- Schema: vmbSchema

-- DROP SCHEMA "vmbSchema";

CREATE SCHEMA "vmbSchema"
  AUTHORIZATION "vmbUser";
-- Table: "vmbSchema"."ResultadoCrawler"

-- DROP TABLE "vmbSchema"."ResultadoCrawler";

CREATE TABLE "vmbSchema"."ResultadoCrawler"
(
  id integer generated always as identity,
  origin text,
  url text,
  product text,
  price text,
  unit text,
  category text,
  CONSTRAINT pk PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "vmbSchema"."ResultadoCrawler"
  OWNER TO "vmbUser";
