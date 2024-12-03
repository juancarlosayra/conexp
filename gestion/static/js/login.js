var btn = document.getElementById('access');
var user = document.getElementById('user');
var pass = document.getElementById('txtcontraseña');

const pattern = new RegExp('^[a-z]+$');

const form = document.getElementById('formlario');
form.addEventListener('submit',(e)=>{
    e.preventDefault();
});

function Validar(){
    btn.addEventListener('click', function(evt){
        if(user.value == "juancab" && pass.value == "Mbro1204"){
            window.location.replace("file:///c:/Users/Home/Desktop/Centro%20de%20isotopos%20CENTIS/Home.html");
        }
        if(user.value == "manuelafl" && pass.value == "Xcelsior"){
            window.location.replace("file:///c:/Users/Home/Desktop/Centro%20de%20isotopos%20CENTIS/Home.html");
        }
        else if(user.value == ''){
            alert("El campo usuario es obligatorio");
            evt.preventDefault();
            return false;
        }else if(!pattern.test(user.value)){
            alert("El campo usuario no acepta esos caracteres");
            evt.preventDefault();
            return false;
        }else if(pass.value == ''){
            alert("El campo contraseña es obligatorio");
            evt.preventDefault();
            return false;
        }/*else if(user.value.length > 30){
            console.log('El nombre del usuario es demasiado largo')
            evt.preventDefault();
            return false;
        }*/
    });
}

function vercontraseña(){
  var tipo = document.getElementById("txtcontraseña");
  if(tipo.type == "password"){
      tipo.type = "text";
  }else{
      tipo.type = "password";
  }
}