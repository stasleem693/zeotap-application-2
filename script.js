// This script can be expanded with functionality like fetching data on button click

// Function to refresh weather data every 60 seconds (can be customized)
function refreshWeatherData() {
    setTimeout(function() {
        location.reload();  // Reload the page to refresh weather data
    }, 60000);  // 60000ms = 60 seconds
}

// Automatically refresh weather every 60 seconds when the page loads
window.onload = function() {
    refreshWeatherData();
};
