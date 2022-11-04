const div = document.querySelector("div.grid-wrapper");

const imgs = div.querySelectorAll("img");

imgs.forEach((img) => {
    img.addEventListener("click", function(){
        const blurr = document.body.style.filter;
        // document.body.style.filter = blurr === 'blur(0px)' ? 'blur(8px)' : 'blur(0px)';
        img.classList.toggle("enlarged");
    })
})