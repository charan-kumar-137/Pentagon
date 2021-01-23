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

