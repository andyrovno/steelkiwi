function display_form_errors(errors, $form) {
	for (var error in errors) {
		$form.find('input[name=' + error + ']').after('<div class="error" style="color:#ff0000">' + errors[error] + '</div>');
	}
}

$(document).ready(function() {
	var options = {
		type:		'post',
		dataType:	'json',
		success:	responseShow
	};
	$('#edit_form').submit(function() {
		$(this).ajaxSubmit(options);
		var $form_elems = $(this).find('input, button');
		$form_elems.prop("disabled",true);
		$('#error_message').text("Loading data, it may take a few moments...").fadeIn("slow");
		return false;
	});
});
function responseShow(data, responseText, statusText, xhr, $form) {
	$('#edit_form').find('input, button').prop("disabled", false);
	$('#edit_form').find('.error').remove();
	$('#error_message').fadeOut("slow");
	if (data['result'] == 'success') {
		e_msg = data['message'];
	}
	else if (data['result'] == 'error') {
		e_msg = "Your form contains errors, please check out!";
		display_form_errors(data['response'], $('#edit_form'));
	}
	$('#error_message').text( e_msg ).fadeIn("slow");
}
