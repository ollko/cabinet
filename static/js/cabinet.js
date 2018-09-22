$( "select" )
  .change(function () {
    var str = "";
    $( "select option:selected" ).each(function() {
      str += $( this ).text() + " ";
    });
    $( "div.product-price" ).text( str );
  })
  .change();

//Popovers initialization
$("[data-toggle=popover]").each(function(i, obj) {

$(this).popover({
  // container: 'body',
  delay: { "show": 500, "hide": 100},
  animation:true,
  html: true,
  content: function() {
  var id = $(this).attr('id')
  return $('#popover-content-' + id).html();
  }
  });
});