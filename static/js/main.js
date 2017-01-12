$(document).ready(function () {

	$("#new_post_button").click(function () {
		alert('new post clicked');
	});

	$("#new_post_form").on('show.bs.modal', function () {
		alert('modal shown');
	});
});