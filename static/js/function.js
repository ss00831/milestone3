$(document).ready(function () {
  $(".sidenav").sidenav();
  $(".modal").modal();
  $('select').formSelect();
});

// Add/Remove Input Fields Dynamically with jQuery :
// https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery

$(document).ready(function () {
  let max_fields = 100; //maximum input boxes allowed
  let input_ingredient = $(".input_fields_ingredient"); //Fields wrapper
  let input_instruction = $(".input_fields_instruction"); //Fields wrapper
  let input_ingredient_edit = $(".input_fields_ingredient_edit"); //Fields wrapper
  let input_instruction_edit = $(".input_fields_instruction_edit"); //Fields wrapper
  let add_ingredient_button = $(".add_ingredient_field_button"); //Add button ID
  let add_instruction_button = $(".add_instruction_field_button"); //Add button ID
  let add_ingredient_button_edit = $(".add_ingredient_field_button_edit"); //Add button ID
  let add_instruction_button_edit = $(".add_instruction_field_button_edit"); //Add button ID

  let x = 0; //initlal text box count for add page of ingredients
  let y = 0; //initlal text box count for add page of instruction
  
  let x1 = -1; //initlal text box count for edit page of ingredients 
  let y1 = -1; //initlal text box count for edit page of instruction

  // for add page of ingredients
  $(add_ingredient_button).click(function (e) {
    //on add input button click
    e.preventDefault();
    
    if (x < max_fields) {
      //max input box allowed
      x++; //text box increment
      name = "ingredient_name_" + x;
      $(input_ingredient).append(
        '<a class="remove_field_button">Remove</a><input class="ingredient validate" name=' +
          name +
          ' type="text" />'
      ); //add input box
    }
  });

  // for edit page of ingredients
  $(add_ingredient_button_edit).click(function (e) {
    //on add input button click
    e.preventDefault();
    let added_ingredients_field = document.querySelectorAll('.ingredient').length;
    x1 = added_ingredients_field;
    if (x1 < max_fields) {
      //max input box allowed
      x1++; //text box increment
      name = "ingredient_name_" + x1;
      $(input_ingredient_edit).append(
        '<a class="remove_field_button">Remove</a><input class="ingredient validate" name=' +
          name +
          ' type="text" />'
      ); //add input box
    }
  });

  // for add page of instructions
  $(add_instruction_button).click(function (e) {
    //on add input button click
    e.preventDefault();
    
    if (y < max_fields) {
      //max input box allowed
      y++; //text box increment
      name = "instructions_name_" + y;
      $(input_instruction).append(
        '<a class="remove_field_button">Remove</a><input class="instructions validate" name=' +
          name +
          ' type="text" />'
      ); //add input box
    }
  });
  
  // for edit page of instructions
  $(add_instruction_button_edit).click(function (e) {
    //on add input button click
    e.preventDefault();
    let added_instructions_field = document.querySelectorAll('.instructions').length;
    y1 = added_instructions_field;
    if (y1 < max_fields) {
      //max input box allowed
      y1++; //text box increment
      name = "instructions_name_" + y1;
      $(input_instruction_edit).append(
        '<a class="remove_field_button">Remove</a><input class="instructions validate" name=' +
          name +
          ' type="text" />'
      ); //add input box
    }
  });

  // remove button for ingredient field on add page
  $(input_ingredient).on("click", ".remove_field_button", function (e) {
    //user click on remove text
    e.preventDefault();
    $(this).next().remove();
    $(this).remove();
    x--;
  });

  // remove button for ingredient field on edit page
  $(input_ingredient_edit).on("click", ".remove_field_button", function (e) {
    //user click on remove text
    e.preventDefault();
    $(this).next().remove();
    $(this).remove();
    x1--;
  });

  // remove button for instructions field on add page
  $(input_instruction).on("click", ".remove_field_button", function (e) {
    //user click on remove text
    e.preventDefault();
    $(this).next().remove();
    $(this).remove();
    y--;
  });

  // remove button for instructions field on edit page
  $(input_instruction_edit).on("click", ".remove_field_button", function (e) {
    //user click on remove text
    e.preventDefault();
    $(this).next().remove();
    $(this).remove();
    y1--;
  });
});

function imgError(image) {
    image.onerror = "";
    image.src = "static/images/alternative_img_for_recipe.png";
    return true;
}

$(document).ready(function () {
    var input_pass = document.getElementById('delete_password').value;
    
});


