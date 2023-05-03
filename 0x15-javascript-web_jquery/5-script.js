const list = $('.my_list');
const addItem = $('div#add_item');

addItem.on('click', () => {
	list.append('<li>Item</li>');
});