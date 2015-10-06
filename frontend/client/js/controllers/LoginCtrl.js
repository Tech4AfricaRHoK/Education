angular.module('LoginCtrl', []).controller('LoginController', function($scope, $http, $window, Authentication) {
    var loginC = this;
    $scope.loginData = {
        username: "",
        password: ""
    };
    
   // $('#loginForm').parsley();
    
    $scope.steam = function(){
        $window.location.href = '/auth/steam';
    }
    
    // Authenticate user
    loginC.login = function(){  
        $window.location.href = '/rate-my-teacher';      
        //Authentication.login(JSON.stringify($scope.loginData))
        //.success(function(data){
        //    $scope.loginFormData = {};
        //    $scope.user = data;
        //    console.log(data);
            
            // Create session for the user from response
        //    Authentication.session(JSON.stringify(data))
        //    .success(function(data){
        //        $window.location.href = '/school/ratemyteacher';
        //    })
        //    .error(function(data){
        //        $window.location.href = '/registration';
        //    });  
                      
        //})
        //.error(function(data){
        //    $window.location.href = '/registration';
        //});
    };
    
});