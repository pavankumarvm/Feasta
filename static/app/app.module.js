var feasta = angular.module("feasta", ['ngRoute', 'ngCookies'])

feasta.constant('BASE_URL', "http://localhost:3000/api/v1/");


feasta.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
    $locationProvider.html5Mode(true);

    $routeProvider
        .when('/', {
            templateUrl: "static/app/app-template/index.html"
        })
        .when('/home/', {
            title: 'Home',
            templateUrl: "static/app/app-template/home.html",
            controller: "getMess"
        })
        .when('/menu/', {
            templateUrl: "static/app/app-template/menu.html",
            controller: "getMenu"
        })
        .when('/profile/:username',{
            templateUrl: "static/app/app-template/profile.html",
            controller: "getProfile",
            controllerAs: "vm",
        })
        .when('/login/',{
            templateUrl: "static/app/app-template/login.html",
            controller: "loginUser",
            controllerAs: "vm",
        })
        .when('/signup/',{
            templateUrl: "static/app/app-template/register.html",
            controller: "registerUser",
            controllerAs: "vm",
        })
    // .otherwise('/', {
    //     redirectTo: "/"
    // })

}]);

feasta.run(['$http', function($http){
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
}])


// feasta.run(['$rootScope', function ($rootScope) {
//     $rootScope.$on('$routeChangeSuccess', function (event, current, previous) {
//         $rootScope.title = current.$$route.title;
//     })

// }])
