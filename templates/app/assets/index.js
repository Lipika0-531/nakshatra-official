let form = document.querySelectorAll(".details-toggle");

const getProduct = async (id) => {
  try {
    const response = await axios.get(
      `http://localhost:8000/app/api/product/${id}`
    );
    return response;
  } catch (error) {
    console.error(error);
  }
};
const showProduct = async (id) => {
  const details = await getProduct(id);

  if (details.data) {
    return details.data[0];
  }
};
form.forEach(function (btn) {
  btn.addEventListener("click", async function (event) {
    const data =  await showProduct(btn.getAttribute("data-api-value"));

    const title = document.getElementById('product-title');
    const price = document.getElementById('product-price');
    const author = document.getElementById('product-author');
    const published = document.getElementById('product-published');
    const rating_count = document.getElementById('product-rating-count');


    title.innerText = data.title
    price.innerText = data.price
    author.innerText = data.author
    published.innerText = data.publised_on
    rating_count.innerText = data.rating_count


  });
});
