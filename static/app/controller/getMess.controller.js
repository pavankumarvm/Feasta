/*
feasta Mess controller, use to display
all mess
*/

feasta.controller('getMess', ['$scope', '$http', '$location', 'Authentication', function ($scope, $http, $location, Authentication) {
    $scope.Mess = {};

    $scope.isAuthenticated = Authentication.isAuthenticated();
    $scope.logout = logout;

    $http.get("/api/v1/get-mess/", )
        .success(function (data) {
            $scope.Mess = data;
            console.log(data);
        })
        .error(function (data, status, value) {
            console.log("error occured");
        })

    function logout(){
        Authentication.logout();
        $location.path('/home');
    }
}]);
