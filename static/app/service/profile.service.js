/*
    Profile Service
*/

feasta.service('Profile', ['$http', function($http){

    var Profile = {
        get: get,
        update: update,
        delete: destroy,
        getMessowner: getMessowner,
        getConsumer: getConsumer,
    }
    return Profile;

    //******************** Get Profile *******************//
    
    function get(username){
        return $http.get('api/v1/get-user/' + username +'/');
    }


    //******************** Upadte Profile *******************//
    
    function update(username){
        return $http.post('api/v1/get-user/' + username +'/');
    }

    //******************** Delete Profile *******************//
    
    function destroy(username){
        return $http.delete('api/v1/get-user/' + username +'/');
    }

    //********************** Messowner Details ********************//

    function getMessowner(username){
        return $http.get("api/v1/get-messowner/" + username + "/");
    }

    //********************** Consumer Details ********************//

    function getConsumer(username){
        return $http.get("api/v1/get-consumer/" + username + "/");
    }
}])