let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 38, lng: 128 },
    zoom: 8,
  });
}

window.initMap = initMap;