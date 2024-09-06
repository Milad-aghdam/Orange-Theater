
    function addMarkersforjusteat(locations) {
    // Clear existing markers from the cluster group
    // markers.clearLayers();

    // Loop through each location object in the response
    locations.forEach(location => {
        const lat = parseFloat(location.lat);
        const lng = parseFloat(location.lng);
        const name = location.name;  // Access 'name' field

        // Add marker if valid latitude and longitude exist
        if (!isNaN(lat) && !isNaN(lng)) {
            const marker = L.marker([lat, lng]).bindPopup(name);
            markers.addLayer(marker);  // Add marker to cluster group
        } else {
            console.warn(`Invalid coordinates for ${name}: ${lat}, ${lng}`);
        }
    });
}

    // Handle toggle switch for justeat***//
    document.getElementById('just').addEventListener('change',
        function () {
            var isChecked = this.checked;

            if (isChecked) {
                console.log('Toggle is on, making API request... for justeat');
                // Fetch data from your API with the X-API-KEY header
                fetch('http://localhost:8000/api/justeat/?fields=name,lat,lng')
                    .then(response => {
                        console.log('Response received:', response);

                        return response.json();
                    })
                    .then(data => {
                        console.log('Data received:', data);
                        addMarkersforjusteat(data);
                    })
                    .catch(error => {
                        console.error('Error fetching data:', error);
                    });
            } else {
                // Clear existing markers from the cluster group
                markers.clearLayers();
                // console.error('Error fetching data:', error);
            }
        });

