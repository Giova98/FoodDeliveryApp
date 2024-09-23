/*
const swiper = new Swiper(".swiper-hero", {
    // Optional parameters
    // slidesPerView: "auto",
    // spaceBetween: 15,
    // slidesPerGroupAuto: true,

    direction: "horizontal",
    loop: true,
    // allowTouchMove: true,
    // effect: "cube",
    autoplay: {
      delay: 10000,
      pauseOnMouseEnter: true,
      disableOnInteraction: false,
    },

    // If we need pagination
    pagination: {
      el: ".swiper-pagination",
      // type: "progressbar"
      clickable: true,
      // dynamicBullets: true
    },

    // Navigation arrows
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },

    // And if we need scrollbar
    // scrollbar: {
    //   el: ".swiper-scrollbar",
    //   draggable: true,
    // },
  });
*/
document.addEventListener("DOMContentLoaded", (event) => {
  console.log("anda");
});

  const form = document.querySelector('.formulario')

  form.addEventListener('submit' , function(event){
    event.preventDefault();

    const nombre = form.querySelector('input[placeholder="Primer nombre"]').value.trim();
    const telefono = form.querySelector('input[type="tel"]').value.trim();
    const email = form.querySelector('input[type="email"]').value.trim();
    const mensaje = form.querySelector('textarea').value.trim();

    if (!nombre || !email || !mensaje){
      alert("Por favor , Completa los Campos Requeridos")
      return;
    }
    if (!email.includes('@')) {
      alert('Por favor, ingresa un correo electrónico válido.');
      return;
    }
    if (!/^[a-zA-Z\s]+$/.test(nombre)) {
      alert("El nombre no puede contener números.");
      return;
    }
    if (!/^[0-9]+$/.test(telefono)) {
      alert("Tu telefono tiene que contenter numeros");
    }
    alert('Formulario validado y listo para enviar.');
  })
  

  console.log("main.js cargado correctamente");