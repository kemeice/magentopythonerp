//document.getElementById("id_type_product").addEventListener("Change",Producttype)
//document.getElementById("id_groups").addEventListener("Change",groups)

function Producttype()
{
var config= $( "#id_type_product option:selected" ).text();
if (config=='configurable')
{$( "#configarable" ).show();

}
}
function groups()
{
 //var cel= $( "#id_groups:selected" ).text();
 //if (cel=='Default')
//{$( "#Default" ).show();
//}
 //if (cel=='Beds')
//{$( "#Beds" ).show();
//}
$('#top').hide();
$( "#content" ).show();
}

 jQuery(window).bind("load", function() {
 jQuery('#dvLoading').fadeOut(2000);
});

