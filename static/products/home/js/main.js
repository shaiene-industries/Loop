// Infinite scroll e imagem de carregando
   var infinite = new Waypoint.Infinite({
    element: $('#products-container'),
    items: '.products-item',
    onBeforePageLoad: function () {
        $('.loading').fadeIn('fast');
    },
    onAfterPageLoad: function ($items) {
        setTimeout(function(){
            $('.loading').fadeOut('slow');
        },1000)
    }
});

//Carousel Slick
$(document).ready(function(){
    $('#product_img--carousel').slick({
        infinite: true,
        lazyLoad: 'progressive',
        slidesToScroll: 1,
        adaptiveHeight: true,
        dots: true,
    });
});