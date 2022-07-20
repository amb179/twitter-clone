////////////////////////////
////// for file upload /////
////////////////////////////

const imgInput = document.querySelector('#img-select')
const imgPreview = document.querySelector('.preview')
const pickerBtn = document.querySelector('.upload')

imgInput.addEventListener('change', function() {  
  const file = this.files[0]  
  if(!file) return  
  const reader = new FileReader()  
  reader.addEventListener('load', function() {  
   imgPreview.src = this.result  
  })  
  reader.readAsDataURL(file)  
})  
 
//const image_select = document.querySelector("#image-select");
//image_select.addEventListener("change", function() {
  //const reader = new FileReader();
  //reader.addEventListener("load", () => {
    //const uploaded_image = reader.result;
  //});
  //reader.readAsDataURL(this.files[0]);
//});

