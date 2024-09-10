console.log('Toggle is on, making API request...');
// Fetch data from your API with the X-API-KEY header
 const cachedData = localStorage.getItem('apiData');




if (cachedDatata){

    console.log('Data has been stored');
    return JSON.parse(cachedData);
}
else {
fetch('http://127.0.0.1:8000/api/foodhub/?fields=name,Latitude,Longitude')
    .then(response => {
        console.log('Response received:', response);
        return response.json();
    })
    .then(data => {
        console.log('Data received:', data);
        // addMarkers(data);
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });  }

