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
            <div style="text-align: center; color: gray; display: flex; justify-content: center; align-items: center; height: 23vh;">
                <iframe src="https://giphy.com/embed/JIX9t2j0ZTN9S" 
                        style="max-width: 100%; max-height: 100%; border: none;" 
                        allowFullScreen>
                </iframe>
            </div>
            <p style="color: brown; font-size: 20px;">No results to display. Start your search!</p>
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
        resultsDiv.innerHTML = "<p>No books found. </p>";
    } else {
        results.forEach(result => {
            const book = result.item;
            const bookDiv = document.createElement("div");

            //Add Goodreads and Google Books links
            const GoogleBooksURL = `https://www.google.com/search?q=${encodeURIComponent(book.Title + " " + book.Author)}`;
            bookDiv.innerHTML = `
                <h2 style="text-align: center; color: brown;">${book.Title} by ${book.Author}</h4>
                <div style="text-align: center;">
                    <a href="${book.URL.trim()}" target="_blank" style="text-decoration: none; color: black; transition: color 0.3s ease;">Goodreads</a><br>
                    <a href="${GoogleBooksURL}" target="_blank" style="text-decoration: none; color: black; transition: color 0.3s ease;">Google</a>
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
