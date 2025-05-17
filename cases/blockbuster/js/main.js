document.addEventListener( 'DOMContentLoaded', function () {
  new Splide( '#banner-carousel', {
    type       : 'loop',         // Loop infinito
    perPage    : 1,              // Quantos slides visíveis (ajuste conforme necessidade)
    focus      : 'center',       // Centraliza o slide ativo
    gap        : '1rem',         // Espaço entre slides
    autoplay   : true,           // Passa automaticamente
    interval   : 3000,           // 3 s entre transições
    pauseOnHover: true,
    arrows     : true,           // Exibe setas
    pagination : true,           // Exibe bolinhas
    breakpoints: {               // Responsividade
      768: { perPage: 1 },
      1024: { perPage: 2 }
    },
  } ).mount();
} );
