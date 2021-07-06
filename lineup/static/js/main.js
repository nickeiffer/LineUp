$(document).ready(function () {
	// Activating date picker
	$( '.dtpick' ).datepicker();

	// Remove bottom border from last todos on each page
	$(last_todo).removeClass('border-bottom');
	$(last_completed).removeClass('border-bottom');

	// Toggle action icon on hover
	$('.bi-check-square').hover(function () {
		$(this).addClass('bi-check-square-fill');
		$(this).removeClass('bi-check-square'); 
	}, function () {
		$(this).addClass('bi-check-square');
		$(this).removeClass('bi-check-square-fill');
	});
	$('.bi-x-square').hover(function () {
		$(this).addClass('bi-x-square-fill');
		$(this).removeClass('bi-x-square'); 
	}, function () {
		$(this).addClass('bi-x-square');
		$(this).removeClass('bi-x-square-fill');
	});
	$('.bi-pencil').hover(function () {
		$(this).addClass('bi-pencil-fill');
		$(this).removeClass('bi-pencil'); 
	}, function () {
		$(this).addClass('bi-pencil');
		$(this).removeClass('bi-pencil-fill');
	});	

	// Slide new todo container into view
	$('#open-new').click(function () {
		$(this).hide();
		$('#close-new').show();
		$('.new-todo-cont').slideDown('fast');
		$('.content-cont').css('pointer-events', 'none');
		$('#new-todo-header').text('New Todo');
		$('.todo-confirm').val('Add');
		$('#todo_id').val(-1);
		$('#title').val(null);
		$('#dueDate').datepicker('setDate', null);
		$('input[name=priority]:checked', '#new-todo-form').val(0);
		$('.priority-outline').hide();
		$('#note').val(null);
	});

	// Slide new todo container out of view
	$('#close-new').click(function () {
		$(this).hide();
		$('#open-new').show();
		$('.new-todo-cont').slideUp('fast');
		$('.content-cont').css('pointer-events', 'all');
	});

	// Slide sort options into view
	$('#open-sort').click(function (e) {
		$(this).hide();
		$('#close-sort').show();
		$('.sort-cont').slideDown('fast');
		e.stopPropagation();
	});

	// Closing sort when clicking outside
	$(document).click(function () {
		$(".sort-cont").hide();
		$('.sort-cont').slideUp('fast');
		$('#open-sort').show();
		$('#close-sort').hide();
		$('.sort-arrow').hide();
		$('.sort-option').val(0);
		$(this).find('#a' + $(this).find('.sort-cont').attr('value')).show();
		if (parseInt($(this).find('.sort-cont').attr('value')) % 2) 
			$(this).find('#a' + $(this).find('.sort-cont').attr('value')).parent().val(1);
		else 
			$(this).find('#a' + $(this).find('.sort-cont').attr('value')).parent().val(2);
	});

	$('.sort-cont').click(function (e) {
		e.stopPropagation();
	});

	// Toggle sort arrows
	$('.sort-option').click(function (e) {
		if ($(this).val() == 1) {
			$('.sort-arrow').hide()
			$('.sort-option').val(0)
			$(this).children('i.bi-arrow-down').show();
			$(this).val(2);
			$('#sort_id').val($(this).children('i.bi-arrow-down').attr('value'));
		}
		else if ($(this).val() == 2) {
			$('.sort-arrow').hide()
			$('.sort-option').val(0)
			$(this).val(0);
			$('#sort_id').val(0);
		}
		else {
			$('.sort-arrow').hide()
			$('.sort-option').val(0)
			$(this).children('i.bi-arrow-up').show();
			$(this).val(1);
			$('#sort_id').val($(this).children('i.bi-arrow-up').attr('value'));
		}
	});

	// Showing priority menu icon outline
	$('#priority-menu-icon-0').click(function () {
		$('#priority-outline-0').show();
		$('#priority-outline-1').hide();
		$('#priority-outline-2').hide();
		$('input[name=priority]:checked', '#new-todo-form').val(1);
	});
	$('#priority-menu-icon-1').click(function () {
		$('#priority-outline-1').show();
		$('#priority-outline-0').hide();
		$('#priority-outline-2').hide();
		$('input[name=priority]:checked', '#new-todo-form').val(2);
	});
	$('#priority-menu-icon-2').click(function () {
		$('#priority-outline-2').show();
		$('#priority-outline-1').hide();
		$('#priority-outline-0').hide();
		$('input[name=priority]:checked', '#new-todo-form').val(3);
	});

	// Hiding priority menu icon outline
	$('#priority-outline-0').click(function () {
		$('#priority-outline-0').hide();
		$('input[name=priority]:checked', '#new-todo-form').val(0);
	});
	$('#priority-outline-1').click(function () {
		$('#priority-outline-1').hide();
		$('input[name=priority]:checked', '#new-todo-form').val(0);
	});
	$('#priority-outline-2').click(function () {
		$('#priority-outline-2').hide();
		$('input[name=priority]:checked', '#new-todo-form').val(0);
	});

	// Toggle changes to todo row
	$('.todo-row').hover(function () {
		$(this).find('#icon-placeholder').hide();
		$(this).find('#icons').show();
		$(this).find('#title-text').css('top', '7px');
		if ($(this).attr('value') == 'complete' && !$(this).find('#note-text').length)
			$(this).find('#title-text').css('padding-top', '28px');
		$(this).find('#secondary-content').show();

	}, function () {
		$(this).find('#icon-placeholder').show();
		$(this).find('#icons').hide();
		$(this).find('#title-text').css('top', '47px');
		$(this).find('#secondary-content').hide();
		$(this).find('#title-text').css('padding-top', '0');
		$(this).find('#note-text').hide();
		$(this).find('.view-note').text('~ View Note');
	});

	// Toggle changes to note
	$('.view-note').click(function () {
		if ($(this).attr('value') == 1) {
			$(this).parent().next().show();
			$(this).attr('value', '2');
		}
		else {
			$(this).parent().next().hide();
			$(this).attr('value', '1');
		}
	});

	// Prepare new todo form with existing data
	edit_todo = function () {
		$('#open-new').hide();
		$('#close-new').show();
		$('.new-todo-cont').slideDown('fast');
		$('.content-cont').css('pointer-events', 'none');
		$('.todo-confirm').val('Save');
		$('#new-todo-header').text('Edit Todo');
		$('#todo_id').val($(this).closest('.todo-row').attr('id'));
		$('#title').val($(this).closest('.todo-row').find('#title-text').text());
		$('#dueDate').datepicker('setDate', null);
		$('#dueDate').datepicker('setDate', $(this).closest('.todo-row').find('.due-date-text').text().split('Due:')[1]);
		$('.priority-outline').hide();
		$('#priority-outline-' + (parseInt($(this).closest('.todo-row').attr('priority'))-1)).show();
		$('input[name=priority]:checked', '#new-todo-form').val($(this).closest('.todo-row').attr('priority'));
		$('#note').val(null);
		$('#note').val($(this).closest('.todo-row').find('#note-text').text());
	}
	$('.edit-icon').click(edit_todo);
	$('.add-note').click(edit_todo);












});