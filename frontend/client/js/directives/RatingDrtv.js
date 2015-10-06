angular.module('RatingCtrl').directive('starRating',
function() {
return {
restrict : 'A',
template : '<ul class="rating">'
   + ' <span ng-repeat="star in stars" ng-class="star" ng-click="toggle($index)">'
   + '  <span class="glyphicon glyphicon-star-empty"></span>'
   + ' </span>'
   + '</ul>',
scope : {
 ratingValue : '=',
 max : '=',
 onRatingSelected : '&'
},
link : function(scope, elem, attrs) {
 var updateStars = function() {
  scope.stars = [];
  for ( var i = 0; i < scope.max; i++) {
   scope.stars.push({
    filled : i < scope.ratingValue
   });
  }
 };
 
 scope.toggle = function(index) {
  scope.ratingValue = index + 1;
  scope.onRatingSelected({
   rating : index + 1
  });
 };
 
 scope.$watch('ratingValue',
  function(oldVal, newVal) {
   if (newVal) {
    updateStars();
   }
  }
 );
}
};
}
);