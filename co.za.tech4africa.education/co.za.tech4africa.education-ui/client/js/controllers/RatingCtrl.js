angular.module('RatingCtrl', []).controller('RatingController', function($scope, $http, $window) {
        

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
    
});