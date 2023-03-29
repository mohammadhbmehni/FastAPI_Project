$(document).ready(function() {
    // Configure/customize these variables.
    var showChar = 250;  // How many characters are shown by default
    var ellipsestext = "...";
    var moretext = "ادامه‌ی مطلب..";
    var lesstext = "کمتر نمایش بده..";


    $('.more').each(function() {
        var content = $(this).html();

        if(content.length > showChar) {

            var c = content.substr(0, showChar);
            var h = content.substr(showChar, content.length - showChar);

            var html = c + '<span class="moreellipses">' + ellipsestext+ '&nbsp;</span><span class="morecontent"><span>' + h + '</span>&nbsp;&nbsp;<a href="" class="morelink">' + moretext + '</a></span>';

            $(this).html(html);
        }

    });

    $(".morelink").click(function(){
        if($(this).hasClass("less")) {
            $(this).removeClass("less");
            $(this).html(moretext);
        } else {
            $(this).addClass("less");
            $(this).html(lesstext);
        }
        $(this).parent().prev().toggle();
        $(this).prev().toggle();
        return false;
    });
});


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

// $(function (){
//     $('#myForm').submit(function (evet){
//         // event.preventDefault();
//         const email = $('#email-input').val();
//         const loginForm = `
//         <form>
//             <label for="email">ایمیل</label><br>
//             <input type="email" id="login-email" name="email" value="${email}" readonly><br>
//             <label for="password">رمز عبور</label><br>
//             <input type="password" id="login-password" name="password" required>
//             <button type="submit">ورود</button>
//         </form>
//         `;
//         $('#myform').replaceWith(loginForm);
//     });
// });
