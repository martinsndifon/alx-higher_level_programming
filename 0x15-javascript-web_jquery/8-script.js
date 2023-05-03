const title = $('ul#list_movies');

$.ajax({
	type: 'GET',
	url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
	success: (data) => {
		let result = data.results;
		$.each(result, (i, res) => {
			title.append(`<li>${res.title}</li>`);
		});
	}
});