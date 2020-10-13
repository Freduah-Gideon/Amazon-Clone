document.getElementById("navbar-toggle").addEventListener("click", () => {
    document.getElementById("left_nav_body_whole").style.display = 'block'
    document.getElementById("left_nav").style.left = '0px'
})

document.getElementById("close_left_nav").addEventListener("click", () => {
    document.getElementById("left_nav_body_whole").style.display = 'none'
    document.getElementById("left_nav").style.left = '-2000px'
})

document.getElementById('navbar-search-select').addEventListener("change", (event) => {
    event.target.style.width = 'min-content'
})

document.getElementById('navbar-language-event-div').addEventListener("mouseenter", () => {
    setTimeout(() => {
        document.getElementById("language-options-container").style.display = 'block'
    },200)

})

document.getElementById('navbar-language-event-div').addEventListener("mouseleave", () => {
    document.getElementById("language-options-container").style.display = 'none'
})

document.getElementById('navbar-user-display').addEventListener("mouseenter", () => {
    setTimeout(() => {
        document.getElementById("navbar-accounts-and-lists").style.display = 'block'
    },200)


})

document.getElementById('navbar-user-display').addEventListener("mouseleave", () => {
    document.getElementById("navbar-accounts-and-lists").style.display = 'none'
})

