/* Кнопка наверх */
$(window).scroll(function() {
    if ($(this).scrollTop() != 0)
        $('#toTop').fadeIn();
    else
        $('#toTop').fadeOut();
});
$('#toTop').click(function() {
    $('body,html').animate({
        scrollTop: 0
    }, 800);
});


var btn = document.querySelectorAll('button');
for (var i = 0; i < btn.length; i++) {
    btn[i].style.outline = 'none';
}
/* Выпадающее меню */
$('.menu-icon').click(function() {
    $('nav').slideToggle(500);
    $('ul.menu').css({
        'display': 'flex',
        'flex-direction': 'column'
    });
    if ($('.menu-icon').html() == '<i class="fas fa-bars"></i>') {
        $(this).html('<i class="fas fa-times"></i>');
    } else {
        $(this).html('<i class="fas fa-bars"></i>');
    }
});