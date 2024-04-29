/** ===============

 .. Preloader
 .. Menu
 .. Number rotator
 .. Skillbar
 .. Tab
 .. Accordion
 .. Isotope
 .. Prettyphoto
 .. Slick_slider 

 =============== */


jQuery(function ($) {

    "use strict";

    /*------------------------------------------------------------------------------*/
    /* Preloader
    /*------------------------------------------------------------------------------*/
    // makes sure the whole site is loaded
    $(window).on("load", function () {
        $(".loader-blob").fadeOut(), $("#preloader").delay(300).fadeOut("slow", function () { $(this).remove() });

    })
    /* side-menu */
    $(".side-menu-container").each(function () {
        $(".side-menu > a", this).on("click", function (e) {
            e.preventDefault();
            $(".side-overlay").toggleClass("on");
            $("body").toggleClass("on-side");
        });
    });
    $(".side .close-side").on("click", function (e) {
        e.preventDefault();
        $(".side-overlay").removeClass("on");
        $("body").removeClass("on-side");
    });
    /*------------------------------------------------------------------------------*/
    /* Menu
    /*------------------------------------------------------------------------------*/

    var menu = {
        initialize: function () {
            this.Menuhover();
        },

        Menuhover: function () {
            var getNav = $("nav.main-menu"),
                getWindow = $(window).width(),
                getHeight = $(window).height(),
                getIn = getNav.find("ul.menu").data("in"),
                getOut = getNav.find("ul.menu").data("out");

            if (matchMedia('only screen and (max-width: 1200px)').matches) {

                // Enable click event
                $("nav.main-menu ul.menu").each(function () {

                    // Dropdown Fade Toggle
                    $("a.mega-menu-link", this).on('click', function (e) {
                        e.preventDefault();
                        var t = $(this);
                        t.toggleClass('active').next('ul').toggleClass('active');
                    });

                    // Megamenu style
                    $(".megamenu-fw", this).each(function () {
                        $(".col-menu", this).each(function () {
                            $(".title", this).off("click");
                            $(".title", this).on("click", function () {
                                $(this).closest(".col-menu").find(".content").stop().toggleClass('active');
                                $(this).closest(".col-menu").toggleClass("active");
                                return false;
                                e.preventDefault();

                            });

                        });
                    });

                });
            }
        },
    };


    $('.btn-show-menu-mobile').on('click', function (e) {
        $(this).toggleClass('is-active');
        $('.menu-mobile').toggleClass('show');
        return false;
        e.preventDefault();
    });

    // Initialize
    $(document).ready(function () {
        menu.initialize();

    });





    /*------------------------------------------------------------------------------*/
    /* Animation on scroll: Number rotator
    /*------------------------------------------------------------------------------*/

    $("[data-appear-animation]").each(function () {
        var self = $(this);
        var animation = self.data("appear-animation");
        var delay = (self.data("appear-animation-delay") ? self.data("appear-animation-delay") : 0);

        if ($(window).width() > 959) {
            self.html('0');
            self.waypoint(function (direction) {
                if (!self.hasClass('completed')) {
                    var from = self.data('from');
                    var to = self.data('to');
                    var interval = self.data('interval');
                    self.numinate({
                        format: '%counter%',
                        from: from,
                        to: to,
                        runningInterval: 2000,
                        stepUnit: interval,
                        onComplete: function (elem) {
                            self.addClass('completed');
                        }
                    });
                }
            }, { offset: '85%' });
        } else {
            if (animation == 'animateWidth') {
                self.css('width', self.data("width"));
            }
        }
    });



    /*------------------------------------------------------------------------------*/
    /* Skillbar
    /*------------------------------------------------------------------------------*/

    $('.prt-progress-bar').each(function () {
        $(this).find('.progress-bar').width(0);
    });

    $('.prt-progress-bar').each(function () {

        $(this).find('.progress-bar').animate({
            width: $(this).attr('data-percent')
        }, 2000);
    });


    // Part of the code responsible for loading percentages:

    $('.progress-bar-percent[data-percentage]').each(function () {

        var progress = $(this);
        var percentage = Math.ceil($(this).attr('data-percentage'));

        $({ countNum: 0 }).animate({ countNum: percentage }, {
            duration: 2000,
            easing: 'linear',
            step: function () {
                // What todo on every count
                var pct = '';
                if (percentage === "0") {
                    pct = Math.floor(this.countNum) + '%';
                } else {
                    pct = Math.floor(this.countNum + 1) + '%';
                }
                progress.text(pct);
            }
        });
    });


    jQuery(".prt-circle-box").each(function () {

        var circle_box = jQuery(this);
        var fill_val = circle_box.data("fill");
        var emptyFill_val = circle_box.data("emptyfill");
        var thickness_val = circle_box.data("thickness");
        var linecap_val = circle_box.data("linecap")
        var fill_gradient = circle_box.data("gradient");
        var startangle_val = (-Math.PI / 4) * 1.5;
        if (fill_gradient != "") {
            fill_gradient = fill_gradient.split("|");
            fill_val = { gradient: [fill_gradient[0], fill_gradient[1]] };
        }
        if (typeof jQuery.fn.circleProgress == "function") {
            var digit = circle_box.data("digit");
            var before = circle_box.data("before");
            var after = circle_box.data("after");
            var digit = Number(digit);
            var short_digit = digit / 100;
            var size_val = circle_box.data("size");
            jQuery(".prt-circle", circle_box)
                .circleProgress({
                    value: 0, duration: 8000, size: size_val, startAngle: startangle_val,
                    thickness: thickness_val, linecap: linecap_val, emptyFill: emptyFill_val, fill: fill_val
                })
                .on("circle-animation-progress", function (event, progress, stepValue) {

                    circle_box.find(".prt-fid-number").html(before + Math.round(stepValue * 100) + after);
                });
        }
        circle_box.waypoint(
            function (direction) {

                if (!circle_box.hasClass("completed")) {
                    if (typeof jQuery.fn.circleProgress == "function") {
                        jQuery(".prt-circle", circle_box).circleProgress({ value: short_digit });
                    }
                    circle_box.addClass("completed");
                }
            },
            { offset: "90%" }
        );
    });


    jQuery(document).ready(function ($) { aqovo_logMarginPadding_content(); });
    function aqovo_logMarginPadding_content() {
        jQuery(".prt-expandcontent-yes").each(function () {
            var prt_column_div = '';
            var scrren_size = jQuery(window).width();
            var box_size = jQuery(this).parent().width();
            var extra_size = (scrren_size - box_size) / 3;

            if (jQuery(this).hasClass('prt-right-span')) {
                prt_column_div = ', .prt-expandcontent_column > .prt-expandcontent_wrapper ';
                jQuery('.prt-expandcontent_column > div' + prt_column_div, jQuery(this)).css('margin-right', '-' + extra_size + 'px');
            } else if (jQuery(this).hasClass('prt-left-span')) {
                prt_column_div = ', .prt-expandcontent_column > .prt-expandcontent_wrapper ';
                jQuery('.prt-expandcontent_column > div' + prt_column_div, jQuery(this)).css('margin-left', '-' + extra_size + 'px');
            }

        });
    } jQuery(window).resize(function () { aqovo_logMarginPadding_content(); });


    /*------------------------------------------------------------------------------*/
    /* Tab
    /*------------------------------------------------------------------------------*/

    $(document).ready(function () {

        $('.prt-tabs > .tabs').children('li').on('click', function (e) {

            var tab = $(this).closest('.prt-tabs > .tabs > .tab'),

                index = $(this).closest('.prt-tabs > .tabs > li').index();

            $(this).parents('.prt-tabs').children(' .tabs').children('li.active ').removeClass('active');

            $(this).addClass('active');
            $(this).addClass('active').parents('.prt-tabs').children('.content-tab').find('.content-inner').not('.content-inner:eq(' + index + ')').slideUp();
            $(this).addClass('active').parents('.prt-tabs').children('.content-tab').find('.content-inner:eq(' + index + ')').slideDown();

            e.preventDefault();
        });
    });


    // team-tab

    $('.prt-tabs-team').each(function () {
        $(this).children('.content-tab').children().hide();
        $(this).children('.content-tab').children().first().show();
        $(this).find('.tabs').children('li').on('click', function (e) {
            var liActive = $(this).index(),
                contentActive = $(this).siblings().removeClass('active').parents('.prt-tabs-team').children('.content-tab').children().eq(liActive);
            contentActive.addClass('active').fadeIn('slow');
            contentActive.siblings().removeClass('active');
            $(this).addClass('active').parents('.prt-tabs-team').children('.content-tab').children().eq(liActive).siblings().hide();
            e.preventDefault();
        });
    });
    /*------------------------------------------------------------------------------*/
    /* Accordion
    /*------------------------------------------------------------------------------*/

    var allPanels = $('.accordion > .toggle').children('.toggle-content').hide();

    $('.toggle-title').on('click', function (e) {

        e.preventDefault();
        var $this = $(this);
        $this.parent().parent().find('.toggle .toggle-title a').removeClass('active');

        if ($this.next().hasClass('show')) {

            $this.next().removeClass('show');
            $this.next().slideUp('easeInExpo');

        } else {
            $this.parent().parent().find('.toggle .toggle-content').removeClass('show');
            $this.parent().parent().find('.toggle .toggle-content').slideUp('easeInExpo');
            $this.next().toggleClass('show');
            $this.next().removeClass('show');
            $this.next().slideToggle('easeInExpo');
            $this.next().parent().children().children().addClass('active');

        }

    });


    /*------------------------------------------------------------------------------*/
    /* Isotope
    /*------------------------------------------------------------------------------*/


    $(function () {

        if ($().isotope) {
            var $container = $('.isotope-project');
            $container.imagesLoaded(function () {
                $container.isotope({
                    itemSelector: '',
                    transitionDuration: '1s',
                });
            });

            $('.portfolio-filter li').on('click', function () {
                var selector = $(this).find("a").attr('data-filter');
                $('.portfolio-filter li').removeClass('active');
                $(this).addClass('active');
                $container.isotope({ filter: selector });
                return false;
            });
        };

    });


    /*------------------------------------------------------------------------------*/
    /* Prettyphoto
    /*------------------------------------------------------------------------------*/
    $(function () {

        // Normal link
        jQuery('a[href*=".jpg"], a[href*=".jpeg"], a[href*=".png"], a[href*=".gif"]').each(function () {
            if (jQuery(this).attr('target') != '_blank' && !jQuery(this).hasClass('prettyphoto')) {
                var attr = $(this).attr('rel');
                if (typeof attr !== typeof undefined && attr !== false && attr != 'prettyPhoto') {
                    jQuery(this).attr('data-rel', 'prettyPhoto');
                }
            }
        });
        jQuery('a[data-rel^="prettyPhoto"]').prettyPhoto();
    });


    $(window).on('load', function () {

        function gridMasonry() {
            var grid = $(".masonry-grid")
            if (grid.length) {

                grid.isotope({
                    itemSelector: '.masonry-grid-item',
                    percentPosition: true,
                    layoutMode: 'masonry',
                    masonry: {
                        columnWidth: '.grid-sizer',
                    },
                });

            }
        }
        gridMasonry();
    });

    // customization icons

    // $(document).ready(function() {
    // var e = '<div class="prt_floting_customsett">'+
    //             '<a href="https://support.preyantechnosys.com/" class="tmtheme_fbar_icons"><i class="fa fa-headphones"></i><span>Support</span></a>'+
    //             '<a href="https://preyantechnosys.com/" class="tmtheme_fbar_icons"><i class="themifyicon themifyicon ti-pencil"></i><span>Customization</span></a>'+
    //             '<a href="https://1.envato.market/LXr0D0" class="tmtheme_fbar_icons"><i class="themifyicon ti-shopping-cart"></i><span class="buy_link">Buy<span></span></span></a>'+
    //             '<div class="clearfix"></div>'+
    //         '</div>';

    // $('body').append(e);
});


