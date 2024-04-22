var headerBtn = document.getElementById("headerBtn");
var tempBox = document.getElementById("tempBox");
var flag = false;

headerBtn.addEventListener("click", () => {
  if (flag === false) {
    console.log("It is working");
    tempBox.innerHTML = `<div class='w-32 h-32 bg-zinc-800 z-10 right-0 top-0 absolute box'></div>`;
    flag = true;
  }
});
