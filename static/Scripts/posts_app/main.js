$(document).ready(function(){
	var cookieScript = document.createElement('script');
	cookieScript.setAttribute('src','https://cdnjs.cloudflare.com/ajax/libs/jquery-cookie/1.4.1/jquery.cookie.min.js');
	document.head.appendChild(cookieScript);

	// Function to GET csrftoken from Cookie
	function getCookie(name) {
	    var cookieValue = null;
	    if (document.cookie && document.cookie !== '') {
	        var cookies = document.cookie.split(';');
	        for (var i = 0; i < cookies.length; i++) {
	            var cookie = jQuery.trim(cookies[i]);
	            // Does this cookie string begin with the name we want?
	            if (cookie.substring(0, name.length + 1) === (name + '=')) {
	                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	                break;
	            }
	        }
	    }
	    return cookieValue;
	}
	var csrftoken = getCookie('csrftoken');

	function csrfSafeMethod(method) {
    	// these HTTP methods do not require CSRF protection
    	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	// Function to set Request Header with `CSRFTOKEN`
	function setRequestHeader(){
	    $.ajaxSetup({
	        beforeSend: function(xhr, settings) {
	            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	                xhr.setRequestHeader("X-CSRFToken", csrftoken);
	            }
	        }
	    });
	}



	$('#blog-post-like').click(function(){								// This triggers whenever he hit like on a blog post
		var data = { 'objectId': getPostId() };							// objectId is defined within the template
		setRequestHeader();
		$.ajax({
			type: 'POST',
			url: '/ajax/blog/like/',									// Post to this URL to trigger view, but we don't redirect the user to it
			dataType: 'json',
			data: (data),
			success: LikePost,
			error: console.log("hi"),
		});

		function LikePost(response){											// response is the server's response received from "succes:"
			console.log(response.Like_Status);
			if (response.Like_Status == 'Disliked' || response.Like_Status == 'Never-Liked')
			{
				$('#blog-post-like').toggleClass('liked', false); 				// Since we know it's either disliked or hasn't been liked yet, remove the "liked" class if it's there (false)
			}
			else if (response.Like_Status == 'Liked')
			{
				$('#blog-post-like').toggleClass('liked', true);
			}
			else{console.log("color is weird")}
		}
	});
});
