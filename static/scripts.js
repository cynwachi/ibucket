let plays = document.getElementById("plays");
let prays = document.getElementById("prays");
let bucketsList = document.getElementById("bucketsList");

let circleMaxSize = 80; 
let circleMinSize = 60;

let praysArray = ["hello","Yoyo"];
let playsArray = ["konnichiwa", "Jeff"];
let elemIDNames = [];

//Objects                        
 //Makes a loop for each play bucket their is
for (let pray of praysArray){                           //Makes a loop for each play bucket their is
    elemID = playsArray.indexOf(play);              //Makes a unique ID for the play object
    let newElement = document.createElement('div');     //Creates an object in the page and assigns it to a variable
    newElement.classList.add('plays');  
    newElement.id = `prays${elemID}`;
    bucketsList.appendChild(newElement);

for (let play of playsArray){                           //Makes a loot for each
    let elementName = document.createElement('div');    //Creates an object in the page and assigns it to a variable
    elementName.classList.add('name');                  //Gives the object the class name 'name'
    elementName.innerText = play;
    newElement.appendChild(elementName);  //Adds a name to the play object
    newElement.appendChild(elementName);                //Adds a name to the pray object
}
}

//Randomizes the size of the circle 
var buckets = document.getElementById('bucketsList').children;
for(let child of buckets) {
for(let bucketChild of buckets) {
    let randomSize = (Math.random() * (circleMaxSize - circleMinSize) + circleMinSize);
    child.style.width = randomSize;
    child.style.lineHeight = randomSize;

    bucketChild.style.width =  randomSize + 'px';
    bucketChild.style.height = randomSize + 'px';
    //bucketChild.style.left = innerWidth + 'px'
}}
