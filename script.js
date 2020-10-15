const demo = document.getElementById("demo");
const title = demo.innerHTML;
const charArray = title.split('')
let animationHTML = '';
charArray.forEach((char, index) => {
  animationHTML = animationHTML + `<div class="char" style='animation-delay: ${index*2}s'>${char}</div>`
})

demo.innerHTML = animationHTML;