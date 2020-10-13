function showFullProduct(event){
    url = `${String(event.target.getAttribute('data-id') +`/?product_name=${event.target.getAttribute('data-name')}`)}`
    window.location = url 
    // + '/' +}
    // console.log(event.target)
}