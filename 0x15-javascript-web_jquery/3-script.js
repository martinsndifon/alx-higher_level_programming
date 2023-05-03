const header = $('header');
const red = $('div#red_header');

red.on('click', () => {
	header.addClass('red')
});