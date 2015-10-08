<?php
/**
 * Tech4Africa 2015 RHoK.
 * Our primary (hacky) API. Built quickly as a proof-of-concept.
 */
// we want JSON on the output - regardless of what we throw out
header('Content-Type: application/json');

echo json_encode(array("message" => $_GET['path']));
?>
