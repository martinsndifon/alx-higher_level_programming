header = $('header');
changeHeader = $('#update_header');

changeHeader.on('click', () => {
	header.text('New Header!!!');
});