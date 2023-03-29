$(document).ready(function(){
    var clicks = 0
    $("h2").click(function(){
      $(this).hide();
    });
    $("a.nav-link").hover(function(){
      $("h2").show();
    });
    $("button").click(function(){
        $.ajax({url: "demo_test.txt", success: function(result){
          $("#div1").html(result);
        }});
      });
  });