var pageInit = {
	//Init function
	init: function(settings) {
		// Init configration
		pageInit.config = {
			pageBody: ".pagebody",
			leftMenuButton: ".menu",
			leftNav: ".leftnav",
			summaryPanel: ".summary_area",
			summaryMenu: ".summary_menu",
			taskSummaryArea: ".task_summary_area",
			taskSummaryButton: ".summary_by_todo_button",
			userSummaryArea: ".user_summary_area",
			userSummaryButton: ".summary_by_user_button",
			taskItem: ".task_li",
			tagInTask: ".task_tag",
			todoButton: ".task_todo",
			topMark: ".task_top",
			toTopButton: ".task_to_top",
			doneButton: ".task_done",
			grayBgColor: "#f5f5f5",
			whiteBgColor: "white",
			tagInbox: "#tag",
			tagInCreator: ".task_tag_container",
			taskArea: ".task_area",
			taskCreatorPanel: ".task_creator",
			taskCreatorButton: ".create_task_button",
			commentArea: ".comment_form",
			reassignBox: "#reassign",
			userList: ".user_list",
			closeCreatorButton: ".close_task_creator",
			colorList: [
				'#1abc9c',
				'#16a085',
				'#f1c40f',
				'#f39c12',
				'#2ecc71',
				'#27ae60',
				'#e67e22',
				'#d35400',
				'#3498db',
				'#2980b9',
				'#e74c3c',
				'#c0392b'
			],
		};

		$.extend(pageInit, settings);
		pageInit.hoverTask();
		pageInit.toggleMenu();
		pageInit.openSummary();
		pageInit.switchSummary();
		pageInit.openTaskCreator();
		pageInit.closeTaskCreator();
		pageInit.hoverActionButton();
		pageInit.randomCategory();
		pageInit.tagRender();
		pageInit.expandTagListInCreator();
		pageInit.expandUserList();
		pageInit.hideExpandItems();
	},

	hideExpandItems: function() {
		$(document).on('click', function(event) {
			if (!$(event.target).closest(pageInit.config.taskArea).length) {
				$(pageInit.config.taskItem)
					.removeClass('selected')
					.css(pageAction.config.taskDefaultClass);
				$(pageInit.config.commentArea).hide();
			}
			if (!$(event.target).closest(pageInit.config.tagInbox).length) {
				$(pageInit.config.tagInCreator).hide();
			}
			if (!$(event.target).closest(pageInit.config.reassignBox).length) {
				$(pageInit.config.userList).hide();
			}
			if (!$(event.target).closest(pageInit.config.summaryPanel).length) {
				$(pageInit.config.summaryPanel).stop()
					.removeClass('activated')
					.animate({
						'right': '-320px'
					}, 'fast');
				$(pageInit.config.pageBody).animate({
					'padding-right': 0
				}, 'fast');
				$(pageInit.config.leftNav).removeClass('shadow');
			}
		});
	},

	toggleMenu: function() {
		$(pageInit.config.leftMenuButton).on('click', function(event) {
			var left_nav = $(pageInit.config.leftNav);
			var pagebody = $(pageInit.config.pageBody);
			if (left_nav.hasClass('selected')) {
				left_nav.removeClass('selected')
					.stop()
					.animate({
						'left': '-230px',
					}, 'fast');
			} else {
				left_nav.addClass('selected')
					.stop()
					.animate({
						'left': 0
					}, 'fast');
				pagebody.stop()
			}
		});
	},

	openSummary: function() {
		$(pageInit.config.summaryMenu).on('click', function(event) {
			var summary_panel = $(pageInit.config.summaryPanel);
			var pagebody = $(pageInit.config.pageBody);
			var left_nav = $(pageInit.config.leftNav);
			if (summary_panel.hasClass('activated')) {
				return 0;
			} else {
				summary_panel.addClass('activated')
					.stop()
					.animate({
						'right': 0
					}, 'fast');
				pagebody.stop()
					.animate({
						'padding-right': '320px'
					}, 'fast');
				left_nav.addClass('shadow');
			}
		});
	},

	switchSummary: function() {
		var task_area = $(pageInit.config.taskSummaryArea);
		var user_area = $(pageInit.config.userSummaryArea);
		$(pageInit.config.taskSummaryButton).on('click', function() {
			task_area.show();
			user_area.hide();
		});
		$(pageInit.config.userSummaryButton).on('click', function() {
			task_area.hide();
			user_area.show();
		});
	},

	openTaskCreator: function() {
		$(pageInit.config.taskCreatorButton).click(function(event) {
			$(pageInit.config.taskCreatorPanel).show();
		});
	},

	closeTaskCreator: function() {
		$(pageInit.config.closeCreatorButton).click(function(event) {
			$(pageInit.config.taskCreatorPanel).hide();
		});
	},

	expandTagListInCreator: function() {
		$(pageInit.config.tagInbox).on("click", function() {
			$(pageInit.config.tagInCreator).show();
		});
	},

	expandUserList: function() {
		$(pageInit.config.reassignBox).on("click", function() {
			$(pageInit.config.userList).show();
		});
	},

	hoverTask: function() {
		$(pageInit.config.taskItem).live("mouseover", function() {
			$(this).find('.task_todo, .task_to_top').show();
		}).live('mouseleave', function(event) {
			$(this).find('.task_todo, .task_to_top').hide();
		});
	},

	checkCNChar: function(str) {
		if (str.substr(0, 1).match(/[\u3400-\u9FBF]/)) {
			return true
		} else {
			return false
		}
	},

	hoverActionButton: function() {
		$(pageInit.config.todoButton)
			.add(pageInit.config.toTopButton)
			.add(pageInit.config.doneButton)
			.hover(function() {
				$(this).css('background-color', pageInit.config.grayBgColor);
			}, function() {
				$(this).css('background-color', pageInit.config.whiteBgColor);
			});
	},

	randomCategory: function() {
		var categoryList = {};
		var pick_index = 0;
		$(pageInit.config.tagInTask).each(function(index) {
			var html = $(this).find("span").html();
			if (html in categoryList) {
				$(this).css("background-color", categoryList[html]);
			} else {
				pick_index += 1;
				categoryList[html] = pageInit.config.colorList[pick_index];
				$(this).css("background-color", categoryList[html]);
			}
			if (pageInit.checkCNChar(html)) {
				$(this).find("span").css("padding-left", "8px");
			}
		});
	},


	tagRender: function() {
		var tag_path = (window.location.href).split("/").pop();
		$(pageInit.config.leftNav).find("li").each(function() {
			if ($(this).html() === decodeURIComponent(tag_path)) {
				$(this).css({
					"background": "#f5f5f5",
				});
			}
		});
	},
};


