


// Function to add markers to the map
    function addfoodhubMarkers(locations) {
    // Clear existing markers from the cluster group
    // markers.clearLayers();
        map.removeLayer(foodhub);
        foodhub.clearLayers();
    // Loop through each location object in the response
    locations.forEach(location => {
        const lat = parseFloat(location.Latitude);
        const lng = parseFloat(location.Longitude);
        const name = location.name;  // Access 'name' field
        const url = location.url;
        
      
        

        if (!isNaN(lat) && !isNaN(lng)) {
            var popupContent = `
                <strong>${name}</strong><br>
                URL: <a href="${url}" target="_blank">${url}</a><br>
                <img src="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@5.15.4/svgs/brands/facebook.svg" alt="Facebook" width="25"/> : <a href="${url}" target="_blank">${url}</a><br>
            `;
            const marker = L.marker([lat, lng], {icon: foodhub_icon}).bindPopup(popupContent);
            foodhub.addLayer(marker);  // Add marker to cluster group
        } else {
            console.warn(`Invalid coordinates for ${name}: ${lat}, ${lng}`);
        }
    });
    map.addLayer(foodhub);
}

// Handle toggle switch for foodhub//
    document.getElementById('foodhub').addEventListener('change',
        function () {
            const cachedData = localStorage.getItem('foodhubData');
            var isChecked = this.checked;

            if (isChecked) {
                console.log('Toggle is on, making API request...for foodhub');

                if (cachedData) {
                    console.log('checking the LocalStorage data.....')
                    const parsedData = JSON.parse(cachedData)
                     // Store data in local storage
                    // return JSON.parse(cachedData);
                    addfoodhubMarkers(parsedData);

                }

                else {
                    console.log("No cached data found ......")
                    // Fetch data from your API with the X-API-KEY header
                    fetch('http://datamap.mealzo.co.uk/api/foodhub/?fields=name,Latitude,Longitude,url')
                        .then(response => {
                            console.log('Response received:', response);

                            return response.json();
                        })
                        .then(data => {
                            console.log('Data received:', data);
                            localStorage.setItem('foodhubData', JSON.stringify(data));
                            addfoodhubMarkers(data);
                        })
                        .catch(error => {
                            console.error('Error fetching data:', error);
                        });
                    // Clear existing markers from the cluster group
                    // markers.clearLayers();
                }


        }
            else {
                map.removeLayer(foodhub)

            }
            });