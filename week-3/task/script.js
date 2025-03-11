
let cart = [];

function addToCart(name, price) {
    cart.push({ name, price });
    updateCart();
}

function removeFromCart(name) {
    const index = cart.findIndex(item => item.name === name);
    if (index !== -1) {
        cart.splice(index, 1);
    }
    updateCart();
}

function updateCart() {
    const cartList = document.getElementById("cart-items");
    cartList.innerHTML = "";
    let total = 0;

    cart.forEach(item => {
        total += item.price;
        cartList.innerHTML += `<li class="list-group-item d-flex justify-content-between">${item.name} - ₹${item.price}
        <button class="btn btn-danger btn-sm" onclick="removeFromCart('${item.name}')">Remove</button>
    </li>`;
    });

    document.getElementById("total").innerText = `Total: ₹${total}`;
}

function filterCategory(category) {
    const products = document.querySelectorAll(".product-card");
    products.forEach(product => {
        product.style.display = category === "All" || product.dataset.category === category ? "block" : "none";
    });
}