// // document.getElementById("lion").style.color = "red";
// // document.getElementById("tiger").style.color = "green";
// // document.getElementById("bear").style.color = "blue";

// // document.getElementsByTagName("li")[0].style.color = "red";

// // document.getElementsByClassName("animal")[1].style.color = "red";

// // document.querySelectorAll(".animal")[0].style.color="red";

// document.querySelectorAll(".animal")[2].innerHTML = "dog"; 
// const animals = document.getElementById("animals");

// animals.innerHTML += "<li class = 'animal'>Cat</li>";

// document.querySelectorAll(".box")[0].classList.add("purple");
// document.querySelectorAll(".box")[0].classList.remove("purple");
// document.querySelectorAll(".box")[0].classList.toggle("yellow");

// document.getElementById("btn").addEventListener("click", function(){
//     console.log("click!!!!!")
// });

// var num = 0;
// document.getElementById("plus").addEventListener("click",
// num++;
// document.getElementById("num").innerHTML = num;
// });

// document.getElementById("minus").addEventListener("click",
// num--;
// document.getElementById("num").innerHTML = num;
// });

// document.querySelector(".bar").addEventListener("click",function(){
//     document.querySelector
//     (".newBar").style.display = "block";
// });


//  document.querySelector(".bar").addEventListener("click",function(){
//      document.querySelector(".bar").innerHTML = "Clicked!!!";
//      document.querySelector
//      (".newBar").classList.toggle("show");
//  });

document.querySelectorAll('.tab-button')[0].addEventListener("click",function(){
    for(let i = 0; i < document.querySelectorAll(".tab-button")[i].classList.remove("here");i++){
        document.querySelectorAll(".tab-button")[i].classList.remove("here");
        document.querySelectorAll(".tab-content")[i].classList.remove("show");
    }
    document.querySelectorAll(".tab-button")[0].classList.add("here");
        document.querySelectorAll(".tab-content")[0].classList.add("show");
});

document
    .querySelectorAll('.list')[0]
    .addEventListener("click",function(e){});

    function tabBtn(a){
        document
        .querySelectorAll('.tab-button')[0]
        .addEventListener("click",function(){
            for(let i = 0; i < document.querySelectorAll(".tab-button")[i].classList.remove("here");i++){
                document.querySelectorAll(".tab-button")[i].classList.remove("here");
                document.querySelectorAll(".tab-content")[i].classList.remove("show");
            }
            document.querySelectorAll(".tab-button")[a].classList.add("here");
                document.querySelectorAll(".tab-content")[a].classList.add("show");
        });
    }