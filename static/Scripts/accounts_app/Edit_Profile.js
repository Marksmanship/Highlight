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

	$('.delete-container').click(function(){
		var indx = $('.delete-image').index(this);
		setRequestHeader();
		$.ajax({
	        type:'POST',
	        url: '/ajax/account/edit/',
	        data: { 'imageNumber': indx, },
	        success: function(response)
			{
	            console.log(response);
	        },
    	});
	});
});
			// xhr.onload = function()
			// {
			// 	if (xhr.status >= 200 && xhr.status < 300)
			// 	{
			// 		console.log("success", xhr)
			// 	}else {
			// 		console.log("failure");
			// 	}
			// };
