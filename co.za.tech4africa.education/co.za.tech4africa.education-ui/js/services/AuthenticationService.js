angular.module('AuthenticationService', []).factory('Authentication', ['$http', function($http) {

    return {
		
        login : function(data) {
            return $http.post('http://localhost:8080/RateMyTeacherRestResource/path/to/login', data);
        },
		
        register : function(data) {
            return $http.post('http://localhost:8080/RateMyTeacherRestResource/path/to/register', data);
        },
        
        session : function(data) {
            return $http.post('/authentication/session', data);
        }
		
    }       

}]);