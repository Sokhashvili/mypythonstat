let apiUrlProducts = "https://fakestoreapi.com/products";
let apiUrlCategories = "https://fakestoreapi.com/products/categories";

let productsPromise = fetch(apiUrlProducts)
  .then(response => response.json());

let categoriesPromise = fetch(apiUrlCategories)
  .then(response => response.json());

  Promise.all([productsPromise, categoriesPromise]).then(values => {
    let products = values[0];
    let categories = values[1];
  
    categories.forEach(category => {
      let categoryProducts = products.filter(product => product.category === category);
  
      let categoryArea = document.createElement('section');
      categoryArea.classList.add('category');
      categoryArea.innerHTML = `
        <h2>${category}</h2>
        <div class="cards-area"></div>`;
  
      let cardsArea = categoryArea.querySelector('.cards-area');
  
      categoryProducts.forEach(product => {
        cardsArea.innerHTML += `
          <div class="card" style="width: 18rem;">
            <img src="${product.image}" class="card-img-top" alt="${product.title}">
            <div class="card-body">
              <h5 class="card-title">${product.title}</h5>
              <p class="card-text">$${product.price}</p>
              <a href="${product.url}" class="btn btn-primary">View Product</a>
            </div>
          </div>`;
      });
  
      document.body.appendChild(categoryArea);
    });
  });