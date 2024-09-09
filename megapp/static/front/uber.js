
// Function to add markers to the map
    function addMarkersforubereats(locations) {
    // Clear existing markers from the cluster group
    // markers.clearLayers();
        map.removeLayer(ubereats)

    // Loop through each location object in the response
    locations.forEach(location => {
        const lat = parseFloat(location.Latitude);
        const lng = parseFloat(location.Longitude);
        const name = location.name;  // Access 'name' field

        // Add marker if valid latitude and longitude exist
        if (!isNaN(lat) && !isNaN(lng)) {
            const marker = L.marker([lat, lng],{icon:ubereats_icon}).bindPopup(name);
            ubereats.addLayer(marker);  // Add marker to cluster group
        } else {
            console.warn(`Invalid coordinates for ${name}: ${lat}, ${lng}`);
        }
    });
        map.addLayer(ubereats)
}


// Handle toggle switch for foodhub//
    document.getElementById('uber').addEventListener('change',
        function () {
            var isChecked = this.checked;

            if (isChecked) {
                console.log('Toggle is on, making API request...for ubereats');
                // Fetch data from your API with the X-API-KEY header
                fetch('http://localhost:8000/api/ubereats/?fields=name,Latitude,Longitude')
                    .then(response => {
                        console.log('Response received:', response);

                        return response.json();
                    })
                    .then(data => {
                        console.log('Data received:', data);
                        addMarkersforubereats(data);
                    })
                    .catch(error => {
                        console.error('Error fetching data:', error);
                    });
            } else {
                // Clear existing markers from the cluster group
                //markers.clearLayers();
                map.removeLayer(ubereats)
            }
        });