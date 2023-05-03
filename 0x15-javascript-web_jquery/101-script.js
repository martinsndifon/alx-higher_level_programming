$(function () {
	const addItem = $('div#add_item');
	const removeItem = $('div#remove_item');
	const clearList = $('div#clear_list');
	const list = $('.my_list');

	addItem.on('click', () => {
		list.append('<li>Item</li>');
	});

	removeItem.on('click', () => {
		const li = $('.my_list li')
		li.last().remove();
	});

	clearList.on('click', () => {
		list.empty();
	})
});