// Your code goes here!
function makeGrid(){
    const widthValue = document.getElementById("inputWidth").value;
    const heightValue = document.getElementById("inputHeight").value;

    const tbl = document.getElementById("pixelCanvas");

   for (let width = 0; width < widthValue; width++) {
    const trElem = document.createElement("tr");
    
    tbl.appendChild(trElem);
    for (let height = 0; height < heightValue; height++) {
       const tdElem = document.createElement("td");
       tdElem.addEventListener("click", (event) => {
        const colorValue = document.getElementById("colorPicker").value
        event.target.style.backgroundColor = colorValue;
       });
       trElem.appendChild(tdElem); 
    }

   }
}
   function clearGrid() {
    const tbl = document.getElementById("pixelCanvas");
    let row = tbl.firstElementChild;
    while (row) {
        row.remove();
        row = tbl.firstElementChild
    }
}


document.addEventListener('submit',(event) => {
    event.preventDefault();
    clearGrid();
    makeGrid();
});