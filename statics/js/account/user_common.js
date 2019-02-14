$(document).ready(function() {
	$("#register").click(function() {
		var user = $("#username").val();
		var pwd = $("#password").val();
		var pwdr = $("#passwordr").val();

		post_data = {
			"username": user,
			"password": pwd,
			"passwordr": pwdr
		}

		$.ajax({
			type: "post",
			url: "/register",
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

})
