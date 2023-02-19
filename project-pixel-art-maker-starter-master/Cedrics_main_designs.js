//x = "height"
//y = "width"



function makeGrid() {
    const x = document.getElementById("inputHeight").value;
    const y = document.getElementById("inputWidth").value;
    const tbl = document.getElementById("pixelCanvas");
    
    for(let height = 0; height < x; height++) {
        const row = document.createElement("tr");
        for(let width = 0; width < y; width++) {
            const cell = document.createElement("td")
            cell.addEventListener('click', function() {
                const color = document.getElementById("colorPicker").value;
                cell.style.backgroundColor = color;
            }, true);
                row.appendChild(cell)
        }
        tbl.appendChild(row)
    }
    document.body.appendChild(tbl);
    
}

function reset() {
    const tbl = document.getElementById("pixelCanvas");
    let newtbl = tbl.firstElementChild;
    while(newtbl) {
        newtbl.remove();
        newtbl = tbl.firstElementChild;
    }
}


document.addEventListener('submit',(event) => {
    event.preventDefault();
    reset();
    makeGrid();
});