 // Initialize the map
    var map = L.map('map').setView([51.505, -0.09], 13);

    // Load and display the tile layer from OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19
    }).addTo(map);

    // // Create a layer group for clustering
    // var markers = L.markerClusterGroup();
    // map.addLayer(markers);

    var foodhub=L.markerClusterGroup();
    var justeat=L.markerClusterGroup();
    var foodhouse=L.markerClusterGroup();
    var ubereats=L.markerClusterGroup();
    var whatthefork=L.markerClusterGroup();
    var flipdish=L.markerClusterGroup();


    var foodhub_icon = L.icon({
        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png',
        // iconSize: [25, 41],  // size of the icon
        //iconAnchor: [12, 41], // point of the icon which will correspond to marker's location
        //popupAnchor: [1, -34], // point from which the popup should open relative to the iconAnchor
        shadowUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-shadow.png',
        //shadowSize: [41, 41]  // size of the shadow
    });

    var justeat_icon = L.icon({
        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-orange.png',
        // iconSize: [25, 41],  // size of the icon
        //iconAnchor: [12, 41], // point of the icon which will correspond to marker's location
        //popupAnchor: [1, -34], // point from which the popup should open relative to the iconAnchor
        shadowUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-shadow.png',
        //shadowSize: [41, 41]  // size of the shadow
    });

    var ubereats_icon = L.icon({
        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-green.png',
        // iconSize: [25, 41],  // size of the icon
        //iconAnchor: [12, 41], // point of the icon which will correspond to marker's location
        //popupAnchor: [1, -34], // point from which the popup should open relative to the iconAnchor
        shadowUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-shadow.png',
        //shadowSize: [41, 41]  // size of the shadow
    });

    var whatthefork_icon = L.icon({
        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-yellow.png',
        // iconSize: [25, 41],  // size of the icon
        //iconAnchor: [12, 41], // point of the icon which will correspond to marker's location
        //popupAnchor: [1, -34], // point from which the popup should open relative to the iconAnchor
        shadowUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-shadow.png',
        //shadowSize: [41, 41]  // size of the shadow
    });





