window.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM fully loaded and parsed');
    getLocation();

});

function myFunction() {
    alert("Hello World")
}

var x = document.getElementById("location");

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
    console.log("This was called.")
}

function showPosition(position) {
    x.innerHTML = "Latitude: " + position.coords.latitude + "<br>Longitude: " + position.coords.longitude;
    console.log("This was called too.");
}

var map;
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 50.2, lng: 50.3 },
        zoom: 8
    });
}