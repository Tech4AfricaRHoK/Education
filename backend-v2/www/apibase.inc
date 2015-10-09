<?php
/**
 * Tech4Africa 2015 RHoK.
 * Our primary (hacky) API code. Built quickly as a proof-of-concept.
 */
// we want JSON on the output - regardless of what we throw out
header('Content-Type: application/json');

/**
 * Basic error handling.
 * @param $msg The error message to send back to the client.
 * @param $code The HTTP status code to use.
 */
function error($msg, $code) {
    http_response_code($code);
    die(json_encode(array("error" => $msg)));
}

/**
 * For sending back a simple JSON message (mainly for debugging).
 * @param $msg The text of the message to send back.
 */
function message($msg) {
    echo json_encode(array("message" => $msg));
}

/**
 * Returns a parsed version of the request body (assuming it's JSON).
 */
function json_parse_request_body() {
    // decode the incoming JSON
    try {
        $body = json_decode(file_get_contents('php://input'), true);
    } catch (Exception $e) {
        error("Invalid message body", 400);
    }
    return $body;
}

function getUserById($userId) {
    global $db;

    $stmt = $db->prepare('SELECT id,mobile,learner_id,teacher_id,created,password FROM users WHERE id=?');
    $stmt->execute(array($userId));
    $results = $stmt->fetchAll();
    // no such user?
    if ($stmt->rowCount() == 0) {
        return NULL;
    }

    return array('id' => $results[0]['id'],
        'mobile' => $results[0]['mobile'],
        'learnerId' => $results[0]['learner_id'],
        'teacherId' => $results[0]['teacher_id'],
        'created' => $results[0]['created'],
        'password' => $results[0]['password']);
}

function getTeacherById($teacherId) {
    global $db;

    $stmt = $db->prepare('SELECT id,name,surname,school_id,created FROM teachers WHERE id=?');
    $stmt->execute(array($teacherId));
    if ($stmt->rowCount() == 0) {
        return NULL;
    }

    $teacher = $stmt->fetchAll()[0];
    return array('id' => $teacher['id'],
        'name' => $teacher['name'],
        'surname' => $teacher['surname'],
        'schoolId' => $teacher['school_id'],
        'created' => $teacher['created']);
}

function getLearnerById($learnerId, $withUser = NULL) {
    global $db;

    $stmt = $db->prepare('SELECT id,name,surname,school_id,created FROM learners WHERE id=?');
    $stmt->execute(array($learnerId));
    $results = $stmt->fetchAll();

    // no such learner
    if ($stmt->rowCount() == 0) {
        return NULL;
    }

    $result = $results[0];
    $learner = array('id' => $learnerId,
        'name' => $result['name'],
        'surname' => $result['surname'],
        'schoolId' => $result['school_id'],
        'created' => $result['created']);

    if ($withUser != NULL) {
        $learner = array_merge($learner, array('userId' => $withUser['id'],
            'mobile' => $withUser['mobile'],
            'password' => $withUser['password']));
    }

    return $learner;
}

$mysql_server = "localhost";
$mysql_database = "learnervoice";
$mysql_user = "learnervoice";
$mysql_password = "learnervoice";

// connect to MySQL
try {
    $db = new PDO("mysql:host=$mysql_server;dbname=$mysql_database", $mysql_user, $mysql_password);
} catch (PDOException $e) {
    error("MySQL connection failed: $e->getMessage()", 500);
}

?>
