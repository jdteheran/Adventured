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
        if (json_resultado.access) {
          console.log('consuminos endpoitn');
        }
      })
      .catch( error => console.log("error", error));
  }

  return true;
}
