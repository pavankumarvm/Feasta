
feasta.controller("registerUser", ['$location', '$http', '$scope', 'Authentication',function($location, $http, $scope, Authentication){
    var vm = this;
    vm.register = register;
    vm.logout = logout;
    vm.proceed = proceed;

    function if_active(){
        // If the User is Registered/Authenticated then they must be redirected to login page.
        if(Authentication.isAuthenticated()){
            $scope.isAuthenticated = true;
            $location.path('/profile');
        }
        else{
            $location.path('/login');
        }
    }

    function register(){
        var registered = Authentication.register(vm.username, vm.email, vm.password1, vm.password2);
        if(!!registered){
            $scope.navigate(0);
        }
    }

    function logout(){
        Authentication.logout();
        $location.path('/signup');
    }

    function proceed(){
        $http.post('api/v1/get-user/'+ vm.username +'/',{
            username:vm.username,
            email:vm.email,
            first_name:vm.first_name,
            last_name:vm.last_name,
            phone_no:vm.phone_no,
            is_messowner:vm.is_messowner,
            is_consumer:vm.is_consumer,
        })
        .success(function(data){
            console.log("User Registeration Completed.");
            if(vm.is_consumer){
                $http.post('api/v1/get-consumer/',{
                    user:vm.username,
                    gender:vm.gender,
                    college:vm.college,
                    stay_type:vm.stay_type,
                })
                .success(function(data){
                    console.log("Consumer Registered Successfully");
                    console.log(data);
                    $location.path('/login');
                })
                .error(function(data){
                    console.error("Epic Failure in Consumer Registration.");
                    console.log(data);
                })
            }
            else if(vm.is_messowner){
                vm.opening_time = $("#opening_time").get(0).value;
                vm.closing_time = $("#closing_time").get(0).value;
                $http.post('api/v1/get-mess/',{
                    mess_name:vm.mess_name,
                    food_type:vm.food_type,
                    typeof_mess:vm.typeof_mess,
                    address:vm.address,
                    opening_time:vm.opening_time,
                    closing_time:vm.closing_time,
                    one_time:vm.one_time,
                    monthly:vm.monthly,
                })
                .success(function(data){
                    console.log("Mess Registered Successfully");
                    console.log(data);
                    vm.mess_id = data['id'];
                    console.log(vm.mess_id);
                    $http.post('api/v1/get-messowner/',{
                        user:vm.username,
                        mess_id:vm.mess_id,
                    })
                    .success(function(data){
                        console.log("Messowner Registered Successfully");
                        console.log(data);
                        $location.path('/login');
                    })
                    .error(function(data){
                        console.error("Epic Failure in Messowner Registration.");
                        console.log(data);
                    })
                })
                .error(function(data){
                    console.log("Epic Failure in Mess Registration.")
                    console.log(data);
                })
            }
        })           
        .error(function(data){
            console.error("Epic Failure");
            console.log(data);
        })
    }

    var user_type;
    $scope.navigate = function(i){
        if(i==0){
            //On registration
            var previous = $(".signup--container");
            var next = $(".nav--container");
            previous[0].className += " hide";
            next[0].className = "nav--container";
        }
        else if(i==1){
            //On filling personal details
            if(user_type== undefined){
                console.log("User type not selected.");
            }
            else{
                let nav_block = $(".nav--block");
                nav_block[0].className += " hide";
                nav_block[1].className = "nav--block";
                if(user_type == 0){
                    vm.is_messowner = false;
                    vm.is_consumer = true;
                    var content = $(".consumer");
                    content[0].className = "consumer";

                }
                else if(user_type == 1){
                    vm.is_messowner = true;
                    vm.is_consumer = false;
                    var content = $(".messowner");
                    content[0].className = "messowner";
                }
            }
        }
        else if(i==2){
            let nav_block = $(".nav--block");
            nav_block[0].className = "nav--block";
            nav_block[1].className += " hide";
        }
    }
    
    $scope.select = function(i){
        var options = $(".option");
        var selected = options.get(i);
        selected.className += ' selected';
        var not_selected = options.get((i+1)%2);
        not_selected.className = 'option';
        user_type = i;
    }
}])