
const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".signs-container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

// ================signin validation




  

'use strict'
  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var signin = document.querySelectorAll('.sign-in-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(signin)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })




  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var signup = document.querySelectorAll('.sign-up-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(signup)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })

