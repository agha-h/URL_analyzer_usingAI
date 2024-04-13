document.addEventListener("DOMContentLoaded", function() {
    // Example functionality: Ensure the URL field is not empty before submission
    const form = document.querySelector('form');
    const urlInput = document.getElementById('url');

    form.addEventListener('submit', function(e) {
        if (urlInput.value.trim() === '') {
            e.preventDefault(); // Prevent form submission
            alert('Please enter a URL.');
            urlInput.focus(); // Focus on the URL input field
        }
        // You can add more checks here, such as validating the URL format
    });
});
