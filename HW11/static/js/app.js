// from data.js
var tableData = data;

// Defining the contents of the table.
tableContents = d3.select("tbody");

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

// Matched data that's filtered by date
var UfoMatches = tableData.filter(filterByDate);

var filterDate= "1/11/2010";

// Initial adding the table data
tableData.forEach(populateTable);

// Test populating with filter
UfoMatches.forEach(populateTable);
