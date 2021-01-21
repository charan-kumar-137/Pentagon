function showComments(comment_id){
	const comment_button = document.getElementById(comment_id);
	hidden = document.getElementById(comment_id).hidden;
	if (hidden == true){
		document.getElementById(comment_id).hidden = false;
		hidden = false;
	}
	else {
		document.getElementById(comment_id).hidden = true;
		hidden = true;
	}

}

function showPostBody(post_id){
	const post_button = document.getElementById(post_id);
	hidden = document.getElementById(post_id).hidden;
	if (hidden == true){
		document.getElementById(post_id).hidden = false;
		hidden = false;
	}
	else {
		document.getElementById(post_id).hidden = true;
		hidden = true;
	}

}
