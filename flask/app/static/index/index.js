$('.search-input').focus(function(){
  $(this).parent().addClass('focus');
}).blur(function(){
  $(this).parent().removeClass('focus');
})