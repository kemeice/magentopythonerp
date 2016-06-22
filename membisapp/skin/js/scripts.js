document.getElementById("id_type_product").addEventListener("Change",Producttype)
document.getElementById("id_groups").addEventListener("Change",groups)

Function Producttype()
var config= $( "#id_type_product option:selected" ).text();
if config==configurable
{$( "#target" ).show();

}

Function groups()
 var cel= $( "#id_groups:selected" ).text();
$( #cel ).show();
$('#top').hide();
$( "#content" ).show();


 $(window).bind("load", function() {
 $('#dvLoading').fadeOut(2000);
});









