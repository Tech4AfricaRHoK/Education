angular.module('appRoutes', []).config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {

    $routeProvider

        // home page
        .when('/', {
            templateUrl: 'index.html',
            controller: 'LoginController'
        })
        
        // Login:
        
        .when('/login', {
            templateUrl: 'index.html',
            controller: 'LoginController'
        })
        
        // Registration:
        
        .when('/registration', {
            templateUrl: 'pages/security/register.html',
            controller: 'RegistrationController'
        })
        
        .when('/recover-password', {
            templateUrl: 'pages/security/team-leaderboard.html',
            controller: 'LeaderboardController'
        })
        
        ;

    $locationProvider.html5Mode(true);

}]);