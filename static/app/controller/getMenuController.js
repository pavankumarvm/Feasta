/*
feasta menu controller
*/

feasta.controller("getMenuController", ['$scope', '$http', '$location', function ($scope, $http, $location) {

    var id = $location.search().messid; // get mess_id from url

    $scope.Mess = {}
    $http.get("/api/v1/get-mess/" + id + '/')
        .success(function (data) {
            $scope.Mess = data;
            console.log(data);
        })
        .error(function (data, status, value) {
            console.log("error occured");
        })


    $scope.Menu = {};
    $http.get("/api/v1/get-menu/" + id + '/')
        .success(function (data) {
            $scope.Menu = data;
            console.log(data);
        })
        .error(function (status) {
            console.log(status);
        })
}])
