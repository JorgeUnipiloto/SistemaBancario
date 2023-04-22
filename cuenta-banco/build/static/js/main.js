$(document).ready(function() {
    // código a ejecutar cuando el documento está listo
  
    // ejemplo de evento click en un botón
    $('#my-button').click(function() {
      alert('¡Haz hecho clic en el botón!');
    });
    
    // ejemplo de evento hover en un enlace
    $('a').hover(function() {
      $(this).css('color', 'red');
    }, function() {
      $(this).css('color', 'inherit');
    });
    
    // más código aquí...
  });
  


  