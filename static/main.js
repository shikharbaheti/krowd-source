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
