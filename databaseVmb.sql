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

-- DROP TABLE "vmbSchema"."Origin";

CREATE TABLE "vmbSchema"."Origin"
(
  id integer generated always as identity,
  name text,
  CONSTRAINT pk_origin PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "vmbSchema"."Origin"
  OWNER TO "vmbUser";

-- DROP TABLE "vmbSchema"."Unity";

CREATE TABLE "vmbSchema"."Unity"
(
  id integer generated always as identity,
  name text,
  CONSTRAINT pk_unity PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "vmbSchema"."Unity"
  OWNER TO "vmbUser";

  -- DROP TABLE "vmbSchema"."Product";

CREATE TABLE "vmbSchema"."Product"
(
  id integer generated always as identity,
  name text,
  url text,
  price money,
  date date DEFAULT now(),
  imageName text,
  category text,
  idUnity integer,
  idOrigin integer,
  CONSTRAINT pk_product PRIMARY KEY (id),
  CONSTRAINT fk_product_unity FOREIGN KEY (idUnity) REFERENCES "vmbSchema"."Unity"(id),  
  CONSTRAINT fk_product_origin FOREIGN KEY (idOrigin) REFERENCES "vmbSchema"."Origin"(id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "vmbSchema"."Product"
  OWNER TO "vmbUser";

insert into "vmbSchema"."Origin" (name) values ('Pingo Doce');
insert into "vmbSchema"."Origin" (name) values ('Continente');
insert into "vmbSchema"."Origin" (name) values ('Mini Preço');
insert into "vmbSchema"."Origin" (name) values ('Lidl');
insert into "vmbSchema"."Origin" (name) values ('Audi');