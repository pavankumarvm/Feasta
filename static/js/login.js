const inputs = document.querySelectorALL('.input');

function focusFunc(){
    let parent = this.parentNode.parentNode;
    if(this.value == "");{
        parent.classList.remove('focus');
    }
}

inputs.forEach(input => {
    input.addEventListener('focus', focusFunc);
    input.addEventListener('blur',blurFunc);
});