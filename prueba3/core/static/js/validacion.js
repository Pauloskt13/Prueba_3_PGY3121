
$(document).ready(function() {

 $("#basic-form").validate({
rules: {
name : {
  required: true,
  minlength: 3
  
},
apellido : {
  required: true,
  minlength: 3
},
email: {
  required: true,
  email: true
},
telefono : {
  required: true,
  number: true,
  minlength: 8 
},
inputAddress: {
  required: true,
  minlength: 3
}
}

});
});

$(document).ready(function(){
$("#basic-form").submit(function () {
  if($("#tel").val().length < 1) {
      alert("Ingresar numero valido");
      return false;
  }
  if(isNaN($("#telefono").val())) {
      alert("El teléfono solo debe contener números");
      return false;
  }
  if($("#telefono").val().length < 8) {
      alert("El teléfono debe tener 8 caracteres. Ej. 99999999 ");
      return false;
  }
  return false;
});
});