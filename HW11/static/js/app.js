// from data.js
var tableData = data;

// Defining the contents of the table.
var tableContents = d3.select("tbody");

// Creating function to capitalize first letter of a string
function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

// Creating a function to clear the table contents
function clearTable(){
    tableContents.html("<tr></tr>")
}

// Creating a function to add data to the table
function populateTable(dataSet){
    tableContents.append("tr").html(
                        "<td>"+String(dataSet.datetime)+"</td>"+
                        "<td>"+capitalizeFirstLetter(String(dataSet.city))+"</td>"+
                        "<td>"+String(dataSet.state).toUpperCase()+"</td>"+
                        "<td>"+String(dataSet.country).toUpperCase()+"</td>"+
                        "<td>"+capitalizeFirstLetter(String(dataSet.shape))+"</td>"+
                        "<td>"+capitalizeFirstLetter(String(dataSet.duration))+"</td>"+
                        "<td>"+capitalizeFirstLetter(String(dataSet.comments))+"</td>"
                        );
}

// Function to filter by date
function filterByDate(ufo) {
    return ufo.datetime === filterDate;
  }

// Initial adding the table data
tableData.forEach(populateTable);

// Getting the button
var button = d3.select("#filter-btn");

button.on("click", function() {
    d3.event.preventDefault();
    clearTable();
    var dateInput=d3.select("#datetime")
    filterDate = dateInput.property("value");
    console.log(filterDate);
    var UfoMatches = tableData.filter(filterByDate);
    UfoMatches.forEach(populateTable);

});

