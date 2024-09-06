 // Initialize the map
    var map = L.map('map').setView([51.505, -0.09], 13);

    // Load and display the tile layer from OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19
    }).addTo(map);

    // Create a layer group for clustering
    var markers = L.markerClusterGroup();
    map.addLayer(markers);