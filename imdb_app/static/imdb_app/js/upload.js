document.getElementById('upload-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    const loader = document.getElementById('loader');
    const messageDiv = document.getElementById('message');
    
    // Show the loader
    loader.style.display = 'block'; // This line shows the loader
    messageDiv.innerHTML = '';

    fetch('/api/upload_csv/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Hide the loader
        loader.style.display = 'none'; // This line hides the loader after upload
        
        if(data.error){
            messageDiv.innerHTML = `<p style="color:red;">${data.error}</p>`;
        } else {
            messageDiv.innerHTML = `<p style="color:green;">${data.message}</p>`;
            document.getElementById('upload-form').reset();
        }
    })
    .catch(error => {
        console.error('Error:', error);
        // Hide the loader
        loader.style.display = 'none';
        messageDiv.innerHTML = `<p style="color:red;">An error occurred.</p>`;
    });
});
