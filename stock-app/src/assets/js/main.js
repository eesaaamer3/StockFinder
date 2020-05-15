function myTest() {
    var btnContainer = document.getElementById("nav-list")

    var btns = document.getElementsByClassName("btn")

    for (var i = 0; i < btns.length; i++) {
        console.log(i)
        btns[i].addEventListener("click", function() {
        var current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
        });
    }
}