var pageAction = {
	// Action function
	init: function(settings) {
		// Action configration
		pageAction.config = {
			todoButton: ".task_todo",
			topButton: ".task_to_top",
			topMark: ".task_top",
			doneButton: ".task_done",
			todoDiv: "<div class='task_todo'></div>",
			topDiv: "<div class='task_top'></div>",
			toTopDiv: "<div class='task_to_top'></div>",
			doneDiv: "<div class='task_done'></div>",
			tagInTask: ".task_tag",
			tagInComment: ".tag_in_comment",
			timeInComment: ".time_in_comment",
			tagInCreator: ".task_tag_container",
			tagInbox: "#tag",
			taskCreator: ".task_creator",
			taskSubmitButton: ".task_submit",
			taskArea: ".task_area",
			taskItem: ".task_li",
			taskValidation: ".task_validation",
			taskID: ".task_id",
			taskTime: ".task_time",
			taskContainer: ".task_container",
			taskContent: ".task_content",
			taskAuthor: ".task_author",
			taskDefaultClass: {
				'margin': '0 0 1px 0',
				'transition': 'none',
				'box-shadow': 'none'
			},
			taskHighlightClass: {
				'margin': '30px -10px',
				'transition': 'scale 0.1s ease-in-out',
				'box-shadow': '0 0 6px rgba(0,0,0,.16),0 6px 12px rgba(0,0,0,.32)'
			},
			taskInComment: ".comment_task_detail",
			todoTaskList: ".task_list_todo",
			doneTaskList: ".task_list_done",
			commentTextArea: ".comment_textarea",
			commentSubmitButton: ".comment_submit",
			commentValidation: ".comment_validation",
			commentArea: ".comment_form",
			commentList: ".comment_list",
			reassignButton: ".submit_reassign",
			reassignInput: "#reassign",
			expandAllDoneTask: ".all_done",
			summaryArea: ".summary_area",
			summaryTable: ".task_summary_table",
			userList: ".user_list"
		};

		$.extend(pageAction, settings);
		pageAction.getAuthorLinkInTask();
		pageAction.autoFillTagName();
		pageAction.autoFillUserName();
		pageAction.getTagLinkInComment();
		pageAction.submitTask();
		pageAction.submitComment();
		pageAction.lookForComment();
		pageAction.markTaskDone();
		pageAction.markTaskTodo();
		pageAction.markTaskTop();
		pageAction.reassignOwner();
		pageAction.reuturnDoneTask();
		pageAction.showCommentSubmitButton();
	},

	getAuthorLinkInTask: function() {
		$(pageAction.config.taskAuthor).live("click", function() {
			var name = $(this).html();
			window.location.href = "/task/people/" + name;
		});
	},

	autoFillTagName: function() {
		$(pageAction.config.tagInCreator).find("li")
			.live('click', function() {
				$(pageAction.config.tagInbox).val($(this).html());
				$(pageAction.config.tagInCreator).hide();
			});
	},

	autoFillUserName: function() {
		$(pageAction.config.userList).find("li")
			.live("click", function() {
				console.log($(this).html());
				$(pageAction.config.reassignInput).val($(this).html());
				$(pageAction.config.userList).hide();
			})
	},

	getTagLinkInComment: function() {
		$(pageAction.config.tagInComment).live("click", function() {
			var name = $(this).find("span").html();
			window.location.href = "/task/tag/" + name;
		});
	},

	showCommentSubmitButton: function() {
		$(pageAction.config.commentTextArea).live('click', function(event) {
			$(pageAction.config.commentSubmitButton).show();
		});
	},

	submitTask: function() {
		$(pageAction.config.taskSubmitButton).live("click", function() {
			var task = $(pageAction.config.taskCreator).find("textarea").val();
			var tag = $(pageAction.config.taskCreator).find("input").val();
			if (task.trim() !== '' && tag.trim() !== '') {
				$(pageAction.config.taskValidation).html("");
				$.ajax({
					type: "POST",
					url: window.location.href,
					data: {
						'new_task': true,
						'task': task,
						'task_tag': unescape(tag),
					},
					cache: false,
					dataType: "json",
				}).done(function(data) {
					if (data) {
						$(pageAction.config.todoTaskList)
							.prepend("<li class='task_li'>\
							<div class='task_todo'></div>\
							<div class='task_to_top'></div>\
							<div class='task_container'>\
								<span class='task_id'>" + data.id + "</span>\
								<span class='task_time'>" + data.time + "</span>\
								<div class='task_tag circle'><span>" + tag + "</span></div>\
								<span class='task_author'>" + data.username + "</span>\
								<span class='task_content'>" + task + "</span>\
							</div></li>");
						$(pageAction.config.taskCreator).find("textarea").val("");
						$(pageAction.config.taskCreator).find("input").val("");
						if (data.new_tag == 1) {
							$(pageAction.config.tagInCreator)
								.find("ul")
								.append("<li>" + tag + "</li>");
						}
						pageInit.randomCategory();
						$(pageInit.config.taskCreatorPanel).hide();
					}
				});
			} else {
				$(pageAction.config.taskCreator).find("textarea").val("");
				$(pageAction.config.taskValidation).html("Please input task and tag");
			}
		});
	},

	submitComment: function() {
		$(pageAction.config.commentSubmitButton).live("click", function() {
			var task_id = $(pageAction.config.commentArea)
				.siblings(pageAction.config.taskContainer)
				.find(pageAction.config.taskID)
				.html();
			var comment = $(pageAction.config.commentTextArea).val();
			if (comment.trim() !== '') {
				$(pageAction.config.commentValidation).html("");
				$.ajax({
					type: "POST",
					url: window.location.href,
					data: {
						'new_comment': true,
						"task_id": task_id,
						"task_comment": comment,
					},
					cache: false,
					dataType: "json",
				}).done(function(data) {
					/*jshint multistr: true */
					$(pageAction.config.commentList)
						.prepend("<div class='comment_li'>\
						<div class='comment_author_circle'><span>" + data.toUpperCase() + "</span></div>\
					    <div class='comment_content_area'><div class='comment_author'>\
					    <span>" + data + "</span><span class='comment_time'>now</span></div>\
						<div class='comment_content'>" + comment + "</div></div>\
						</div>");
					$(pageAction.config.commentTextArea).val("");
				});
			} else {
				$(pageAction.config.commentValidation).html("Please input comment");
			}
		});
	},

	lookForComment: function() {
		$(document).on("click", pageAction.config.taskContent, function(event) {
			var task_container = $(this).parent();
			var task_li = task_container.parent();
			if (task_li.hasClass('selected')) {
				task_li.removeClass('selected')
					.css(pageAction.config.taskDefaultClass);
				$(pageAction.config.commentArea).hide();
			} else {
				var id = task_container.find(pageAction.config.taskID).html();
				var author = task_container.find(pageAction.config.taskAuthor).html();
				var tag = task_container.find(pageAction.config.tagInTask).html();
				var time = task_container.find(pageAction.config.taskTime).html();
				var task = $(this).html();
				$(pageAction.config.commentArea).hide()
					.insertAfter(task_container)
					.slideDown('fast');
				$(pageAction.config.taskItem).removeClass('selected')
					.css(pageAction.config.taskDefaultClass);
				task_li.addClass('selected')
					.css(pageAction.config.taskHighlightClass);
				$(pageAction.config.taskInComment).html(task);
				$(pageAction.config.tagInComment).html(tag);
				$(pageAction.config.timeInComment).html(time);
				$(pageAction.config.commentList)
					.add(pageAction.config.commentValidation)
					.add(pageAction.config.taskValidation)
					.html("");
				$(pageAction.config.commentSubmitButton).hide();
				$.ajax({
					type: "POST",
					url: window.location.href,
					data: {
						'look_for_task': 1,
						'task_id': id,
					},
					cache: false,
					dataType: "json",
				}).done(function(data) {
					$(data).each(function(i) {
						/*jshint multistr: true */
						if (author === data[i].username) {
							var comment_user = "<div class='comment_author_circle blue_circle'><span >" + author.toUpperCase() + "</span></div>";
						} else {
							var comment_user = "<div class='comment_author_circle'><span>" + author.toUpperCase() + "</span></div>";
						}
						$(pageAction.config.commentList)
							.prepend(
								"<div class='comment_li'>" + comment_user + "<div class='comment_content_area'>\
								<div class='comment_author'>\
								<span>" + data[i].username + "</span>\
								<span class='comment_time'>" + data[i].time + "</span></div>\
					            <div class='comment_content'>" + data[i].comment + "</div></div></div>");
					});
				});
			}
		});
	},

	markTaskDone: function() {
		$(pageAction.config.todoButton).live("click", function() {
			var task = $(this).parent();
			var id = task.find(pageAction.config.taskID).html();
			task.insertBefore('.task_list_done li:first')
				.append(pageAction.config.doneDiv);
			task.find(pageAction.config.todoButton).remove();
			task.find(pageAction.config.topButton).remove();
			task.find(pageAction.config.topMark).remove();
			$.ajax({
				type: "POST",
				url: window.location.href,
				data: {
					"task_done": 1,
					"task_id": id,
				},
				cache: false,
				dataType: "json",
			}).done(function(data) {
				console.log(data);
			});
		});
	},

	markTaskTodo: function() {
		$(pageAction.config.doneButton).live("click", function() {
			var task = $(this).parent();
			var id = task.find(pageAction.config.taskID).html();
			task.insertBefore('.task_list_todo li:first')
				.append(pageAction.config.todoDiv)
				.append(pageAction.config.toTopDiv);
			task.find(pageAction.config.doneButton).remove();
			$.ajax({
				type: "POST",
				url: window.location.href,
				data: {
					"task_todo": 1,
					"task_id": id,
				},
				cache: false,
				dataType: "json",
			}).done(function(data) {
				console.log(data);
			});
		});
	},

	markTaskTop: function() {
		$(pageAction.config.topButton).live('click', function() {
			var task = $(this).parent();
			var id = task.find(pageAction.config.taskID).html();
			task.insertBefore('.task_list_top li:first')
				.append(pageAction.config.topDiv);
			task.find(pageAction.config.topButton).remove();
			$.ajax({
				type: "POST",
				url: window.location.href,
				data: {
					"task_top": 1,
					"task_id": id,
				},
				cache: false,
				dataType: "json",
			}).done(function(data) {
				console.log(data);
			});
		});
	},

	reassignOwner: function() {
		$(pageAction.config.reassignButton).live("click", function() {
			var owner = $(pageAction.config.reassignInput).val();
			var id = $(pageAction.config.commentArea)
				.siblings(pageAction.config.taskContainer)
				.find(pageAction.config.taskID)
				.html();
			if (owner.trim() !== '') {
				$.ajax({
					type: "POST",
					url: window.location.href,
					data: {
						"change_owner": true,
						"new_owner": owner,
						"task_id": id
					},
					cache: false,
					dataType: "json",
				}).done(function(data) {
					$(pageAction.config.reassignInput).val("");
					$(pageAction.config.commentArea)
						.siblings(pageAction.config.taskContainer)
						.find(pageAction.config.taskAuthor).html(data.new_owner);
				});
			} else {
				$(pageAction.config.reassignInput).val("");
			}
		});
	},

	reuturnDoneTask: function() {
		$(pageAction.config.expandAllDoneTask).live('click', function() {
			$.ajax({
				type: "POST",
				url: window.location.href,
				data: {
					"expand_all_task": 1
				},
				cache: false,
				dataType: "json",
			}).done(function(data) {
				if (data !== '') {
					$(pageAction.config.commentArea)
						.insertAfter(pageAction.config.summaryArea).hide();
					$(pageAction.config.doneTaskList).children().remove();
					$(data).each(function(i) {
						$(pageAction.config.doneTaskList)
							.append("<li class='task_li'>\
							<div class='task_done'></div>\
							<div class='task_container'>\
							<span class='task_id'>" + data[i].id + "</span>\
							<span class='task_time'>" + data[i].time + "</span>\
							<div class='task_tag circle'><span>" + data[i].tag + "</span></div>\
							<span class='task_author'>" + data[i].username + "</span>\
							<span class='task_content'>" + data[i].task + "</span>\
							</div>\
							</li>");
					});
					pageInit.randomCategory();
				}
			});
		});
	},
	drawTaskSummary: function() {
		data_dict = [
			["Status", "Number"]
		];
		var options = {
			title: 'TODO SUMMARY',
			colors: ['#C74433', '#f39c12', '#4285f4']
		};
		$(".task_summary_area li").each(function(index) {
			var title = $(this).find(".summary_title");
			title.css("border-color", options["colors"][index])
			var value = $(this).find("span").html();
			data_dict.push([title.html(), parseInt(value)]);
		})
		var data = google.visualization.arrayToDataTable(data_dict);
		var chart = new google.visualization.PieChart(document.getElementById("task_summary_dashboard"));
		chart.draw(data, options);
	},

	drawUserSummary: function() {
		data_dict = [
			["Status", "Number"]
		];
		var options = {
			title: 'USER SUMMARY',
			colors: ['#C74433', '#f39c12', '#4285f4']
		};
		$(".user_summary_area li").each(function(index) {
			var title = $(this).find(".summary_title");
			title.css("border-color", options["colors"][index])
			var value = $(this).find("span").html();
			data_dict.push([title.html(), parseInt(value)]);
		})
		var data = google.visualization.arrayToDataTable(data_dict);
		var chart = new google.visualization.PieChart(document.getElementById("user_summary_dashboard"));
		chart.draw(data, options);
	},
};

$(document).ready(pageInit.init);
google.load("visualization", "1", {
	packages: ["corechart"]
});
google.setOnLoadCallback(pageAction.drawTaskSummary);
google.setOnLoadCallback(pageAction.drawUserSummary);
pageAction.init();