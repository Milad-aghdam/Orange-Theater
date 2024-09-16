
    function addMarkersforfoodhouse(locations) {
    // Clear existing markers from the cluster group
        map.removeLayer(foodhouse);
        foodhouse.clearLayers();

    // Loop through each location object in the response
    locations.forEach(location => {
        const lat = parseFloat(location.latitude);
        const lng = parseFloat(location.longitude);
        const name = location.name;  // Access 'name' field



        // Add marker if valid latitude and longitude exist
        if (!isNaN(lat) && !isNaN(lng)) {
            var popupContent = `
                <div style="display: flex; align-items: center; margin-bottom: 10px;">
                    <img src='./static/img/shop.png' alt="Shop" width="25" style="margin-right: 5px;">
                    <strong>${name}</strong>
                </div>
                
            `;
            const marker = L.marker([lat, lng],{icon:foodhouse_icon}).bindPopup(popupContent);
            foodhouse.addLayer(marker);  // Add marker to cluster group
        } else {
            console.warn(`Invalid coordinates for ${name}: ${lat}, ${lng}`);
        }
    });
    map.addLayer(foodhouse);
}

    // Handle toggle switch for justeat***//
    document.getElementById('foodhuse').addEventListener('change',
        function () {
        const cachedData = localStorage.getItem('foodhouse')
            var isChecked = this.checked;

            if (isChecked) {
                console.log('Toggle is on, making API request... for foodhouse');

                if (cachedData){
                    console.log('checking the LocalStorage... data.....')
                    const parsedData = JSON.parse(cachedData)
                     // Store data in local storage
                    // return JSON.parse(cachedData);
                    addMarkersforfoodhouse(parsedData);
                }

                else {
                    console.log("No cached data found.....")
                    // Fetch data from your API with the X-API-KEY header
                    fetch('http://127.0.0.1:8000/api/foodhouse/?fields=name,latitude,longitude')
                        .then(response => {
                            console.log('Response received:', response);

                            return response.json();
                        })
                        .then(data => {
                            console.log('Data received:', data);
                            localStorage.setItem('foodhouse',JSON.stringify(data));
                            addMarkersforfoodhouse(data);
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

