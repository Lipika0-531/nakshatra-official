let form = document.querySelectorAll(".details-toggle");

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();

      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
commentSection = document.getElementById("comments");

function addComment(data) {
  var row = document.createElement("div");
  row.classList.add("row", "prev-comments", "mt-4");
  var profile_col = document.createElement("div");
  profile_col.classList.add("col-md-2", "user-profile");
  var review_col = document.createElement("div");
  review_col.classList.add("name-content", "col-md-10");

  var user_name = document.createElement("h6");
  user_name.classList.add("user-name");
  user_name.appendChild(document.createTextNode(data.username));

  var review_content = document.createElement("p");
  review_content.classList.add("review-content");
  review_content.appendChild(document.createTextNode(data.body));

  review_col.appendChild(user_name);
  review_col.appendChild(review_content);

  row.appendChild(profile_col);
  row.appendChild(review_col);

  return row;
}

const getProduct = async (id) => {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/app/api/product/${id}`
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
    const data = await showProduct(btn.getAttribute("data-api-value"));

    const title = document.getElementById("product-title");
    const price = document.getElementById("product-price");
    const author = document.getElementById("product-author");
    const published = document.getElementById("product-published");
    const rating_count = document.getElementById("product-rating-count");
    const product_description = document.getElementById("product-description");

    title.innerText = data.title;
    price.innerText = data.price;
    author.innerText = data.author;
    published.innerText = data.publised_on;
    rating_count.innerText = data.rating_count;
    product_description.innerText = data.description

    commentSection.innerHTML = "";
    for (let i = 0; i < data.reviews.length; i++) {
      commentSection.appendChild(addComment(data.reviews[i]));
    }
  });
});
var rating

document.querySelectorAll(".star").forEach((element)=>{
  element.addEventListener('click',function(){
    rating=this.value
  })
})
comment = document.getElementById("floatingTextarea");
commentSubmit = document.getElementById("submit-btn");

commentCancel = document.getElementById("cancel-btn");
commentSubmit.addEventListener("click", function (event) {
  body = $("#floatingTextarea").val();
  axios({
    method: "POST",
    url: `http://127.0.0.1:8000/app/api/product/${id}`,
    data: {
      user: 1,
      product: id,
      rating,
      body,
    },
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
  }).then(function (response) {
    console.log(response);
  });
});

