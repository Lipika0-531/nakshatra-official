let form = document.querySelectorAll(".details-toggle");
console.log("hello");

const getProduct = async (id) => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/app/api/product/${id}`);
    return response;
  } catch (error) {
    console.error(error);
  }
};
const showProduct = async (id) => {
    const details = await getProduct(id);

    if(details.data.detail){
        console.log(details.data.detail,id)
    }
};
form.forEach(function(btn){
    btn.addEventListener('click', function(event){
        showProduct(btn.getAttribute('data-api-value'))
    })
 })
