window.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM fully loaded and parsed');
});

function myFunction() {
    alert("Hello World")
}

navigator.geolocation.getCurrentPosition(success);

var longi;
var lati;

function success(pos) {
    var crd = pos.coords;

    console.log('Your current position is:');
    console.log(`Latitude : ${crd.latitude}`);
    console.log(`Longitude: ${crd.longitude}`);
    console.log(`More or less ${crd.accuracy} meters.`);
    longi = crd.longitude;
    lati = crd.latitude;
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: crd.latitude, lng: crd.longitude },
        zoom: 14
    });
}

// function location(id) {
//     var marker = new google.maps.Marker({
//         position: { lat: lati, lng: longi },
//         map: map,
//         title: 'Hello World!'
//     });
//     console.log("This was called as well.")
// }






// function getLocation() {
//     if (navigator.geolocation) {
//         navigator.geolocation.getCurrentPosition(showPosition);
//     } else {
//         x.innerHTML = "Geolocation is not supported by this browser.";
//     }
//     console.log("This was called.")
//     longi = parseInt(position.coords.longitude, 10);
//     lati = parseInt(position.coords.latitude, 10);
//     console.log(lati);
// }

var x = document.getElementById("map");

function getLocation() {

}

// var map;
// function initMap() {
//     map = new google.maps.Map(document.getElementById('map'), {
//         center: { lat: 55, lng: 44 },
//         zoom: 8
//     });
// }