
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

// =======================================INDEX PAGE================================================================
function indexPage(){
  AOS.init();

  // ============owl carousel=============
    $(".carousel").owlCarousel({
      margin: 10,
      loop:true,
      center: true,
      nav: true,
      responsive: {
          0:{
              items: 1,
              nav:false
          },
          600:{
              items: 2,
              nav:false
          },
          1000:{
              items: 3,
              nav:false
          }

      }
    });

  const changable = document.querySelectorAll('.button');
  const iconnames = document.querySelectorAll('.button .icon-name');

  function change(){
    const aboutPage = document.getElementById('aboutpage');
      changable.forEach(btn => {
        if(window.scrollY > window.innerHeight / 2 + 100){
          btn.classList.add('iconchange','hovericonchange');  
          aboutPage.setAttribute('style',"overflow-x:unset;");
        } else {
          btn.classList.remove('iconchange','hovericonchange');
          aboutPage.setAttribute('style',"overflow-x:hidden;");
        }
      })
  }
  window.addEventListener('scroll', change);

  function namechange(){
    iconnames.forEach(i => {
      if(window.scrollY > window.innerHeight / 2 + 100){
        i.classList.add('hovernamechange');
      } else {
        i.classList.remove('hovernamechange');
        
      }
    })
  }
  window.addEventListener('scroll', namechange);

}

// ==========================================work page===================================================
function workPage(){
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
    console.log(id);
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
    document.getElementById("comment").style.display ="block";
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



let hearts = document.querySelectorAll(".heart-icon");
hearts.forEach(function(heart){
  heart.addEventListener('click', function(event){
    this.classList.add("animate-like");
  })
})

}

// ==========================================profile page===================================================

function profilePage(){
  
  // ================profilepic=========================

  const propic = document.querySelector('.propichere');
  const picfile = document.querySelector('#propicinput');
  const uploadfile = document.querySelector('#propicupload');

  picfile.addEventListener('change', function() {
    const newfile = this.files[0];

    if(newfile){
      const reader = new FileReader();

      reader.addEventListener('load', function(){
        propic.setAttribute('src',reader.result);
      });
      
      reader.readAsDataURL(newfile);
    }
  });


}

 // ====================editbutton
 var userNameEdit = document.getElementById('validationCustom01');
 var emailEdit = document.getElementById('exampleFormControlInput1');
  function editButton1(){
    if(userNameEdit.disabled == true){
      userNameEdit.disabled = false;
    } else if(userNameEdit.disabled == false){
      userNameEdit.disabled = true;
    }
  }

  function editButton2(){
    if(emailEdit.disabled == true){
      emailEdit.disabled = false;
    } else if(emailEdit.disabled == false){
      emailEdit.disabled = true;
    }
  }
// ================================profile-validation 


  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })


  // ============================================page load==============================================
  window.addEventListener("load", function () {
    if (this.document.title === "NAKSHATHRA PHOTOGRAPHY") {
      indexPage();
    } else if(this.document.title === "Your Profile"){
      profilePage();
    } else if(this.document.title === "Our Works" || this.document.title === "Collections"){
      workPage();
    }
  });