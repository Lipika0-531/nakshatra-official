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

//------------------------------------------detail toggler--------------------------------------------------------------

//add comment------------------------------//
const commentSection = document.getElementById("comments");
const toggleDetails = document.querySelectorAll(".details-toggle");
var id;

function addComment(data) {
  var row = document.createElement("div");
  row.classList.add("row", "prev-comments", "mt-4");
  var profile_col = document.createElement("div");
  profile_col.classList.add("col-2", "user-profile");
  var review_col = document.createElement("div");
  review_col.classList.add("name-content", "col-10");

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

const getProductDetails = async (id) => {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/app/api/product/${id}`
    );
    if (response.data) return response.data[0];
    throw "No data";
  } catch (error) {
    console.log(error);
  }
};

toggleDetails.forEach(function (btn) {
  btn.addEventListener("click", async function () {
    commentSection.innerHTML="";
    id = btn.getAttribute("data-api-value");
    const productData = await getProductDetails(id);
    dataset = ["title","price", "author", "published_on", "rating_count", "description"];
    dataset.forEach((data) => {
      document.getElementById(`product-${data}`.replace("_", "-")).innerText =
        (data==='published_on')?new Date(productData[data]).toDateString():
        productData[data];
    });
    if(productData['reviews'])
      productData["reviews"].forEach((review) => {
        commentSection.appendChild(addComment(review));
      });
    if(productData['avg_ratings']){
      let star = document.querySelectorAll(".overall-review")
      star.forEach( elem => elem.classList.remove('active'));
      for(let i=0; i<productData['avg_ratings']; i++){
          star[i].classList.add('active');
      }
    }
      
  });
});

//submit comment---------------------------------------------------------------

const commentSubmit = document.getElementById("submit-btn");
var userRating='0';
document.querySelectorAll('.star').forEach( 
  star => star.addEventListener('click', function() {
    userRating = this.value;
  })
);
commentSubmit.addEventListener("click", async function (event) {
  body = $("#floatingTextarea");
  try{
    await axios({
      method: "POST",
      url: `http://127.0.0.1:8000/app/api/product/${id}`,
      data: {
        user: 1,
        product: id,
        rating: userRating,
        body: body.val(),
      },
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
    }).then(function (response) {
      if(response.data.message === "success"){
        let data = response.data;
        commentSection.appendChild(addComment({username:data.username, body:data.body}));
      }
    });
  }catch(error){
    console.log(error);
  }

  body.val("");
});

$('#cancel-btn').click(function(){
  $("#floatingTextarea").val("");
})
//==comment display==

let cmt_display = document.getElementsByClassName("star");

function comment_display(){
  document.getElementById("comment").style.display ="block";
}
