$(document).ready(function(){
    $('.slickyy').slick({
        infinite: true,
        dots: true,
        slidesToShow: 1,
        arrows: false,
    });
    $('.troco-por').slick({
        infinite: true,
        dots: true,
        slidesToShow: 2,
    });
});

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        img_tag = $(input).next()
        label_tag = $(input).parent()
        $(label_tag).removeClass("product-image--after")
        $(label_tag).css("backgroundColor","transparent")

        reader.onload = function (e) {
            $(img_tag).attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}


$("input[type='file']").change(function(){
    readURL(this);
});