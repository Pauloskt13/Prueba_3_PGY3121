/** FUNCION PARA NAVEGAR EN PAGINA SIN RECARGAR DOCUMENTO HTML **/
const xhr = new XMLHttpRequest();

window.onload= function(){
    changeSite('inicio.html');
}

const index = document.getElementById('index');
index.addEventListener('click', () => {
    changeSite('inicio.html');
});
        
const aboutUs = document.getElementById('aboutUs');
aboutUs.addEventListener('click', () => {
    changeSite('nosotros.html');
});

const store = document.getElementById('store');
store.addEventListener('click', () => {
    changeSite('tienda.html');
});

const donation = document.getElementById('donation');
donation.addEventListener('click', () => {
    changeSite('donaciones.html');
});

const contact = document.getElementById('contact');
contact.addEventListener('click', () => {
    changeSite('contacto.html');
    getRegions();       
});




function changeSite(url) {
    const container = document.getElementById('container');
    xhr.onload = function() {
        if (this.status === 200) {
            container.innerHTML = this.responseText;
        } else {
            console.warn('did not receive 200 OK from server');
        }
    };
    xhr.open('get', url);
    xhr.send();
}

/** FUNCION PARA CONSUMIR API DE REGIONES **/


function getRegions() {
  const _xhr = new XMLHttpRequest();
  _xhr.onload = function () {
    if (this.status === 200) {
      regions = JSON.parse(this.responseText);
      console.log(regions);
      select = document.getElementById('selectRegionId');
      
      }
      for (let index = 0; index < regions.length; index++) {
        const region = regions[index];
        let optionElem = document.createElement('option');
        optionElem.value = region.codigo;
        optionElem.textContent = region.nombre;
        select.appendChild(optionElem);
      
      
    }
  }
  _xhr.open('get', 'https://apis.digital.gob.cl/dpa/regiones');
  _xhr.send();
}

/**FUNCION PARA CONSUMIR API COMUNAS */

function getComunas(code){
    const _xhr = new XMLHttpRequest();
    _xhr.onload = function(){
      if(this.status === 200){
          comunas = JSON.parse(this.responseText);
          console.log(comunas);
          select = document.getElementById('selectComunas');
          let tries = 0; 
          while (true ){
              select = document.getElementById('selectComunas');
              console.log('select is null');
            if(tries == 5)break;
            tries++;

          }
          for (let index = 0; index < comunas.length; index++){
              const comuna = comunas[index];
              let optionElem = document.createElement('option');
              optionElem.value = comuna.codigo;
              optionElem.textContent = comuna.nombre;
              select.appendChild(optionElem);
          }
      }
    }
    let url = `https://apis.digital.gob.cl/dpa/comunas`;
  _xhr.open('get', url);
  _xhr.send();
}