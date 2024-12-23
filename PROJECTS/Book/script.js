let books = [];

//load books data from JSON file 
fetch("books.json")
    .then(response => response.json())
    .then(data => {
        books = data;

        //initialize fuse.js wiht books data and search options to allow fuzzy search
        fuse = new Fuse(books, {
            keys: ['Title', 'Author'],
            threshold: 0.4,
        });
    })
    .catch(error => console.error("Error Loading Books data:", error))

function displayGif() {
    const resultsDiv = document.getElementById("results");

    resultsDiv.innerHTML = `
        <div style="text-align: center; color: gray;">
            <div style="text-align: center; color: gray; display: flex; justify-content: center; align-items: center; height: 18vh;">
                <iframe src="https://giphy.com/embed/JIX9t2j0ZTN9S" 
                        style="max-width: 100%; max-height: 100%; border: none;" 
                        allowFullScreen>
                </iframe>
            </div>
            <p style="color: brown; font-size: 0.6rem;">No results to display 😞 Start your search!</p>
        </div>
    `;
}

document.addEventListener('DOMContentLoaded', function () {
    displayGif();
})

function searchBooks() {
    const query = document.getElementById("search-input").value.toLowerCase();
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = "";

    //perform fuzzy search
    const results = fuse.search(query)

    if (results.length === 0) {
        resultsDiv.innerHTML = "<p style='text-align: center;'>No books found. </p>";
    } else {
        results.forEach(result => {
            const book = result.item;
            const bookDiv = document.createElement("div");

            //Add Goodreads and Google Books links
            const GoogleBooksURL = `https://www.google.com/search?q=${encodeURIComponent(book.Title + " " + book.Author)}`;
            bookDiv.innerHTML = `
                <h2 style="text-align: center; color: brown;">${book.Title} by ${book.Author}</h4>
                <div style="text-align: center;">
                    <a href="${book.URL.trim()}" target="_blank" style="text-decoration: none; color: black; transition: color 0.3s ease; font-size: 0.8rem;">Goodreads</a><br>
                    <a href="${GoogleBooksURL}" target="_blank" style="text-decoration: none; color: black; transition: color 0.3s ease; font-size: 0.8rem;">Google</a>
                </div>
            `;
            resultsDiv.appendChild(bookDiv)
        })
    }
}

//event listener for 'enter' key press
document.getElementById("search-input").addEventListener("keypress", function(event) {
    if(event.key === "Enter") {
        searchBooks();
    }
})

//function to clear input() 
function clearInput() {
    document.getElementById("search-input").value = "";
    
    displayGif();
}

//functions to handle switching tabs/sections
document.addEventListener('DOMContentLoaded', function () {
    // Get all the tab buttons and sections
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabSections = document.querySelectorAll('.tab-section');

    function switchTab(event) {
        // Remove the 'active' class from all buttons and sections
        tabButtons.forEach(button => button.classList.remove('active'));
        tabSections.forEach(section => section.classList.remove('active'));

        // Add the 'active' class to the clicked tab button and corresponding section
        const selectedSection = event.target.getAttribute('data-section');
        document.getElementById(selectedSection).classList.add('active');
        event.target.classList.add('active');
    }

    // Attach click event listeners to each tab button
    tabButtons.forEach(button => {
        button.addEventListener('click', switchTab);
    });

    // // Optionally, activate the first tab by default
    // document.querySelector('.tab-button.active').classList.add('active');
    // document.querySelector('.tab-section.active').classList.add('active');
});

