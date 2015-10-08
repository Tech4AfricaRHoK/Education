<?php
/**
 * Tech4Africa 2015 RHoK.
 *
 * User management API endpoint.
 *
 * TODO: Mobile number validation when users sign up.
 */
include "apibase.inc";

/**
 * Lists all of the available teachers.
 */
function listTeachers($schoolId, $query = NULL) {
    global $db;

    if ($query == NULL) {
        $stmt = $db->prepare('SELECT id,name,surname FROM teachers WHERE school_id=?');
    } else {
        $query = trim($db->quote(strtoupper($query)), "'");
        $stmt = $db->prepare('SELECT id,name,surname FROM teachers WHERE school_id=? AND (UPPER(name) LIKE "%'.$query.'%" OR UPPER(surname) LIKE "%'.$query.'%")');
    }
    $stmt->execute(array($schoolId));
    $result = $stmt->fetchAll();
    $teachers = array();
    // get all of the results
    foreach ($result as $row) {
        array_push($teachers, array("id" => intval($row['id']),
            "name" => $row['name'],
            "surname" => $row['surname']));
    }
    return $teachers;
}

/**
 * Attempts to retrieve the user with the given mobile number.
 *
 * @return An array containing the user's data on success, or NULL on failure.
 */
function getUserByMobile($mobile) {
    global $db;

    $stmt = $db->prepare('SELECT id,mobile,learner_id,teacher_id,created,password FROM users WHERE mobile=?');
    $stmt->execute(array($mobile));
    $results = $stmt->fetchAll();
    if ($stmt->rowCount() == 0) {
        return NULL;
    }
    return $results[0];
}

/**
 * Non-transactional function to create a new user. Either $learner_id or
 * $teacher_id must be specified.
 */
function createUser($mobile, $password, $learner_id = NULL, $teacher_id = NULL) {
    global $db;

    // if the user already exists
    if (getUserByMobile($mobile) != NULL) {
        return NULL;
    }

    // compute the hash of the password
    $passwordHash = hash("sha256", $password);

    if ($learner_id != NULL) {
        $stmt = $db->prepare('INSERT INTO users (mobile,password,learner_id) VALUES (?, ?, ?)');
        $stmt->execute(array($mobile, $passwordHash, $learner_id));
    } else {
        $stmt = $db->prepare('INSERT INTO users (mobile,password,teacher_id) VALUES (?, ?, ?)');
        $stmt->execute(array($mobile, $passwordHash, $teacher_id));
    }

    return getUserByMobile($mobile);
}


function getLearnerByMobile($mobile) {
    global $db;

    // see if there's a user by that mobile number
    $user = getUserByMobile($mobile);
    if ($user == NULL) {
        return NULL;
    }

    $stmt = $db->prepare('SELECT id,name,surname,school_id,created FROM learners WHERE id=?');
    $stmt->execute(array($user['learner_id']));
    $results = $stmt->fetchAll();

    // no such learner
    if ($stmt->rowCount() == 0) {
        return NULL;
    }

    $learner = $results[0];

    return array('user_id' => $user['id'],
        'mobile' => $user['mobile'],
        'learner_id' => intval($user['learner_id']),
        'name' => $learner['name'],
        'surname' => $learner['surname'],
        'school_id' => intval($learner['school_id']),
        'created' => $learner['created']);
}

/**
 * Creates a new learner in the system (learner and user).
 */
function createLearner($name, $surname, $mobile, $password, $schoolId) {
    global $db;

    // if a user with that mobile number already exists
    if (getUserByMobile($mobile) != NULL) {
        return NULL;
    }

    // try to create the learner first
    $stmt = $db->prepare('INSERT INTO learners (name,surname,school_id) VALUES (?,?,?)');
    $stmt->execute(array($name,$surname,$schoolId));
    $learnerId = $db->lastInsertId();

    // now try to create the user
    $user = createUser($mobile, $password, $learnerId);

    return getLearnerByMobile($mobile);
}

/**
 * Attempts to validate the given mobile number.
 *
 * TODO: Improve this algorithm substantially :-)
 */
function validateMobile($mobile) {
    return (strlen($mobile) < 10) ? false : true;
}


switch ($_SERVER['REQUEST_METHOD']) {
case "GET":
    if (!array_key_exists('schoolId', $_GET)) {
        error("Missing school ID in request", 400);
    }
    $query = array_key_exists('t', $_GET) ? $_GET['t'] : NULL;
    // fetch the teacher listing
    echo json_encode(listTeachers(intval($_GET['schoolId']), $query));
    break;

case "POST":
    $body = json_parse_request_body();
    if (!array_key_exists('type', $body)) {
        error("Missing user type indicator in request", 400);
    }
    if ($body['type'] == 'learner') {
        // the required fields for our message body
        $requiredFields = array('name', 'surname', 'mobile', 'password', 'schoolId');
        if (count(array_intersect_key(array_flip($requiredFields), $body)) != count($requiredFields)) {
            error("One or more missing field(s) in incoming request", 400);
        }
        if (!validateMobile($body['mobile'])) {
            error("Invalid mobile phone number", 400);
        }
        $learner = createLearner($body['name'],
            $body['surname'],
            $body['mobile'],
            $body['password'],
            $body['schoolId']);
        if ($learner == NULL) {
            error("Learner with that mobile number already exists", 400);
        }
        echo json_encode($learner);
    } else {
        error("Unsupported user type", 400);
    }
    break;
    
default:
    error("Unsupported method", 405);
}

?>
