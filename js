<script>
    console.log('working');
  if (localStorage.getItem('cart') == null) {
    var cart = {};
  }
  else {
    cart = JSON.parse(localStorage.getItem('cart'));
    document.getElementById("cart").innerHTML = Object.keys(cart).length;
  }
  $('.cart').click(function () {
    console.log('clicked');
    var idstr = this.id.toString();
    console.log(idstr);
    if (cart[idstr] != undefined) {
      cart[idstr] = cart[idstr] + 1;
    }
    else {
      cart[idstr] = 1;
    }
    console.log(cart);
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById("cart").innerHTML = Object.keys(cart).length;

  });

  

    updatePopover(cart);
function updatePopover(cart)
{
    console.log('We are inside updatePopover');
    var popStr = "";
    popStr = popStr + "<h5> Cart for your items in my shopping cart </h5><div class='mx-2 my-2'>";
    var i = 1;
    for (var item in cart){
        popStr = popStr + "<b>" + i + "</b>. ";
        popStr = popStr + document.getElementById('name' + item).innerHTML.slice(0, 19) + "... Qty: " + cart[item] + '<br>';
        i = i+1;
    }
    popStr = popStr + "</div>" 
    console.log(popStr);
    document.getElementById('popcart').setAttribute('data-bs-content', popStr);
    var exampleEl = document.getElementById('popcart');
    var popover = new bootstrap.Popover(exampleEl);
}


  </script>