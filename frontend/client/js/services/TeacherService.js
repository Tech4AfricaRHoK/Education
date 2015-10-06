angular.module('TeacherService', []).factory('Teacher', ['$http', function($http) {

    return {
		
        rateTeacher : function(data) {
            return $http.post('http://rateyourteacher.cloudapp.net/api/feedback/rating', data);
        },
		
        searchTeacher : function(data) {
            return $http.post('http://rateyourteacher.cloudapp.net/api/user', data);
        },
        
        session : function(data) {
            return $http.post('/authentication/session', data);
        }
		
    }       

}]);