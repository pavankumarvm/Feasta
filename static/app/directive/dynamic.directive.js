/*
    feasta additem directive
*/

//This file is for compiling the dynamically inserted elements


//  This is for adding menu items.
feasta.directive('addItem', function($compile){
    var i=1;
    return {
        replace: true,
        link: function(scope, element, attrs){
            element.on("click", function(){
                scope.$apply(function(){
                    $(".remove--items").show();
                    var template = 
                        "<li class='list-item' id='item" + i + "'>"
                        +   "<div class='item'>"
                        +       "<input type='text' class='item-input'>"
                        +       "<div class='remove' ng-click='removeItem(" + i + ")'>"
                        +           "<svg class='svg-icon' viewBox='0 0 20 20' fill='red'>"
                        +               "<path d='M14.776,10c0,0.239-0.195,0.434-0.435,0.434H5.658c-0.239,0-0.434-0.195-0.434-0.434s0.195-0.434,0.434-0.434h8.684C14.581,9.566,14.776,9.762,14.776,10 M18.25,10c0,4.558-3.693,8.25-8.25,8.25c-4.557,0-8.25-3.691-8.25-8.25c0-4.557,3.693-8.25,8.25-8.25C14.557,1.75,18.25,5.443,18.25,10 M17.382,10c0-4.071-3.312-7.381-7.382-7.381C5.929,2.619,2.619,5.93,2.619,10c0,4.07,3.311,7.382,7.381,7.382C14.07,17.383,17.382,14.07,17.382,10'></path>"
                        +           "</svg>"
                        +       "</div>"
                        +   "</div>"
                        +"</li>"
                    i++;
                    var item = $compile(template)(scope);
                    var items_list = $(".items--list");
                    items_list.append(item[0]);
                })
            })
        }
    }
})