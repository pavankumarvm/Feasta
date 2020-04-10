/*
    feasta menu service
*/

feasta.service("Menu", ['$http', function($http){

    var Menu = {
        getItem :getItem,
        addItem :addItem,
    }

    return Menu;

    function getItem(mess_id){
        console.log(mess_id);
    }

    //***********************Add Item ************************//

    function addItem(item, mess_id){
        $http.post("api/v1/get-menu/",{
            item:item,
            mess_id:mess_id,
        })
        .success(function(data){
            console.log("Item added" + data);
        })
        .error(function(data, status, value){
            console.error("Epic Failure");
            console.log("Item cannot be added" + data);
        })
    }
}])