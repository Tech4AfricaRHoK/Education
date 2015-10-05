angular.module('RegistrationCtrl', []).controller('RegistrationController', function($scope, $http, $window, Authentication) {

    $scope.registrationData = {
        name: "",
        surname: "",
        email: "",
        password: "",
        cellno: ""
    };
    
    $('#registrationForm').parsley();    
    
    // Authenticate user
    $scope.register = function(){        
        Authentication.register(JSON.stringify($scope.registrationData))
        .success(function(data){
            $scope.registrationData = {};
            $scope.user = data;
            console.log(data);
            $window.location.href = '/school/ratemyteacher';
            
            // Create session for the user from response
            Authentication.session(JSON.stringify(data))
            .success(function(data){
                
            })
            .error(function(data){
                
            });  
                      
        })
        .error(function(data){
            console.log('Error: ' + data);
        });
    };
    
});