$(document).ready(function() {
	$("#login").click(function() {
		var user = $("#username").val();
		var pwd = $("#password").val();

		post_data = {
			"username": user,
			"password": pwd
		}

		$.ajax({
			type: "post",
			url: "/login",
			data: post_data,
			cache: false,
			success: function(data){
				alert(data);
			},
			error: function(data){
				alert("error");
			}

		})
	});

});
