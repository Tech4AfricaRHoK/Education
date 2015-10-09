<?php
/**
 * Tech4Africa 2015 RHoK.
 *
 * Auth-related functionality.
 */

// assumes apibase.inc has been included prior to this file

/**
 * Attempts to get the user details from the current request.
 * For POC purposes, we just assume that the user ID is in the
 * "Authorization" header as a clear integer (obviously super
 * insecure, but allows us to show MVP quickly).
 *
 * TODO: Make this more secure. Perhaps JSON Web Tokens over SSL.
 *
 * @return The ID of the user for whom this request is relevant.
 */
function getUserFromRequest() {
    return array_key_exists('HTTP_AUTHORIZATION', $_SERVER) ? intval($_SERVER['HTTP_AUTHORIZATION']) : NULL;
}

?>
