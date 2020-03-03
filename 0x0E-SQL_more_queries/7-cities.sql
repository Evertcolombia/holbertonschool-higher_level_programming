-- create database if  not exist and table if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	UNIQUE(id),
	PRIMARY KEY(id),
	FOREIGN KEY (id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL);
