/*
    Profile Controller
*/

feasta.controller('getProfile',['$scope', '$http', '$location', '$routeParams', 'Profile', 'Authentication', function($scope, $http ,$location, $routeParams, Profile, Authentication){
    $scope.Profile = {};
    var vm = this;
    vm.logout = logout;

    if_active();

    function if_active(){
        var username = $routeParams.username.substr(0);

        Profile.get(username).then(profileSuccessFn, profileErrorFn);

        function profileSuccessFn(data, status, headers, config){
            $scope.Profile = data.data;
            if($scope.Profile.is_messowner == true){
                Profile.getMessowner(username).then(detailSuccessFn, detailErrorFn);
            }
            else if($scope.Profile.is_consumer == true){
                Profile.getConsumer(username).then(detailSuccessFn, detailErrorFn);
            }

            function detailSuccessFn(data, status, headers, config){
                var object = angular.extend({}, data.data, $scope.Profile);
                $scope.Profile = object;
            }

            function detailErrorFn(data, status, headers, config){
                console.error("Epic Failure");
                console.log(data);
            }
        }

        function profileErrorFn(data, status, headers, config){
            $location.path('/');
            alert("Sorry, there was problem while loading the Profile." + '\n' + 
                    "Try, Logging in again.");
            Authentication.logout();
        }
    }

    function logout(){
        Authentication.logout();
        $location.path('/');
    }

    var previous = 0;

    $scope.select = function(i){
        var nav_content = $(".nav-content");
        var selected = nav_content.get(i);
        selected.className = 'nav-content';
        if(previous!=i){
            var un_selected = nav_content.get(previous);
            un_selected.className += ' hide';
            previous = i;
        }
    }


    //***************************Profile***************************//
    $scope.editProfile = function(){
        console.log("You can edit Profile Now.");
        var input = $(".tag-desc");
        for(let i=0;i<input.length;i++){
            let element = input.get(i);
            element.className += " update";
        }
        var address_input = $("#address");
        address_input[0].className += " update";
        var editbtn = $("#edit");
        editbtn[0].className += " hide";
        var cancelbtn = $("#cancel");
        cancelbtn[0].className = "cancel";
        var updatebtn = $("#update-it");
        updatebtn[0].className = "update-it";
    };

    $scope.cancelEdit = function(){
        console.log("Editing cancelled.");
        var input = $(".tag-desc");
        for(let i=0;i<input.length;i++){
            let element = input.get(i);
            element.className = "tag-desc";
        }
        var address_input = $("#address");
        address_input[0].className = "address-text";
        var editbtn = $("#edit");
        editbtn[0].className = "edit";
        var cancelbtn = $("#cancel");
        cancelbtn[0].className += " hide";
        var updatebtn = $("#update-it");
        updatebtn[0].className += " hide";
    }

    $scope.updateProfile = function(){
        Console.log("Updating Profile");
    }
}])