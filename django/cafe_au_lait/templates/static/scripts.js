//executes all this after the DOM has loaded
$(document).ready(function(){

	//General

		//on load hides all divs except the home one
		$('div').slice(2).hide();

		//front page menu
		$('#buttons li a').click(function(){
			var action = $(this).attr("href").replace("#", "");
			$("#p_home").fadeOut(200, function(){
				$("#p_"+action).fadeIn(200);
				$("#p_"+action+" div").fadeIn(200);
			});
		});

		//header link
		$('h1 a').click(function(){
			$('div#wrap>div').fadeOut(200, function(){
				$("#p_home").fadeIn(200);
			});
		});

	//New Order Page

		//grabs the beverages
		function get_beverages(){
			$.get('/beverages/list/',
			function(data){
				$('form#order').empty();
				$('form#order').append(data);
			});
		}

		//refreshes beverage list whenever the new order page is opened
		$('#new_order').click(function(){
			get_beverages();
			$('ul#takeaway').hide();
		});

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

		/*when form submitted rouds up the inputs into 
		an array, then sends it off as json*/
		$('a#place_order').click(function(){
			var inputs = $('#order').serializeArray();
			inputs_json = JSON.stringify(inputs);
			if(inputs_json){
				console.log(inputs_json);
				$.ajax({
					type: "POST",
					contentType: 'application/json; charset=utf-8',
					url: "/orders/submit/",
					data: inputs_json,
					complete: function(msg){
						//alert( "Data Saved: " + msg );
						console.log(msg);
					}
				});
			}
		});

	//Curent Orders

		//loads current orders
		function load_current_orders(){
			$.get('/orders/current/',
			function(data){
				$('div#p_current_orders').empty();
				$('div#p_current_orders').append(data);

				//binds clear order click event
				$(".clear_order").click(function() {
					$(this).parent().hide();
					$.post('/orders/clear/', {order: $(this).attr("id").replace('order_', '')}, function(data){
						console.log("complete!");
					});
				});
			});
		}

		//loads it when the page is opened
		$('a#current_orders').click(load_current_orders());

		//updates current items list
		setInterval(function(){
			if ($('div#p_current_orders').is(":visible")){
				load_current_orders();
			}
		},10000);

		//completes item when x pressed
		
});
