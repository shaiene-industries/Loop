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