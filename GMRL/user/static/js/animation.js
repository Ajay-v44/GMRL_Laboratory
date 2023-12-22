 document.addEventListener("DOMContentLoaded", function() {
    // Find the message element
    var messageElement = document.querySelector(".alert");

    // Check if the message element exists
    if (messageElement) {
      // Set a timeout to hide the message after 5 seconds (5000 milliseconds)
      setTimeout(function() {
        messageElement.style.display = "none";
      }, 5000);
    }
  });

