// Authentication

feasta.service('Authentication',['$cookies', '$http', function($cookies, $http){

    var Authentication = {
        login: login,
        logout: logout,
        register: register,
        isAuthenticated: isAuthenticated,
        getAuthenticatedAccount: getAuthenticatedAccount,
        setauthenticatedAccount: setauthenticatedAccount,
        unauthenticate: unauthenticate,
    }
    
    return Authentication;
    
    //**********************Register*************************//

    function register(username, email, password1, password2){
        // Registering particular user.

        return $http.post('api/v1/rest-auth/registration/',{
            username: username,
            password1: password1,
            password2: password2,
            email: email,
        }).then(registerSuccessFn, registerErrorFn);
    }

    
    function registerSuccessFn(data, status, headers, config){
        // On successful registration
        console.log("Registered Successfully");
        return (true);
    }

    function registerErrorFn(data, status, headers, config){
        // On failure.

        console.error("Epic failure");
        error_message = data.data;
        console.log(error_message);
        return (false);
    }


    //*************************Login****************************//

    function login(username, password){
        // Logging in using particular username and password.

        return $http.post('api/v1/rest-auth/login/',{
            username: username,
            password: password,
        }).then(loginSuccessFn, loginErrorFn);
    }

    function loginSuccessFn(data, status, headers, config){
        // On successful login.

        Authentication.setauthenticatedAccount(data.data);
        console.log("Login Successful");
        // console.log(data);
    }

    function loginErrorFn(data, status, headers, config){
        //on failure.

        console.error("Epic failure");
        // console.log(data);
    }


    //************************ Logout ***************************//

    function logout(){
        // Loogout the user

        return $http.post('api/v1/rest-auth/logout/')
            .then(logoutSuccessFn,logoutErrorFn);
    }

    function logoutSuccessFn(){
        // On successful logout

        Authentication.unauthenticate();
        console.log("Logout Successful");
        // window.location.href = '/';
    }

    function logoutErrorFn(){
        // On failure

        console.error("Epic failure");
    }

    //********************** Authenticated Account ********************//

    function getAuthenticatedAccount(){
        // Returns undefined if not logged in,
        // else returns the account key and value pair as object.

        if(!$cookies.getObject("authenticatedAccount")){
            return;
        }
        return JSON.parse($cookies.getObject("authenticatedAccount"));
    }

    function isAuthenticated(){
        // Returns true if User is authenticated else returns false.

        return !!getAuthenticatedAccount();
    }

    function setauthenticatedAccount(account){
        //  Sets the authenticated account key for session.

        var authenticatedAccount = JSON.stringify(account);

        $cookies.putObject("authenticatedAccount", authenticatedAccount);
    }

    function unauthenticate(){
        // Removes the authenticated account cookies on logout.

        $cookies.remove("authenticatedAccount");
    }
}])