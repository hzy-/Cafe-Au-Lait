$(document).ready(function(){
	//on load hides all divs except the home one
	$("div").slice(2).hide();

	//switches page to #new_order
	$('#new_order').click(function(){
		$("#p_home").fadeOut(200, function(){
			$("#p_new_order").fadeIn(200);
		});
	});
});