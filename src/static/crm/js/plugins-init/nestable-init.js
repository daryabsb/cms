(function ($) {
	"use strict"
	var e = function (e) {
		var t = e.length ? e : $(e.target)
		saveStructure()
	};
	$("#nestable").nestable({
		group: 1
	}).on("change", e)
})(jQuery);