document.querySelector(".year").innerHTML = new Date().getFullYear();
var notifiBox = document.querySelector(".notifi-box");
var notifiModal = document.querySelector(".notifi-modal");
var notifiModalPopped = false;
notifiBox.onclick = () => {
    if(!notifiModalPopped) {
        notifiModal.style.display = "block";
        notifiModalPopped = true;
    }
    else {
        notifiModal.style.display = "none";
        notifiModalPopped = false;
    }
}

var acc = document.getElementsByClassName("accordion");
var i;
for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    } 
  });
}

const notifPopup = (e) => {
    if(!(e.target == notifiBox)) {
        if(notifiModalPopped) {
            notifiModal.style.display = "none";
            notifiModalPopped = false;
        }
    }
}
document.body.addEventListener('click', notifPopup, true);
var loginModal = document.getElementById('login-modal-id');
    window.onclick = function(event) {
    if (event.target == loginModal) {
        loginModal.style.display = "none";
    }
}
