 //PRODUCT DETAILS
 
 //disable +/- buttons outside 1-99 range
 function handleEnableDisable(itemId){
  let currentValue = parseInt($(`#qty_${itemId}`).val());
  let minusDisabled = currentValue <=  1;
  let plusDisabled = currentValue > 98;
  $(`#minus_item_${itemId}`).prop('disabled', minusDisabled);
  $(`#plus_item_${itemId}`).prop('disabled', plusDisabled);
}

//Ensure proper enabling/disabling of all inputs on page load
let allQtyInputs = $('.qty_input');
for(let i=0; i < allQtyInputs.length; i++){
  let itemId = $(allQtyInputs[i]).data('item_id');
  handleEnableDisable(itemId);
}
//Check enable/disable every time the input is changed
$('.qty_input').change(function(){
  let itemId = $(this).data('item_id');
  handleEnableDisable(itemId);
})

//Incement quantity
$('.increment-qty').click(function(e){
  e.preventDefault();
  let closestInput = $(this).closest('.input-group').find('.qty_input')[0];
  let currentValue = parseInt($(closestInput).val());
  $(closestInput).val(currentValue + 1);
  let itemId = $(this).data('item_id');
  handleEnableDisable(itemId);
});

//decrement quantity
$('.decrement-qty').click(function(e){
  e.preventDefault();
  let closestInput = $(this).closest('.input-group').find('.qty_input')[0];
  let currentValue = parseInt($(closestInput).val());
  $(closestInput).val(currentValue - 1);
  let itemId = $(this).data('item_id');
  handleEnableDisable(itemId);
});

//PRODUCTS

// Select button control
$("#sort-selector").change(function() {
  let selector = $(this);
  let currentUrl = new URL(window.location);

  let selectedVal = selector.val();
  if (selectedVal != "reset"){
      let sort = selectedVal.split("_")[0];
      let direction = selectedVal.split("_")[1];

      currentUrl.searchParams.set("sort", sort);
      currentUrl.searchParams.set("direction", direction);

      window.location.replace(currentUrl);
  } else {
      currentUrl.searchParams.delete("sort");
      currentUrl.searchParams.delete("direction");

      window.location.replace(currentUrl);
  }
})

