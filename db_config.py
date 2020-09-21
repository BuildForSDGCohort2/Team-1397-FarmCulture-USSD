
#create farmcultureappdb database
CREATE DATABASE farmculturedb;

#create table category
CREATE TABLE product_category(
	id SERIAL CONSTRAINT pcategory_pk PRIMARY KEY,
	name VARCHAR(150) NOT NULL UNIQUE
	);

#create table product
CREATE TABLE product(
	id SERIAL CONSTRAINT product_pk PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	scientific_name VARCHAR(150) NULL,

	);

#create table howto
CREATE TABLE howto(
	id SERIAL CONSTRAINT howto_pk PRIMARY KEY,
	product_id INT CONSTRAINT howto_fk FOREIGN KEY REFERENCES product(id),
	title VARCHAR(100),
	procedure VARCHAR(500)
	);

