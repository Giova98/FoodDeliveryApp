document.addEventListener("DOMContentLoaded", function() {
    Toastify({
        text: "¡Bienvenido/a!",
        duration: 3000,
        destination: "https://github.com/apvarun/toastify-js",
        newWindow: true,
        close: true,
        gravity: "top", // `top` or `bottom`
        position: "center", // `left`, `center` or `right`
        stopOnFocus: true, // Prevents dismissing of toast on hover
        style: {
            background: "linear-gradient(to right, #000 , #0098d3 ,  #0098d3)",  
        },
        onClick: function(){} // Callback after click
    }).showToast();

    // Agregar eventos a los campos de entrada
    document.getElementById("nombre").addEventListener("blur", validarNombre);
    document.getElementById("email").addEventListener("blur", validarEmail);
    document.getElementById("password").addEventListener("blur", validarContraseña);
    document.getElementById("confirm_password").addEventListener("blur", validarConfirmarContraseña);
});

function validarNombre() {
    const nombre = document.getElementById("nombre").value;
    const nombreRegex = /^[A-Za-záéíóúÁÉÍÓÚÑñ ]+$/;

    if (nombre === "") {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Por favor, completa el campo de nombre.",
            footer: '<a href="#">¿Por qué tengo este problema?</a>'
        });
    } else if (!nombreRegex.test(nombre)) {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Por favor, ingrese un carácter válido para el nombre (solo letras).",
            footer: '<a href="#">¿Por qué tengo este problema?</a>'
        });
    }
}
function validarEmail() {
    const email = document.getElementById("email").value;
    if (email === "") {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Por favor, completa el campo de email.",
            footer: '<a href="#">¿Por qué tengo este problema?</a>'
        });
    }
    // Aquí podrías agregar más validaciones para el formato del email
}

function validarContraseña() {
    const password = document.getElementById("password").value;
    if (password.length < 6) {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "La contraseña debe tener al menos 6 caracteres.",
            footer: '<a href="#">¿Por qué tengo este problema?</a>'
        });
    }
}

function validarConfirmarContraseña() {
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm_password").value;

    if (confirmPassword === "") {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Por favor, completa el campo de confirmar contraseña.",
            footer: '<a href="#">¿Por qué tengo este problema?</a>'
        });
    } else if (password !== confirmPassword) {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Las contraseñas no coinciden. Por favor, verifica.",
            footer: '<a href="#">¿Por qué tengo este problema?</a>'
        });
    }
}

function validarFormulario() {
    // Obtener valores de los campos
    const nombre = document.getElementById("nombre").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm_password").value;

    // Validación de campos vacíos
    if (nombre === "" || email === "" || password === "" || confirmPassword === "") {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Por favor, completa todos los campos.",
            footer: '<a href="#">¿Por qué tengo este problema?</a>'
        });
        return false;
    }

    // Validación de coincidencia de contraseñas
    if (password !== confirmPassword) {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Las contraseñas no coinciden. Por favor, verifica.",
            footer: '<a href="#">¿Por qué tengo este problema?</a>'
        });
        return false;
    }

    // Validación de longitud de contraseña
    if (password.length < 6) {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "La contraseña debe tener al menos 6 caracteres.",
            footer: '<a href="#">¿Por qué tengo este problema?</a>'
        });
        return false;
    }

    return true; // Permitir el envío del formulario
}