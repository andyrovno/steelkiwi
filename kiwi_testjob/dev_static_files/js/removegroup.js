$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                     break;
                 }
             }
         }
         return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});

function removeGroup(obj, id) {
	if (confirm('Are you sure you want to delete this instance?')) {
		$.ajax({
			type:		"POST",
			url:		delurl + "?id=" + id,
			data:		{
				"group_id": id
			},
			dataType:	"json",
			success:	function(data) {
				if (data['success']) {
					row = $(obj).parents(".group_table_row");
					$(obj).parents(".group_table_row").animate({opacity: 'hide'}, "slow");
				}
				else {
					alert("Something went wrong! Try again later.");
				}
			}
		})
	}
}
