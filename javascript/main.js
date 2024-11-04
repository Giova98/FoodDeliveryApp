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

