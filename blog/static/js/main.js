$(document).ready(function(){
    $('.togg').click(function(){
$('.togg').toggleClass('lijo');
$('.firstlevel').toggleClass('surya');

});


$('.firstlevel li.has-sub').click(function(){
$(this).find('.sub').slideToggle();   
var t = $(this).find('.sub'); 
$('.sub').not(t).slideUp();
});
});