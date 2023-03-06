// Smooth scrolling for anchor links
$('a[href^="#"]').on('click', function(event) {
  var target = $(this.getAttribute('href'));
  if( target.length ) {
    event.preventDefault();
    $('html, body').animate({
        scrollTop: target.offset().top
    }, 1000);
  }
});

// Change header background on scroll
$(window).on('scroll', function() {
  var scrollPosition = $(this).scrollTop();
  if (scrollPosition > 100) {
    $('header').addClass('scrolled');
  } else {
    $('header').removeClass('scrolled');
  }
});
