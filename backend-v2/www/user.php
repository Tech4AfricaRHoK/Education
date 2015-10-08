<?php
/**
 * Tech4Africa 2015 RHoK.
 *
 * User management API endpoint.
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
        array_push($teachers, array("id" => $row['id'],
            "name" => $row['name'],
            "surname" => $row['surname']));
    }
    return $teachers;
}


switch ($_SERVER['REQUEST_METHOD']) {
case "GET":
    if (!array_key_exists('schoolId', $_GET)) {
        error("Missing school ID in request", 400);
    }
    $query = array_key_exists('q', $_GET) ? $_GET['q'] : NULL;
    // fetch the teacher listing
    echo json_encode(listTeachers(intval($_GET['schoolId']), $query));
    break;
    
default:
    error("Unsupported method", 405);
}

?>
