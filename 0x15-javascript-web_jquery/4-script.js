const header = $('header');
const toggle = $('div#toggle_header');

toggle.on('click', () => {
	header.toggleClass('red green');
});