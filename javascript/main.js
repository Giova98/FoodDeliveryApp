const swiper = new Swiper(".swiper-hero", {
   slidesPerView: "auto",
   spaceBetween: 15,
   slidesPerGroupAuto: true,

  direction: "horizontal",
  loop: true,
  allowTouchMove: true,
  effect: "fade",
  autoplay: {
    delay: 1000,
    pauseOnMouseEnter: true,
    disableOnInteraction: false,
  },

  // If we need pagination
  pagination: {
    el: ".swiper-pagination",
    type: "progressbar"
  },

  // Navigation arrows
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  scrollbar: {
    el: ".swiper-scrollbar",
    draggable: true,
  },
});

// AGUSTINA ENCARGADA DE ARMAR LOS 2 FILTERS PARA BUSCAR POR PROMOS , CUPONES Y NOVEDADES Y TMB EL ORDENAR POR

//   document.addEventListener('DOMContentLoaded', () => {
//     const buttons = document.querySelectorAll('.buttons button');
//     const select = document.getElementById('ordenar');
//     const productos = document.querySelectorAll('.producto');

//     // Filtrar por categoría
//     buttons.forEach(button => {
//         button.addEventListener('click', () => {
//             const categoria = button.id; // 'promos', 'cupones' o 'novedades'
//             filtrarProductos(categoria);
//         });
//     });

//     // Ordenar
//     select.addEventListener('change', () => {
//         const criterio = select.value;
//         ordenarProductos(criterio);
//     });

//     function filtrarProductos(categoria) {
//         productos.forEach(producto => {
//             if (categoria === 'promos' || categoria === 'cupones' || categoria === 'novedades') {
//                 producto.style.display = producto.dataset.categoria === categoria ? 'block' : 'none';
//             } else {
//                 producto.style.display = 'block'; // Mostrar todos si no hay filtro
//             }
//         });
//     }

//     function ordenarProductos(criterio) {
//         const productosArray = Array.from(productos);
//         let sortedProductos;

//         if (criterio === 'clasificacion') {
//             sortedProductos = productosArray.sort((a, b) => a.dataset.clasificacion - b.dataset.clasificacion);
//         } else if (criterio === 'tiempo_entrega') {
//             sortedProductos = productosArray.sort((a, b) => a.dataset.tiempo-entrega - b.dataset.tiempo-entrega);
//         } else if (criterio === 'envio_gratis') {
//             sortedProductos = productosArray.sort((a, b) => (a.dataset.envio-gratis === 'true' ? -1 : 1) - (b.dataset.envio-gratis === 'true' ? -1 : 1));
//         } else {
//             sortedProductos = productosArray; // Sin criterio, no se ordena
//         }

//         // Limpiar el contenedor de productos
//         const contenedor = document.getElementById('productos');
//         contenedor.innerHTML = '';
//         sortedProductos.forEach(producto => contenedor.appendChild(producto)); // Reinsertar productos en orden
//     }
// });
