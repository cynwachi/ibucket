let prays = document.getElementById("prays");
let plays = document.getElementById("plays");
let bucketsList = document.getElementById("bucketsList");
let addBucket =  document.getElementById("add_bucket")

let circleMaxSize = 80; 
let circleMinSize = 20;

let praysArray = ["hello","Yoyo"];
let playsArray = ["konnichiwa", "ja"];
let elemIDNames = [];


//Creates an object for each pray inside of the buckets div
for (let pray of praysArray){
    elemID = praysArray.indexOf(pray);
    let newElement = document.createElement('div');
    newElement.classList.add('prays');
    newElement.id = `prays${elemID}`;
    bucketsList.appendChild(newElement);

    let elementName = document.createElement('div');
    elementName.classList.add('name');
    elementName.innerText = pray;
    newElement.appendChild(elementName);
}

//Creates an object for each play inside of the buckets div
for (let play of playsArray){                           //Makes a loop for each play bucket their is
    let elemID = playsArray.indexOf(play);              //Makes a unique ID for the play object
    let newElement = document.createElement('div');     //Creates an object in the page and assigns it to a variable
    newElement.classList.add('plays');                  //Gives the object the class name plays
    newElement.id = `plays${elemID}`;                   //Gives the object a unique ID
    bucketsList.appendChild(newElement);                //Adds the plays object to the bucket list
    elemIDNames.push(newElement.id);

    let elementName = document.createElement('div');    //Creates an object in the page and assigns it to a variable
    elementName.classList.add('name');                  //Gives the object the class name 'name'
    elementName.innerText = play;
    newElement.appendChild(elementName);                //Adds a name to the play object
}

//Randomizes the size of the circle 
var buckets = document.getElementById('bucketsList').children;
for(let bucketChild of buckets) {
    let randomSize = ((Math.random() * (circleMaxSize - circleMinSize) + circleMinSize));
    bucketChild.style.width = randomSize + 'px';
    bucketChild.style.height =  randomSize + 'px';
    //bucketChild.style.left = innerWidth + 'px'
}

// Randomizes the location of the circle
for(let bucketChild of buckets) {
    let validLocation = false;
    let randomX;
    let randomY; 
    
    while(validLocation === false){
        randomX = ((Math.random() * (xMax - xMin) + xMin));
        randomY = ((Math.random() * (yMax - yMin) + yMin));

        for(let x in bucketCoordsX){
            if ((bucketCoordsX[x] + 100) < randomX && (bucketCoordsX - 100) >  randomX){
                validLocation = true;
            }else{
                validLocation = false;
            }
        }
        for(let y in bucketCoordsY){
            if (randomY > (bucketCoordsY[y] + 100) || randomY < (bucketCoordsY[y] - 100)){
                validLocation = true;
            }else{
                validLocation = false;
            }
        }
        
    }
    
    bucketCoordsX.push(randomX);
    bucketCoordsY.push(randomY);
    bucketChild.style.position = "relative";
    bucketChild.style.left = randomX + 'px';
    bucketChild.style.top = randomY + 'px'

    if(bucketCoordsX.length == 2){

    }
    
    if(bucketCoordsY.length == 2){

    }

}
