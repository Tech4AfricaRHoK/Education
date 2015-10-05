angular.module('appRoutes', []).config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {

    $routeProvider

        // home page
        .when('/', {
            templateUrl: 'pages/login.html',
            controller: 'LoginController'
        })
        
        // Login:
        
        .when('/login', {
            templateUrl: 'pages/login.html',
            controller: 'LoginController'
        })
        
        // Registration:
        
        .when('/registration', {
            templateUrl: 'pages/register.html',
            controller: 'RegistrationController'
        })
        
        .when('/recover-password', {
            templateUrl: 'pages/recover-password.html',
            controller: 'RecoverPasswordController'
        })
        
        ;

    $locationProvider.html5Mode(true);

}]);