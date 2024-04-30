$(document).ready(function(){
    $('#myCarousel').on('slide.bs.carousel', function (e) {
       var nextSlideId = $(e.relatedTarget).attr('class').split(' ')[1]; // Obtém a classe do próximo slide
       var imageUrl = ''; // Defina aqui as URLs das imagens para cada slide
       
       // Mapeia cada slide com sua respectiva imagem de fundo
       switch(nextSlideId) {
             case 'slide1':
                imageUrl = 'url("static/images/measure_cloth1.png")';
                break;
             case 'slide2':
                imageUrl = 'url("static/images/measure_cloth2.png")';
                break;
             case 'slide3':
                imageUrl = 'url("static/images/measure_cloth3.png")';
                break;
       }
       
       // Define a nova imagem de fundo para o top_section
       $('#top_section').css('background-image', imageUrl);
    });
 });