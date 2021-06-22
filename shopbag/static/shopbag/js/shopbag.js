//Shopbag update/remove
//update quantity on click
$('.update-pr-link').click(function(e){
    let form = $(this).prev('.update-form')
    form.submit();
  });

  //remove quantity on click
  $('.remove-item').click(function(e){
    let csrfToken = '{{csrf_token}}'
    let itemId = $(this).attr('id').split('remove_')[1];
    let size = $(this).data('poduct_size');
    let url = `/shopbag/delete/${itemId}/`
    let data= {'csrfmiddlewaretoken': csrfToken, 'product_size': size};
  
    $.post(url, data)
    .done(function(){
        location.reload();
    })
  });