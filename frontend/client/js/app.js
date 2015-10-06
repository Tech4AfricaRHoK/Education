angular.module('RateMyTeacherApp', [
	'ngRoute', 
	'appRoutes', 
	
	// Controllers: 
	
	'LoginCtrl',
	'RegistrationCtrl',
	'RecoverPasswordCtrl',
	'RatingCtrl',
	
	// Services: 
	
	'AuthenticationService',

	'TeacherService'
	// Directives: 
	//'RatingDrtv'
	
]);