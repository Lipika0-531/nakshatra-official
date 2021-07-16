
// let active;
// active= document.querySelectorAll(".overall-review");
// var count=[ ];
// for(var i=0; i<=active.length; i++){
//   active+=i[] ;
//   count.push(active);
// }

rev_elem = document.querySelectorAll(".overall-review");
for(let i = 0; i< 3; i++){
  rev_elem[i].classList.add("active")
}

let form = document.querySelectorAll(".details-toggle");

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


comment = document.getElementById("floatingTextarea");
commentSubmit = document.getElementById("submit-btn");






commentCancel = document.getElementById("cancel-btn");
commentSubmit.addEventListener('click', function(event){
  console.log("hello");
    axios({
      method:"PUT",
      url:"http://127.0.0.1:8000/app/api/product/1",
      data: {
        "rating":"4",
        "body":"hello"
      },
      headers:{
        'Content-Type': 'application/json',
      }
  })
  .then(function(response){
    console.log(response)
  })

})
//==comment display==

let cmt_display = document.getElementsByClassName("star");

function comment_display(){
  document.getElementById("comment").style.display ="block";
}
