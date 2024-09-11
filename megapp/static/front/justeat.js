
    function addMarkersforjusteat(locations) {
    // Clear existing markers from the cluster group
        map.removeLayer(justeat);
        justeat.clearLayers();

    // Loop through each location object in the response
    locations.forEach(location => {
        const lat = parseFloat(location.lat);
        const lng = parseFloat(location.lng);
        const name = location.name;  // Access 'name' field
        const rating = location.rating || 'No ratings';
        const starRating = location.starRating || 'No star rating';
         // Ensure cuisines is always an array
        let cuisinesArray = [];
        try {
            if (typeof location.cuisines === 'string') {
                // Convert single quotes to double quotes for valid JSON
                const jsonString = location.cuisines.replace(/'/g, '"');
                cuisinesArray = JSON.parse(jsonString);
            } else if (Array.isArray(location.cuisines)) {
                cuisinesArray = location.cuisines;
            }
        } catch (error) {
            cuisinesArray = [];
        }

        // Extract the 'name' values from 'cuisines' and join them
        const cuisines = cuisinesArray.length > 0
            ? cuisinesArray.map(cuisine => {


                // Return the name if it exists, else return 'Unknown cuisine'
                return cuisine && cuisine.name ? cuisine.name : 'Unknown cuisine';
            }).join(', ')
            : 'No cuisines available';  // Default value if array is empty



        if (!isNaN(lat) && !isNaN(lng)) {
             var popupContent = `
                <img src='./static/img/shop.png' alt="Facebook" width="25"> <strong>${name}</strong><br>
                <img src='./static/img/rating.png' alt="Facebook" width="25"> Rate : ${starRating}<br>
                Review count : ${rating}<br>              
                Shop type : ${cuisines}<br>
            `;
            const marker = L.marker([lat, lng],{icon:justeat_icon}).bindPopup(popupContent);
            justeat.addLayer(marker);  // Add marker to cluster group
        } else {
            console.warn(`Invalid coordinates for ${name}: ${lat}, ${lng}`);
        }
    });
    map.addLayer(justeat);
}





// Handle toggle switch for justeat***//
    document.getElementById('just').addEventListener('change',
        function () {
        //const cachedData =localStorage.getItem('justeatapidata')
            var isChecked = this.checked;


            if (isChecked) {
                console.log('Toggle is on, making API request... for justeat');
                const chacheName ='justeatCache'
                const apiurl ='http://datamap.mealzo.co.uk/api/justeat/?fields=name,lat,lng,rating,starRating,cuisines,'
                //if(cachedData){
                    //console.log('checking the cached data.....')
                    //const parsedData = JSON.parse(cachedData)
                     // Store data in local storage
                    // return JSON.parse(cachedData);
                    //addfoodhubMarkers(parsedData);
                caches.open(chacheName).then(cache =>
                {
                    cache.match(apiurl).then(cachedResponse =>{
                        if (cachedResponse) {
                            console.log('Cached response found:', cachedResponse);
                            cachedResponse.json().then(data =>{
                                addMarkersforjusteat(data);
                            })
                        }
                        else {
                            console.log("No cached data found")
                            // Fetch data from your API with the X-API-KEY header
                            fetch('http://datamap.mealzo.co.uk/api/justeat/?fields=name,lat,lng,rating,starRating,cuisines,')
                                .then(response => {
                                    console.log('Response received:', response);
                                    const clonedResponse = response.clone();
                                    // return response.json();
                                    return response.json().then(data => {
                                        // Cache the cloned response for future use
                                        cache.put(apiurl, clonedResponse);
                                        console.log('Response received:', data);

                                        addMarkersforjusteat(data)

                            });
                        })
                        // .then(data => {
                        //     console.log('Data received:', data);
                        //     addMarkersforjusteat(data);
                        //     //localStorage.setItem('justeatapidata',JSON.stringify(data))
                        //     //Clone the response for chaching
                        //
                        //    // cache.put(apiurl,data.clone());
                        //
                        // })
                        .catch(error => {
                            console.error('Error fetching data:', error);
                        });
                      }
                        })
                    })

                 }
              else {
                // Clear existing markers from the cluster group
                //markers.clearLayers();
                // console.error('Error fetching data:', error);
                map.removeLayer(justeat)

            }



        });

