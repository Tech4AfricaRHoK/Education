<?php
/**
 * Tech4Africa 2015 RHoK.
 *
 * School management API endpoint.
 */
include "apibase.inc";

/**
 * Provides a listing of the available schools.
 */
function listSchools($query = NULL) {
    global $db;

    if ($query == NULL) {
        $result = $db->query('SELECT id,name FROM schools');
    } else {
        $query = trim($db->quote(strtoupper($query)), "'");
        $result = $db->query('SELECT id,name FROM schools WHERE UPPER(name) LIKE "%'.$query.'%"');
    }
    $schools = array();

    foreach ($result as $row) {
        array_push($schools, array("id" => $row['id'],
            "name" => $row['name']));
    }

    return $schools;
}

function getSchoolByName($name) {
    global $db;

    $stmt = $db->prepare('SELECT id FROM schools WHERE name=?');
    $stmt->execute(array($name));
    if ($stmt->rowCount() == 0) {
        // no such school
        return NULL;
    }

    // just get the first one
    return array('id' => $stmt->fetchAll()[0]['id']);
}

/**
 * Assists in creating a school with the given name.
 * @param $name The name of the school to create.
 */
function createSchool($name) {
    global $db;

    // first check that the school with the given name doesn't exist yet
    if (getSchoolByName($name) != NULL) {
        return NULL;
    }

    $stmt = $db->prepare('INSERT INTO schools (name) VALUES (?)');
    $stmt->execute(array($name));

    return getSchoolByName($name);
}


switch ($_SERVER['REQUEST_METHOD']) {
case "GET":
    $query = array_key_exists('q', $_GET) ? $_GET['q'] : NULL;
    echo json_encode(listSchools($query));
    break;

case "POST":
    // decode the incoming JSON
    try {
        $body = json_decode(file_get_contents('php://input'));
    } catch (Exception $e) {
        error("Invalid message body", 400);
    }
    // try to extract the name
    if (!array_key_exists('name', $body)) {
        error("Missing school name in request", 400);
    }
    $result = createSchool($body['name']);
    if ($result == NULL) {
        error("School by that name already exists", 400);
    }
    echo json_encode($result);
    break;

default:
    error("Unsupported method", 405);
}

?>