/*------------------------------------------------------------------------------*/
/* Slick_slider
/*------------------------------------------------------------------------------*/
$(".slick_slider").slick({
    speed: 1000,
    infinite: true,
    arrows: false,
    dots: false,
    autoplay: false,
    centerMode: false,

    responsive: [{

        breakpoint: 1360,
        settings: {
            slidesToShow: 3,
            slidesToScroll: 3
        }
    },
    {
        breakpoint: 1024,
        settings: {
            slidesToShow: 3,
            slidesToScroll: 3
        }
    },
    {
        breakpoint: 680,
        settings: {
            slidesToShow: 2,
            slidesToScroll: 2
        }
    },
    {
        breakpoint: 575,
        settings: {
            slidesToShow: 1,
            slidesToScroll: 1
        }
    }]
});

/*------------------------------------------------------------------------------*/
/* Slick_slider
/*------------------------------------------------------------------------------*/
$(".hero-slider").slick({
    speed: 1000,
    infinite: true,
    arrows: false,
    dots: false,
    autoplay: true,
    slidesToShow: 1,
    slidesToScroll: 1,
});

});



// popupbox

$(".popupbox").on('click', function () {
    $(".appoinment-model-main").addClass('model-open');
});
$(".close-btn, .bg-overlay").click(function () {
    $(".appoinment-model-main").removeClass('model-open');
});



