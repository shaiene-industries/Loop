
$(document).ready(function(){
    $('#product_img--carousel').slick({
        infinite: true,
        lazyLoad: 'progressive',
        slidesToScroll: 1,
        adaptiveHeight: true,
        dots: true,
    });

    $('.troco-por').slick({
        infinite: true,
        lazyLoad: 'progressive',
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 3,
        dots: true,
        autoplay: true,
        autoplaySpeed: 4000,
        responsive: [
            {
              breakpoint: 768,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
                 }
            },
            {
            breakpoint: 576,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows: false,
                }
            },
        ]
    });
  });