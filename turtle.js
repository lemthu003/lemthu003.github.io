document.addEventListener("scroll", function() {
    let scrollY = window.scrollY; 
    let turtle = document.getElementById("turtle");

    let alpha = 0.05;
    let moveRight = scrollY * alpha; 
    let rotateAngle = Math.sin(scrollY * alpha) * 7.5; 

    turtle.style.transform = `translateX(${moveRight}px) rotate(${rotateAngle}deg)`;
});
