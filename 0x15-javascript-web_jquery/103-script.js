$(function() {
	const langCode = $('#language_code');
	const translate = $('#btn_translate');
	const hello = $('div#hello');

	translate.on('click', () => {
		const code = langCode.val();
		$.ajax({
			type: 'GET',
			url: 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + code,
			success: (data) => {
				hello.text(data.hello);
			}
		});
	});

	langCode.on('keypress', (event) => {
		if (event.keyCode === 13) {
			const code = langCode.val();
			$.ajax({
				type: 'GET',
				url: 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + code,
				success: (data) => {
					hello.text(data.hello);
				}
			});
		}
	});
});
