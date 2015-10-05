angular.module('RecoverPasswordCtrl', []).controller('RecoverPasswordController', function($scope, $http, $window, Authentication) {

    $scope.registrationData = {
        cellno: ""
    };
    
    $('#recoverPasswordForm').parsley();    
    
    // Authenticate user
    $scope.recoverPassword = function(){        
        Authentication.recoverPassword(JSON.stringify($scope.recoverPasswordData))
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