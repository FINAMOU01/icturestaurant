/* =========== Show Navbar =========== */
const navbar = document.querySelector(".navbar");
const hamburger = document.querySelector(".hamburger");

hamburger.addEventListener("click", () => {
  navbar.classList.toggle("show");
});

/* =========== Scroll Position =========== */

const header = document.querySelector(".header");
const scrollLink = document.querySelectorAll(".navbar a:not(:last-child)");

/* =========== Smooth Scroll =========== */
Array.from(scrollLink).map((link) => {
  link.addEventListener("click", (e) => {
    // Prevent Default
    e.preventDefault();

    const id = e.currentTarget.getAttribute("href").slice(1);
    const element = document.getElementById(id);
    let position = element.offsetTop - 90;

    window.scrollTo({
      left: 0,
      top: position,
      behavior: "smooth",
    });
    navbar.classList.remove("show");
  });
});

/* =========== Preloader =========== */
const preloader = document.querySelector(".preloader");

window.addEventListener("load", () => {
  setTimeout(() => {
    preloader.style.display = "none";
  }, 2000);
});

/* =========== Scroll Top =========== */
const scrollTop = document.querySelector(".scroll-top");

scrollTop.addEventListener("click", () => {
  window.scrollTo({
    left: 0,
    top: 0,
    behavior: "smooth",
  });
});

window.addEventListener("scroll", (e) => {
  const scrollHeight = window.pageYOffset;

  if (scrollHeight > 300) {
    scrollTop.classList.add("show");
  } else {
    scrollTop.classList.remove("show");
  }
});


// ... your existing JavaScript code ...

const products = [
  { name: 'Fried Rice & Chicken', price: 2000, image: 'friedrice.png' },
  { name: 'Ndole & Plantain', price: 1500, image: 'ndole.png' },
  { name: 'Garri & Eru', price: 1500, image: 'garri.png' },
  { name: 'Achu', price: 2000, image: 'achu.png' },
  { name: 'Poulet DG', price: 2000, image: 'poulet.png' },
  { name: 'Reaktor', price: 500, image: 'reaktor.png' },
  { name: 'Top', price: 500, image: 'top.png' },
  
  // Add more products
];

const productList = document.querySelector('.product-list');
const orderForm = document.getElementById('orderForm');
const orderMessage = document.getElementById('orderMessage');

function createProductElement(product) {
  const productElement = document.createElement('div');
  productElement.classList.add('product');
  productElement.innerHTML = `
    <img src="items/${product.image}" alt="${product.name}">
    <h3>${product.name}</h3>
    <p>Price: XAF${product.price}</p>
    <button class="order-btn">Order Now</button>
  `;
  return productElement;
}

products.forEach(product => {
  const productElement = createProductElement(product);
  productList.appendChild(productElement);
});

const orderBtns = document.querySelectorAll('.order-btn');
orderBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    orderForm.style.display = 'block';
  });
});

orderForm.addEventListener('submit', (event) => {
  event.preventDefault();
  // Handle form submission and send data to server
  // ...
  orderForm.style.display = 'none';
  orderMessage.textContent = 'Order submitted successfully!';
});


