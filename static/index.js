$(document).ready(function() {
	$(".arrow").hover(function() {
		$(this).append("<div class='arrow-right'></div>");
		$(this).parent().find("a").fadeOut(300).fadeIn(300);
	}, function() {
		$("div").remove(".arrow-right");
	});

	$(".arrow").live("click", function() {
		var li = $(this).parent();
		var text = li.find("a").html();
		$("li").css("background-color", "");
		li.css("background-color", "rgba(200,200,200,.5)");
		if ($(".content").css("display") == "none") {
			$(".container").transition({
				x: '-300px'
			});
			$(".task").transition({
				y: "44%"
			});
			$(".content").fadeIn("slow");
		} else {
			$(".task").empty().transition({
				y: "110%"
			}).fadeOut(100).transition({
				y: "-110%"
			}, 1).fadeIn().transition({
				y: "50%"
			}).transition({
				y: "44%"
			});
		}
		if (text == "AUTOMATION") {
			$(".task").html("<iframe type='text/html' class='video' src='http://www.youtube.com/embed/OsNkcUq0veI' frameborder='0'></iframe>");
		} else if (text == "TEST REPORT") {
			$(".task").html("<iframe type='text/html' class='video' src='http://www.youtube.com/embed/GUU6NWI0w4Y' frameborder='0'></iframe>");
		} else if (text == "BUG LIST") {
			$(".task").html("<iframe type='text/html' class='video' src='http://www.youtube.com/embed/dLSTc2hodUI' frameborder='0'></iframe>");
		}
	});
	$(".x").live("click", function() {
		$(".task").empty();
		$(".content").fadeOut();
		$("li").css("background-color", "");
		$(".container").transition({
			x: 0
		});
	});
});