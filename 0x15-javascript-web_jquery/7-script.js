const character = $('#character');

$.ajax({
	type: 'GET',
	url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
	success: (data) => {
		character.text(data.name);
	}
});