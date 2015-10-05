angular.module('LoginCtrl', []).controller('LoginController', function($scope, $http, $window, Authentication) {

    $scope.loginData = {
        username: "",
        password: ""
    };
    
   // $('#loginForm').parsley();
    
    $scope.steam = function(){
        $window.location.href = '/auth/steam';
    }
    
    // Authenticate user
    $scope.login = function(){        
        Authentication.login(JSON.stringify($scope.loginData))
        .success(function(data){
            $scope.loginFormData = {};
            $scope.user = data;
            console.log(data);
            
            // Create session for the user from response
            Authentication.session(JSON.stringify(data))
            .success(function(data){
                $window.location.href = '/school/ratemyteacher';
            })
            .error(function(data){
                $window.location.href = '/registration';
            });  
                      
        })
        .error(function(data){
            $window.location.href = '/registration';
        });
    };
    
});