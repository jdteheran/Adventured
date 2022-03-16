const url_string = window.location.href;
const url = new URL(url_string);
temporal_token = url.searchParams.get("temporal_token");

function validacion_login() {
  if (temporal_token) {
    nombre_usuario = document.getElementById("user").value;
    password = document.getElementById("pwd").value;

    if (!nombre_usuario) {
      return false;
    }

    if (!password) {
      return false;
    }

    let encabezado = new Headers();
    encabezado.append("Content-Type", "application/json");

    let cuerpo = JSON.stringify({
      username: nombre_usuario,
      password: password,
    });

    var peticion_opciones = {
      method: "POST",
      headers: encabezado,
      body: cuerpo,
      redirect: "follow",
    };

    fetch("/api/token/", peticion_opciones)
      .then( respuesta => respuesta.json())
      .then( json_resultado => {
        console.log(json_resultado.access);
        if (json_resultado.access) {
          let formdata = new FormData();

          temporal_token = {
            'temporal_token': temporal_token,
            'token': json_resultado.access
          }
          
          formdata.append("form", JSON.stringify(temporal_token));

          var requestOptions = {
            method: 'POST',
            body: formdata,
            redirect: 'follow'
          };

          fetch("/device_login/", requestOptions)
            .then(response => response.json())
            .then(result => console.log(result))
            .catch(error => console.log('error', error));
          
        }
      })
      .catch( error => console.log("error", error));
  }

  return false;
}