// left
gsap.set(".animation .animation-img-left", { x: -100, opacity: 1 });
gsap.to(".animation .animation-img-left", {
    scrollTrigger: {
        trigger: ".animation .amination-img-left",
        start: "top center+=300",
        markers: false
    },
    x: 0,
    opacity: 1,
    ease: "power2.out",
    duration: 2,
    stagger: {
        each: 0.3
    }
})

// right
gsap.set(".animation .animation-img-right", { x: 100, opacity: 1 });
gsap.to(".animation .animation-img-right", {
    scrollTrigger: {
        trigger: ".animation .amination-img-right",
        start: "top center+=300",
        markers: false
    },
    x: 0,
    opacity: 1,
    ease: "power2.out",
    duration: 2,
    stagger: {
        each: 0.3
    }
})

// fase-up
gsap.set(".animation .animation-fase-up", { y: 100, opacity: 1 });
gsap.to(".animation .animation-fase-up", {
    scrollTrigger: {
        trigger: ".animation .amination-fase-up",
        start: "top center+=300",
        markers: false
    },
    y: 0,
    opacity: 1,
    ease: "power2.out",
    duration: 2,
    stagger: {
        each: 0.3
    }
})
/*------------------------------------------------------------------------------*/
/* services-item
/*------------------------------------------------------------------------------*/

jQuery(document).ready(function () {

    setTimeout(function () {


    }, 100);

    jQuery('.services-item.style1:first').addClass("active");
    jQuery('.services-item.style1').hover(function () {
        jQuery('.services-item.style1').removeClass("active");
        jQuery(this).addClass("active");
    });

});

/*------------------------------------------------------------------------------*/
/* calendar
/*------------------------------------------------------------------------------*/

$(document).ready(function () {
    $('#schedule-calendar').fullCalendar({

        eventClick: function (event) {
            var modal = $("#schedule-edit");
            modal.modal();
        },
        dayClick: function (date, jsEvent, view) {
            $('#schedule-add').modal('show');
        }
    });
});

