(function ($) {
	"use strict"
	function saveStructure() {
		// var menu_id = $(this).attr('rel');
		var form_data = $(`#MenuItem${menu_id}Form`).serializeArray();
		var formData = JSON.stringify(form_data);

		var menu_name = $('#MenuNameEdit').val();

		// let menu_data = {
		//     "menu_id": menu_id,
		//     "menu_name": menu_name
		// };
		menu_data = JSON.stringify(menu_data)
		var data = $('.dd').nestable('toArray');
		// var data = $('.dd').nestable('serialize');
		// var data = $('.dd').nestable('asNestedSet');


		var dd_data = JSON.stringify(data);

		if (dd_data != "") {
			$.ajax({
				headers: {
					'X-CSRF-TOKEN': CSRF_TOKEN
				},
				url: menu_structure_save_url,
				type: 'POST',
				dataType: 'json',
				data: {
					csrfmiddlewaretoken: CSRF_TOKEN,
					'dd_data': dd_data,
					'menu_data': menu_data,
					'form_data': formData
				},
				success: function (res) {

					console.log("res = ");
					console.log("res = ", res);
					if (res.success) {
						$('.MenuSelectDiv .nice-select .current').text(menu_name);
						$('.MenuSelectDiv .nice-select .list .selected').text(menu_name)
						// alert(res.success);
						Swal.fire({
							type: 'success',
							title: 'Save Successfully',
							text: 'All Menu Item Save Successfully',
							timer: 2e3,
							showConfirmButton: !1
							// confirmButtonColor: "var(--primary)"
						});
					}
					if (res.error) {

						Swal.fire({
							type: 'warning',
							title: 'Not Allow',
							text: res.error,
							confirmButtonColor: "var(--primary)"
						})

					}
				},
			});
		}
	}


	/*******************
	Nestable
	*******************/

	var e = function (e) {
		var t = e.length ? e : $(e.target)
		saveStructure()
	};
	$("#nestable").nestable({
		group: 1
	}).on("change", e)
	// ,
	// 	$("#nestable2").nestable({
	// 		group: 1
	// 	}).on("change", e), e($("#nestable").data("output", $("#nestable-output"))), e($("#nestable2").data("output", $("#nestable2-output"))), $("#nestable-menu").on("click", function (e) {
	// 		var t = $(e.target).data("action");
	// 		"expand-all" === t && $(".dd").nestable("expandAll"), "collapse-all" === t && $(".dd").nestable("collapseAll")
	// 	}), $("#nestable3").nestable();



})(jQuery);