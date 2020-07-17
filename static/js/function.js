$(document).ready(function () {
  $(".sidenav").sidenav();
  $(".slider").slider({ fullwidth: true });
  $(".carousel").carousel();
  $(".collapsible").collapsible();
  $(".modal").modal();
  $(".scrollspy").scrollSpy();
  $("select").formSelect();
});

// Add/Remove Input Fields Dynamically with jQuery : 
// https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery

$(document).ready(function () {
  var max_fields = 100; //maximum input boxes allowed
  var wrapper = $(".input_fields_wrap"); //Fields wrapper
  var add_button = $(".add_field_button"); //Add button ID

  var x = 1; //initlal text box count
  $(add_button).click(function (e) {
    //on add input button click
    e.preventDefault();
    if (x < max_fields) {
      //max input box allowed
      x++; //text box increment
      $(wrapper).append(
        '<input type="text" name="ingredients"/><a href="#" class="remove_field">Remove</a>'
      ); //add input box
    }
  });

  $(wrapper).on("click", ".remove_field", function (e) {
    //user click on remove text
    e.preventDefault();
    $(this).parent("div").remove();
    x--;
  });
});


//$('#message-cancel').val('');
//$('#message-cancel').next().removeClass('active');


var x = document.getElementsByClassName("ingredient");
x.length;