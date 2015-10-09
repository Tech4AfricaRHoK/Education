<?php
/**
 * Tech4Africa 2015 RHoK.
 *
 * Allows us to rate teachers.
 */
include "../apibase.inc";
include "../auth.inc";


/**
 * Helps with getting the average rating for the specified teacher.
 *
 * TODO: Take into account timeframes, like school years, etc.
 */
function getTeacherAvgRating($teacherId) {
    global $db;

    $stmt = $db->prepare('SELECT AVG(rating) as avg_rating, COUNT(*) as rating_count FROM teacher_ratings WHERE teacher_id=?');
    $stmt->execute(array($teacherId));
    // no results
    if ($stmt->rowCount() == 0) {
        return NULL;
    }

    $result = $stmt->fetchAll()[0];

    return array('id' => $teacherId,
        'count' => intval($result['rating_count']),
        'avgRating' => round(floatval($result['avg_rating']), 2));
}

/**
 * Rates the given teacher.
 */
function rateTeacher($learnerUserId, $teacherId, $rating, $comment = NULL) {
    global $db;

    // try to find the learner with the given user ID
    $user = getUserById($learnerUserId);
    if ($user === NULL) {
        error("The specified user does not exist in the database", 400);
    }

    // get the learner's details
    $learner = getLearnerById($user['learnerId'], $user);
    if ($learner == NULL) {
        error("The specified user does not have a learner associated with them", 400);
    }

    // try to find the teacher
    $teacher = getTeacherById($teacherId);
    if ($teacher == NULL) {
        error("The specified teacher does not exist in the database", 400);
    }

    // check that they're from the same school
    if ($teacher['schoolId'] != $learner['schoolId']) {
        error("Teacher and learner are not at the same school", 400);
    }

    $stmt = $db->prepare('INSERT INTO teacher_ratings (teacher_id,learner_id,rating,comments) VALUES (?,?,?,?)');
    $stmt->execute(array($teacher['id'], $learner['id'], $rating, $comment));

    // return the average rating for that teacher
    return getTeacherAvgRating($teacherId);
}


switch ($_SERVER['REQUEST_METHOD']) {
case "GET":
    $userId = getUserFromRequest();
    if ($userId == NULL) {
        error("Unauthorized", 401);
    }

    if (!array_key_exists("teacherId", $_GET)) {
        error("Missing teacherId parameter in request", 400);
    }
    $rating = getTeacherAvgRating($_GET['teacherId']);
    echo json_encode($rating);
    break;

case "POST":
    $userId = getUserFromRequest();
    if ($userId === NULL) {
        error("Unauthorized", 401);
    }
    $body = json_parse_request_body();
    $requiredFields = array('teacherId', 'value');
    if (count(array_intersect_key(array_flip($requiredFields), $body)) != count($requiredFields)) {
        error("One or more missing field(s) in incoming request", 400);
    }
    $teacherId = intval($body['teacherId']);
    $ratingValue = intval($body['value']);
    if ($ratingValue < 1 || $ratingValue > 5) {
        error("Rating value must be an integer value between 1 and 5", 400);
    }
    $comment = array_key_exists('comment', $body) ? $body['comment'] : NULL;
    $rating = rateTeacher($userId, $teacherId, $ratingValue, $comment);
    echo json_encode($rating);
    break;

default:
    error("Unsupported method", 405);
}
?>
