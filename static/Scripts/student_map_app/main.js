$(document).ready(function()
{
	
	$('#school-search-form').on('submit', function(event)
	{
		event.preventDefault();
		var searchFormData = $('#school-search-form').serializeArray();
		$.ajax(
		{
			type: "POST", 			// If we don't specify type, it resorts to get
			// url: ...  			// If we don't specify url, it resorts to current URL
			data: searchFormData,
			dataType: 'html',		// 'text/html'
			success: function(response)
			{
				var result = $('<div />').append(response).find('#school-select-name').html();
				$('#school-select-name').html(result);

				// $('#school-select-name').removeAttr('multiple');
			},
			error: function(response)
			{
				console.log("pepe SCREEEEECH!!!!");
			},
		});
	});
	$('#school-select-form').on('submit', function(event)
	{
		event.preventDefault();
		var selectFormData = $('#school-select-form').serializeArray(); // Stored as an array of javascript objects
		$.ajax(
		{
			type: "POST",
			data: selectFormData,
			success: function(resposne)
			{
				$('#school-select-name').val('');
				console.log(response);
			},
			error: function()
			{
				console.log('ERROR');
			}
		});
	});
});
