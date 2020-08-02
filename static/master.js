let hidden = true;
const comment_button = document.getElementById('comment_button');
comment_button.addEventListener('click', function() {
    if (hidden == true){
        document.getElementById('comments').hidden = false;
        hidden = false;
    }
    else {
        document.getElementById('comments').hidden = true;
        hidden = true;
    }
});
