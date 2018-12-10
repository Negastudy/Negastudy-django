
jQuery(document).ready(function() {

    /*
        Fullscreen background
    */
    $.backstretch([
        "2.jpg",
        "../../static/assert/img/backgrounds/2.jpg",
        // ,"../static/assets/img/backgrounds/2.jpg"
        // , "../static/assets/img/backgrounds/3.jpg"
        // , "../static/assets/img/backgrounds/1.jpg"
        // , "../static/assets/img/backgrounds/4.jpg"
        // , "../static/assets/img/backgrounds/5.jpg"
        // , "../static/assets/img/backgrounds/6.jpg"
    ], {duration: 6000, fade: 550});

    /*
        Form validation
    */
    $('.login-form input[type="text"], .login-form input[type="password"], .login-form textarea').on('focus', function() {
        $(this).removeClass('input-error');
    });

    $('.login-form').on('submit', function(e) {

        $(this).find('input[type="text"], input[type="password"], textarea').each(function(){
            if( $(this).val() == "" ) {
                e.preventDefault();
                $(this).addClass('input-error');
            }
            else {
                $(this).removeClass('input-error');
            }
        });

    });


});
