
    function addMarkersforwhatthefork(locations) {
    // Clear existing markers from the cluster group
        map.removeLayer(whatthefork);
        whatthefork.clearLayers();

    // Loop through each location object in the response
    locations.forEach(location => {
        const lat = parseFloat(location.lat);
        const lng = parseFloat(location.lng);
        const name = location.name;  // Access 'name' field

        // Add marker if valid latitude and longitude exist
        if (!isNaN(lat) && !isNaN(lng)) {
            const marker = L.marker([lat, lng],{icon:whatthefork_icon}).bindPopup(name);
            whatthefork.addLayer(marker);  // Add marker to cluster group
        } else {
            console.warn(`Invalid coordinates for ${name}: ${lat}, ${lng}`);
        }
    });
    map.addLayer(whatthefork);
}

    // Handle toggle switch for justeat***//
    document.getElementById('wtf').addEventListener('change',
        function () {
        const cachedData = localStorage.getItem('whattheforkapiData')
            var isChecked = this.checked;

            if (isChecked) {
                console.log('Toggle is on, making API request... for whatthefork');

                if (cachedData){
                    console.log('checking the LocalStorage... data.....')
                    const parsedData = JSON.parse(cachedData)
                     // Store data in local storage
                    // return JSON.parse(cachedData);
                    addMarkersforwhatthefork(parsedData);
                }

                else {
                    console.log("No cached data found.....")
                    // Fetch data from your API with the X-API-KEY header
                    fetch('http://datamap.mealzo.co.uk/api/whatthefork/?fields=name,lat,lng')
                        .then(response => {
                            console.log('Response received:', response);

                            return response.json();
                        })
                        .then(data => {
                            console.log('Data received:', data);
                            localStorage.setItem('whattheforkapiData',JSON.stringify(data));
                            addMarkersforwhatthefork(data);
                        })
                        .catch(error => {
                            console.error('Error fetching data:', error);
                        });
                }
            }


            else {
                // Clear existing markers from the cluster group
                //markers.clearLayers();
                // console.error('Error fetching data:', error);
                map.removeLayer(whatthefork)
            }
        });

