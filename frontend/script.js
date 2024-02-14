
function uploadFile() {
    var fileInput = document.getElementById('audioFile');
    var file = fileInput.files[0];
    
    // Check if a file is selected
    if (!file) {
        displayUploadStatus('Please select a file to upload', 'error');
        return;
    }

    // Check if the selected file is an audio file
    if (!file.type.startsWith('audio/')) {
        displayUploadStatus('Please select an audio file', 'error');
        return;
    }

    // Display loading indicator
    displayUploadStatus('Uploading...', 'info');

    // Proceed with file upload
    var formData = new FormData();
    formData.append('audioFile', file);

    // Use Fetch API to send file data to the server
    fetch('the URL of your server side script that handles the file upload process', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            // Handle successful upload
            displayUploadStatus('File uploaded successfully', 'success');
        } else {
            // Handle upload error
            displayUploadStatus('Error uploading file', 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        displayUploadStatus('Error: ' + error.message, 'error');
    });
}

function displayUploadStatus(message, type) {
    var uploadStatus = document.getElementById('uploadStatus');
    uploadStatus.textContent = message;
    uploadStatus.className = type;

}