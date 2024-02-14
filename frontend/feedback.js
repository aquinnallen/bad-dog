document.getElementById('feedbackForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    // Get form values
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var feedback = document.getElementById('feedback').value;

    // Validate form inputs
    var errorMessage = '';
    if (!name.trim()) {
        errorMessage += 'Please enter your name.\n';
    }
    if (!email.trim()) {
        errorMessage += 'Please enter your email.\n';
    } else if (!isValidEmail(email)) {
        errorMessage += 'Please enter a valid email address.\n';
    }
    if (!feedback.trim()) {
        errorMessage += 'Please enter your feedback.\n';
    }

    if (errorMessage) {
        alert(errorMessage);
    } else {
        // Simulate form submission (you can replace this with your actual submission logic)
        document.getElementById('feedbackForm').reset();
        document.getElementById('successMessage').style.display = 'block';
    }
});

function isValidEmail(email) {
    // Basic email validation using regular expression
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}