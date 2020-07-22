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
      name = "ingredient_name_" + x;
      $(wrapper).append(
        '<div><a class="remove_field_button"><i class="material-icons prefix">remove_circle_outline</i></a><input class="ingredient validate" name=' +
          name +
          ' type="text" /></div>'
      ); //add input box
    }
  });

  $(wrapper).on("click", ".remove_field_button", function (e) {
    //user click on remove text
    e.preventDefault();
    $(this).parent("div").remove();
    x--;
  });
});

/*
for (i = 0; i < x; i++) {
      name = "ingredient_name_" + x;
      $(wrapper).append(
        '<div><input class="ingredient validate" name=' +
          name +
          ' type="text" /><a href="#" class="remove_field">Remove</a></div>'
      ); //add input box
    }*/


function cal_length() 
    { var length = document.querySelectorAll('.ingredient').length;
    return length; } 

function get_password() 
    { var input_pass = document.getElementById('delete_password').value;
    return input_pass; } 

var length1 = document.querySelectorAll('.ingredient').length;
var input_pass1 = document.getElementById('delete_password').value;