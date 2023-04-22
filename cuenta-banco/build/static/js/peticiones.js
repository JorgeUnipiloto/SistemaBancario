
//Peticion Get api rest



$(document).ready(function () {
    // Agregamos el evento click al botón cerrar
    $('#closeModalBtn').click(function () {
        $('#myModal').modal('hide');
    });

    $.getJSON('http://127.0.0.1:8000/api/personas', function (data) {
        $.each(data, function (index, persona) {
            $('#nombres').append('<option value="' + persona.id + '">' + persona.nombres + ' ' + persona.apellidos + '</option>');
        });
    });
});

var valuesAdded = false;
        $(document).ready(function () {
            // Verificamos si los valores ya se han agregado
            if (!valuesAdded) {
                $.getJSON('http://127.0.0.1:8000/api/cuentas', function (data) {
                    // Verificamos si el select ya contiene opciones
                    var selectHasOptions = $('#cuentas').children().length > 0;
                    if (!selectHasOptions) {
                        $.each(data, function (index, cuenta) {
                            $('#cuentas').append('<option value="' + cuenta.id + '">' + cuenta.id + '</option>');
                        });
                        
                    }

                    
    
                    // Cambiamos el valor de la variable para indicar que ya se han agregado los valores
                    valuesAdded = true;
                });
            }
        });

        $(document).ready(function () {
            // Verificamos si los valores ya se han agregado
            if (!valuesAdded) {
                $.getJSON('http://127.0.0.1:8000/api/cuentas', function (data) {
                    // Verificamos si el select ya contiene opciones
                    var selectHasOptions = $('#cuentas1').children().length > 0;
                    if (!selectHasOptions) {
                        $.each(data, function (index, cuenta) {
                            $('#cuentas1').append('<option value="' + cuenta.id + '">' + 'Cuenta: ' + cuenta.id + ' Tiene un saldo de: ' +' ' + cuenta.saldo  +'</option>');
                        });
                        
                    }

                    
    
                    // Cambiamos el valor de la variable para indicar que ya se han agregado los valores
                    valuesAdded = true;
                });
            }
        });


        

