angular.module('appRoutes', []).config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {

    $routeProvider

        // home page
        .when('/', {
            templateUrl: 'pages/auth/login.html',
            controller: 'LoginController'
        })
        
        // Login:
        
        .when('/login', {
            templateUrl: 'pages/auth/login.html',
            controller: 'LoginController'
        })
        
        // Registration:
        
        .when('/registration', {
            templateUrl: 'pages/auth/register.html',
            controller: 'RegistrationController'
        })
        
        // Recover Password:

        .when('/recover-password', {
            templateUrl: 'pages/auth/recover-password.html',
            controller: 'RecoverPasswordController'
        })
        
        // Recover Password:

        .when('/rate-my-teacher', {
            templateUrl: 'pages/teacher/rate.html',
            controller: 'RatingController'
        })
        

        //Teacher
        .when('/add-teacher', {
            templateUrl: 'pages/teacher/create-teacher.html',
            controller: 'AddTeacherController'
        })

        //School
        .when('/schools', {
            templateUrl: 'pages/school/schools.html',
            controller: 'SchoolController'
        })
        ;

    $locationProvider.html5Mode(true);

}]);