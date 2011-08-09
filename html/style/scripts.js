//executes all this after the DOM has loaded
$(document).ready(function(){

	//on load hides all divs except the home one
	$('div').slice(2).hide();

	//front page menu
	$('#buttons li a').click(function(){
		var action = $(this).attr("href").replace("#", "");
		$("#p_home").fadeOut(200, function(){
			$("#p_"+action).fadeIn(200);
		});
	});

	//header link
	$('h1 a').click(function(){
		$('div#wrap>div').fadeOut(200, function(){
			$("#p_home").fadeIn(200);
		});
	});

	//New Order Page

	//hides takeaway by default and sets 
	$('ul#takeaway').hide();
	$('#t_dinein').css('border-bottom', '10px solid #036902');

	//switches between which menu is active
	$('ul#dinein_takeaway a').click(function(){
		var action = $(this).attr('id').replace('t_', '');
		$('#dinein, #takeaway').fadeOut(200, function(){
			$('#t_dinein, #t_takeaway').css('border', 'none');
			$('#t_'+action).css('border-bottom', '10px solid #036902');
			$('#'+action).fadeIn(200);
		});
	});

	//when form submitted rouds up the inputs into an array
	$('a#place_order').click(function(){
		var inputs = $('#order').serializeArray();
		inputs_json = JSON.stringify(inputs);
		if(inputs_json){
			console.log(inputs_json);
		}
	});

});