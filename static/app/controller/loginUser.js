
feasta.controller("loginUser", ['$location', '$scope', 'Authentication' ,function($location, $scope, Authentication){
    var vm = this;
    vm.login = login;

    if_active();

    function if_active(){
        // If the User is Authenticated then they must be redirected to profile page.
        if(Authentication.isAuthenticated()){
            console.log("User has logged in");
            $location.path('/profile/' + vm.username + '/');
        }
    }

    function login(){
        // console.log(vm);
        Authentication.login(vm.username, vm.password);
        if_active();
    }
}])