$(function() {
    $(".navbar-toggler").on("click", function(e) {
        $(".tm-header").toggleClass("show");
        e.stopPropagation();
      });
    
      $("html").click(function(e) {
        var header = document.getElementById("tm-header");
    
        if (!header.contains(e.target)) {
          $(".tm-header").removeClass("show");
        }
      });
    
      $("#tm-nav .nav-link").click(function(e) {
        $(".tm-header").removeClass("show");
      });
});

function myFunction() {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("myBtn");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "بیشتر..";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "کمتر..";
    moreText.style.display = "inline";
  }
};