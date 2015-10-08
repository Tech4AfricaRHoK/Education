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

function json_parse_request_body() {
    // decode the incoming JSON
    try {
        $body = json_decode(file_get_contents('php://input'), true);
    } catch (Exception $e) {
        error("Invalid message body", 400);
    }
    return $body;
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
