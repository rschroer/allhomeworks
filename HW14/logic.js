// Store our API endpoint inside queryUrl
var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

// Perform a GET request to the query URL
d3.json(queryUrl, function(data) {
  // Once we get a response, send the data.features object to the createFeatures function
  createFeatures(data.features);
});

function color(mag) {
  return mag > 4.5 ? '#FF0000':
         mag > 2.5 ? '#FFA500':
         '#FFFF00';
}

function createFeatures(earthquakeData) {


  // Define a function we want to run once for each feature in the features array
  // Give each feature a popup describing the place and time of the earthquake
    //    Select colors for circles

    props = []

    for ( var i=0 ; i < earthquakeData.length; i++ ) {
      props.push(L.circle([earthquakeData[i].geometry.coordinates[1],
                          earthquakeData[i].geometry.coordinates[0]],{
                            color: color(earthquakeData[i].properties.mag),
                            fillcolor: color(earthquakeData[i].properties.mag),
                            radius: Math.pow(earthquakeData[i].properties.mag,3) *1000
                          })
                          .bindPopup("<h3>" + earthquakeData[i].properties.place +
      "</h3><hr><p>" + new Date(earthquakeData[i].properties.time) +"</p><p>magnatude: "+ earthquakeData[i].properties.mag + "</p>"));
  }

  // Create a GeoJSON layer containing the features array on the earthquakeData object
  // Run the onEachFeature function once for each piece of data in the array
  
  // var earthquakes = L.circle(earthquakeData, {
  //   onEachFeature: onEachFeature
  // });
  


  // Sending our earthquakes layer to the createMap function
  createMap(props);
}

function createMap(earthquakes) {

  // Define streetmap and darkmap layers
  var streetmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.streets",
    accessToken: API_KEY
  });

  var darkmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.dark",
    accessToken: API_KEY
  });

  // Define a baseMaps object to hold our base layers
  var baseMaps = {
    "Street Map": streetmap,
    "Dark Map": darkmap
  };

  // Create overlay object to hold our overlay layer
  var earthquake = L.layerGroup(props);
  
  var overlayMaps = {
    "Earthquakes": earthquake
  };

  // Create our map, giving it the streetmap and earthquakes layers to display on load
  var myMap = L.map("map", {
    center: [
      37.09, -95.71
    ],
    zoom: 5,
    layers: [streetmap, earthquake]
  });

  // Create a layer control
  // Pass in our baseMaps and overlayMaps
  // Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);
}
