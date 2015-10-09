-- First version of the database

-- First set up the database and user access
CREATE DATABASE IF NOT EXISTS learnervoice;
GRANT ALL ON learnervoice.* to 'learnervoice'@'localhost' IDENTIFIED BY 'learnervoice';

USE learnervoice;

-- Create our tables
CREATE TABLE IF NOT EXISTS schools (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,

    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS teachers (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    school_id INT NOT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(school_id) REFERENCES schools(id),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS learners (
    id BIGINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    school_id INT NOT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(school_id) REFERENCES schools(id),
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS users(
    id BIGINT NOT NULL AUTO_INCREMENT,
    mobile VARCHAR(30) NOT NULL UNIQUE,
    learner_id BIGINT DEFAULT NULL,
    teacher_id INT DEFAULT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(learner_id) REFERENCES learners(id),
    FOREIGN KEY(teacher_id) REFERENCES teachers(id),
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS teacher_ratings (
    id BIGINT NOT NULL AUTO_INCREMENT,
    teacher_id INT NOT NULL,
    learner_id BIGINT NOT NULL,
    rating INT NOT NULL,
    comments TEXT DEFAULT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(teacher_id) REFERENCES teachers(id),
    FOREIGN KEY(learner_id) REFERENCES learners(id),
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS incidents (
    id BIGINT NOT NULL AUTO_INCREMENT,
    teacher_id INT NOT NULL,
    learner_id BIGINT NOT NULL,
    description TEXT NOT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(teacher_id) REFERENCES teachers(id),
    FOREIGN KEY(learner_id) REFERENCES learners(id),
    PRIMARY KEY(id)
);



