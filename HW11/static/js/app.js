// from data.js
var tableData = data;

// YOUR CODE HERE!

tableContents = d3.select("tbody");

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}
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

tableData.forEach(populateTable);