
    const carouselData = [
        {
            title: "Unlocking Vital: Insights Your Blood, Your Lab",
            text: "Unlocking Vital Insights: Where Your Blood Holds the Key to Your Health – Welcome to Your Trusted Laboratory..",
        },
        {
            title: "Your Journey to Wellness: Precision Diagnostics, Compassionate Care.",
            text: "Experience excellence in healthcare at our state-of-the-art lab,where precision meets compassion for your well-being.",
        }
        // Add more data as needed
    ];

    let currentIndex = 0;
    const titleElement = document.getElementById("carouselTitle");
    const textElement = document.getElementById("carouselText");
    const slides = document.querySelectorAll(".mySlides");

    function showSlide(index) {
        titleElement.textContent = carouselData[index].title;
        textElement.textContent = carouselData[index].text;
        slides.forEach(slide => slide.style.display = "none");
        slides[index].style.display = "block";
    }

    function carousel() {
        showSlide(currentIndex);
        currentIndex = (currentIndex + 1) % carouselData.length;
        setTimeout(carousel, 3000); // Change image and content every 3 seconds
    }

    // Initial call to start the carousel
    carousel();
