-- Our first fixture, just to populate the database with a little data.

USE learnervoice;

-- Create a few schools
INSERT INTO schools (name) VALUES ("Lebogang High School"),("Riverside High School"),("Somewhere Preparatory");

-- Create some teachers
INSERT INTO teachers (name,surname,school_id) VALUES (
    "Angie",
    "Mabena",
    ( SELECT id FROM schools WHERE name="Lebogang High School" LIMIT 1 )
), (
    "Frikkie",
    "Motshekga",
    ( SELECT id FROM schools WHERE name="Riverside High School" LIMIT 1 )
), (
    "Carrie",
    "Anderson",
    ( SELECT id FROM schools WHERE name="Somewhere Preparatory" LIMIT 1 )
);

-- Create some learners
INSERT INTO learners (name,surname,school_id) VALUES (
    "Michael",
    "Motsepe",
    ( SELECT id FROM schools WHERE name="Lebogang High School" LIMIT 1 )
), (
    "Grace",
    "Nkosi",
    ( SELECT id FROM schools WHERE name="Riverside High School" LIMIT 1 )
);

-- Create some user accounts
INSERT INTO users (mobile,learner_id,teacher_id) VALUES (
    "0821231234",
    ( SELECT id FROM learners WHERE name="Michael" LIMIT 1 ),
    NULL
), (
    "0761231234",
    ( SELECT id FROM learners WHERE name="Grace" LIMIT 1 ),
    NULL
), (
    "0621231234",
    NULL,
    ( SELECT id FROM teachers WHERE name="Angie" LIMIT 1 )
);

