$(document).ready(function()
{
	$('#Search-Form').on('submit', function(event)
	{
		event.preventDefault();
		console.log("FORM SUBMITTED!");
		Search_For_School();
	});

	function Search_For_School()
	{
		console.log("The user searched for: " + $('#school-search-box').val());
		$.ajax(
			{
				url: "",
				type: "POST",
				data: { searchString: $('#school-search-box').val() },

				success: function(json)
				{
					$('#school-search-box').val('');
					console.log(json);
					console.log("success");
				},
				error: function()
				{
					console.log('ERROR');
				}
			});
		)
	}
});
