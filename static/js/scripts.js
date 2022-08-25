//  Preloader
jQuery(window).on("load", function () {
    $('#preloader').fadeOut(500);
    $('#main-wrapper').addClass('show');
});


(function ($) {

    "use strict"

    //to keep the current page active
    $(function () {
	for (var nk = window.location,
		o = $(".settings-menu a, .menu a").filter(function () {
	    return this.href == nk;
	})
		.addClass("active")
		.parent()
		.addClass("active"); ; ) {
	    // console.log(o)
	    if (!o.is("li"))
		break;
	    o = o.parent()
		    .addClass("show")
		    .parent()
		    .addClass("active");
	}

    });

    $('[data-toggle="tooltip"]').tooltip();

})(jQuery);





(function () {
    let onpageLoad = localStorage.getItem("theme") || "";
    $('body').addClass(onpageLoad);
    $('#theme').text(localStorage.getItem("theme") || "light");
    /*
     let element = document.body;
     element.classList.add(onpageLoad);
     document.getElementById("theme").textContent = localStorage.getItem("theme") || "light";
     */

})(jQuery);

function themeToggle() {
    let element = document.body;
    element.classList.toggle("dark-theme");

    let theme = localStorage.getItem("theme");
    if (theme && theme === "dark-theme") {
	localStorage.setItem("theme", "");
    } else {
	localStorage.setItem("theme", "dark-theme");
    }
}