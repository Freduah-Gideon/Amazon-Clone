const addToCart = () => {
    const form_object = document.getElementById('add-to-cart-form')
    const form = new FormData(form_object);
    const xhttp = new XMLHttpRequest();
    xhttp.onload = () => {
        console.log(xhttp.responseText)
        // const parsed = JSON.parse(xhttp.responseText)
        // var response;
        // response = parsed['200'] ? document.querySelector('.fake-text').classList.remove('hide') : alert(response['error'])
    }
    xhttp.onerror = ()=>{
        alert(xhttp.status)
    }
    xhttp.open('POST', event.target.getAttribute('data-location'), true)
    xhttp.send(form)
}
