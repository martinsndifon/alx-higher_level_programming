$(function () {
	const hello = $('#hello');
	$.ajax({
		type: 'GET',
		dataType: "jsonp",
		jsonpCallback: "callback",
		url: 'https://fourtonfish.com/hellosalut/?lang=fr',
		success: (data) => {
			hello.text(data.hello);	
		}
	});
});