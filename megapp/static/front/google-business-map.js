// Function to add markers to the map
    function addgooglebusinessdatamarkers(locations) {
    // Clear existing markers from the cluster group
    // markers.clearLayers();
        map.removeLayer(googlebusiness);
        googlebusiness.clearLayers();
    // Loop through each location object in the response
    locations.forEach(location => {
        const lat = parseFloat(location.latitude);
        const lng = parseFloat(location.longitude);
        const name = location.title;  // Access 'name' field
        const url = location.url ? formatUrl(location.url) : '#';
        // const facebook = location.facebook;
        // const twitter = location.twitter;
        // const android_link = location.android_link;



        if (!isNaN(lat) && !isNaN(lng)) {
            var popupContent = `
                <img src='./static/img/shop.png' alt="Facebook" width="25"> <strong>${name}</strong><br>
                <img src='./static/img/url.png' alt="Facebook" width="25"> <a href="${url}" target="_blank" rel="noopener noreferrer">${url}</a><br>
                
            `;
            const marker = L.marker([lat, lng], {icon: googlebusiness_icon}).bindPopup(popupContent);
           googlebusiness.addLayer(marker);  // Add marker to cluster group
        } else {
            console.warn(`Invalid coordinates for ${name}: ${lat}, ${lng}`);
        }
    });
    map.addLayer(googlebusiness);
}

// Handle toggle switch for foodhub//
    document.getElementById('google').addEventListener('change',
        function () {
            // const cachedData = localStorage.getItem('googlebusinessdata');
            var isChecked = this.checked;

            if (isChecked) {
                console.log('Toggle is on, making API request...for googlebusiness');
                const chacheName='google'
                //if (cachedData) {
                    //console.log('checking the LocalStorage data.....')
                    //const parsedData = JSON.parse(cachedData)
                     // Store data in local storage
                    // return JSON.parse(cachedData);
                    //addfoodhubMarkers(parsedData);

                //}
                caches.open(chacheName).then(cache => {
                    cache.match('http://127.0.0.1:8000/api/businessinformation/').then(cachedResponse => {
                        if (cachedResponse) {
                            console.log('Cached response found:', cachedResponse);
                            cachedResponse.json().then(data => {
                                addgooglebusinessdatamarkers(data);
                            })
                        } else {
                            console.log("No cached data found ......")
                            // Fetch data from your API with the X-API-KEY header
                            fetch('http://127.0.0.1:8000/api/businessinformation/')
                                .then(response => {
                                    console.log('Response received:', response);
                                    const clonedResponse = response.clone();
                                    return response.json().then(data => {
                                        cache.put('http://127.0.0.1:8000/api/businessinformation/', clonedResponse);
                                        console.log('Response received:', data);
                                        addgooglebusinessdatamarkers(data);
                                    });
                                })
                                // .then(data => {
                                //     console.log('Data received:', data);
                                //     localStorage.setItem('foodhubData', JSON.stringify(data));
                                //     addfoodhubMarkers(data);
                                // })
                                .catch(error => {
                                    console.error('Error fetching data:', error);
                                });
                            // Clear existing markers from the cluster group
                            // markers.clearLayers();
                        }
                    })
                })

        }
            else {
                map.removeLayer(googlebusiness)}
            });

//Function to ensure URL is properly formatted
function formatUrl(url) {
    try {
        // Ensure the URL has a protocol
        if (!url.match(/^https?:\/\//i)) {
            url = 'http://' + url; // Prepend http:// if missing
        }
        const formattedUrl = new URL(url); // Check if it's a valid URL
        return formattedUrl.href; // Return the absolute URL
    } catch (e) {
        console.error('Invalid URL:', url);
        return '#'; // Return a fallback URL if invalid
    }
}