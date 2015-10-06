angular.module('TeacherService', []).factory('Teacher', ['$http', function($http) {

    return {
		
        rating : function(data) {
            return $http.post('http://localhost:8080/api/feedback/rating', data);
        },
		
        getAllTeachers : function(data) {
            return $http.post('http://localhost:8080/api/teacher/getAllTeachers', data);
        },
        
        session : function(data) {
            return $http.post('/authentication/session', data);
        }
		
    }       

}]);