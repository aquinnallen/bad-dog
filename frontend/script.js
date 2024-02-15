async function uploadFile() {
    document.getElementById("results-box").innerHTML = ""
    var fileInput = document.getElementById('audioFile');
    var file = fileInput.files[0];
    var fileExtension = file.name.slice(-4)
    console.log(fileExtension)
    // Check if a file is selected
    if (!file) {
        displayUploadStatus('Please select a file to upload', 'error');
        return;
    }
    if (!fileExtension.startsWith('.wav')){
       displayUploadStatus('Please select a .wav file', 'error');
       return;
    }

    // Check if the selected file is an audio file
    if (!file.type.startsWith('audio/')) {
        displayUploadStatus('Please select an audio file', 'error');
        return;
    }
    console.log(file.name.length)
    // Display loading indicator
    displayUploadStatus('Uploading...', 'info');

    // Proceed with file upload
    var formData = new FormData();
    formData.append('audioFile', file);

    // Use Fetch API to send file data to the server
    let newDiv = await fetch('http://192.9.248.32:5000/upload_audio_file', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            // Handle successful upload
            displayUploadStatus('File uploaded successfully', 'success');
            return response.json()
        } else {
            // Handle upload error
            displayUploadStatus('Error uploading file', 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        displayUploadStatus('Error: ' + error.message, 'error');
    });
    console.log(newDiv)
    document.getElementById("results-box").appendChild(displayReturn(newDiv))

}

function displayUploadStatus(message, type) {
    var uploadStatus = document.getElementById('uploadStatus');
    uploadStatus.textContent = message;
    uploadStatus.className = type;

}

function displayReturn(jsonObj) {
 // Create a new <div> element
    var div = document.createElement("div");
    div.classList.add("json-container");

    // Iterate through each key-value pair in the JSON object
    for (var key in jsonObj) {
        if (jsonObj.hasOwnProperty(key)) {
            // Create a <div> for the key
            var keyDiv = document.createElement("div");
            keyDiv.classList.add("json-key"); 
            keyDiv.textContent = key + ":";

            // Create a <div> for the value
            var valueDiv = document.createElement("div");
            valueDiv.classList.add("json-value");
            if (typeof jsonObj[key] === "object") {
                // If the value is an object, recursively call displayJSON
                valueDiv.appendChild(displayReturn(jsonObj[key]));
            } else {
                valueDiv.textContent = jsonObj[key];
            }

            // Append key and value <div>s to the main <div>
            div.appendChild(keyDiv);
            div.appendChild(valueDiv);
        }
    }

    // Return the created <div> element
    return div;
}
