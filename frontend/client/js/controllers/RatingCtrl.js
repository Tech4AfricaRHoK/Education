angular.module('RatingCtrl', []).controller('RatingController', function($scope, $http, $window) {
        
    var ratingC = this;
    $scope.rateFunction = function( rating )
{
       var _url = 'your service url';
 
 var data = {
   rating: rating
 };
 
 $http.post( _url, angular.toJson(data), {cache: false} )
  .success( function( data )
  {
   success(data);
  })
  .error(function(data){
    error(data);
  });
 
};

// Search Teacher
    ratingC.searchTeacher = function(){  
        //$window.location.href = '/rate-my-teacher';      
        Authentication.searchTeacher(JSON.stringify($scope.loginData))
        .success(function(data){
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
                      
        })
        .error(function(data){
            //$window.location.href = '/registration';
        });
    };

// Rate Teacher
    ratingC.rateTeacher = function(){  
        //$window.location.href = '/rate-my-teacher';      
        Authentication.rateTeacher(JSON.stringify($scope.loginData))
        .success(function(data){
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
                      
        })
        .error(function(data){
            //$window.location.href = '/registration';
        });
    };
    
});