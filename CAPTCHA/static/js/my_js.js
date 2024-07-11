document.getElementById("hintButton").addEventListener('click', function() {
  var imageUrl = this.getAttribute('data-img-url'); // Get the image URL from the data attribute
  var hintImageContainer = document.getElementById('hintImageContainer');
  hintImageContainer.style.display = 'block';
  hintImageContainer.innerHTML = `<img style="width:150px;height:150px;" src="${imageUrl}" alt="Hint Image">`;
  this.disabled = true;

  setTimeout(function() {
      hintImageContainer.innerHTML = '';
      hintImageContainer.style.display = 'none';
      document.getElementById('hintButton').style.textDecoration = 'line-through';
      document.getElementById('hintButton').style.backgroundColor='#308e6b'
  }, 5000);
});

document.addEventListener('DOMContentLoaded',() => {
  var timeRem=45
  var timer=document.getElementById("timer")
  timer.innerText=timeRem

  setInterval(function(){
    timeRem--
    timer.innerText=timeRem
    if(timeRem<=10 && timeRem%2==0){
      timer.style.color='red'
      document.getElementById("time-left").style.color='red'
    }
    else{
      timer.style.color='black'
      document.getElementById("time-left").style.color='black'
    }
    if(timeRem<=0){
      // clearInterval(count);  //setInterval returns id which is used to clear it
      window.location.reload(); 
    }
  },1000)
})

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}

function allowDrop(ev) {
  ev.preventDefault();
}

function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  var target = ev.target;
  // If dropping on an image, get the parent div if it's a valid drop zone
  if (target.tagName === 'IMG') {
    target = target.parentNode;
  }
  
  // Only proceed if the target is a drop zone
  if (target.id.startsWith("div")) {
    var draggedElement = document.getElementById(data);
    // Check if the drop zone already has an image
    if (target.children.length === 0 || target.contains(draggedElement)) {
      target.appendChild(draggedElement);
    } 
    else {
      // where the drop zone already has a child
      console.log("Drop zone is not empty.");
      return; // Exit the function to prevent appending
    }
    
    // Remove 'correct' class from all drop zones to reset their state
    resetCorrectClasses();
    
    // Re-check all pieces to update their 'correct' state
    recheckAllPieces();
    
    // Delay checking if the puzzle is solved to allow the UI to update
    setTimeout(checkPuzzleSolved, 100); // 100 milliseconds delay
  }
}

function resetCorrectClasses() {
  var allDropZones = document.querySelectorAll('[id^="div"]');
  allDropZones.forEach(function(zone) {
    zone.classList.remove('correct');
  });
}

function recheckAllPieces() {
  var allDropZones = document.querySelectorAll('[id^="div"]');
  allDropZones.forEach(function(zone) {
    var child = zone.querySelector('img'); // Assuming only one child image per drop zone
    if (child && zone.getAttribute('data-correct-piece') === child.id) {
      zone.classList.add('correct');
    }
  });
}

function checkPuzzleSolved() {
  var correctPieces = document.querySelectorAll('.correct').length;
  var totalPieces = 9;
  
  if (correctPieces === totalPieces) {
    alert('Puzzle solved!');
    window.location.reload()
    // window.location.href=""
  }
}