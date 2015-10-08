-- Adding a password field to the users table

USE learnervoice;

ALTER TABLE users ADD COLUMN password VARCHAR(255) DEFAULT NULL;

