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
                <h2 style="text-align: center; color: yellowgreen;">${book.Title} by ${book.Author}</h4>
                <div style="text-align: center;">
                    <a href="${book.URL.trim()}" target="_blank" style="text-decoration: none; color: pink; transition: color 0.3s ease;">Goodreads Link</a><br>
                    <a href="${GoogleBooksURL}" target="_blank" style="text-decoration: none; color: violet; transition: color 0.3s ease;">Google Search Link</a>
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
    document.getElementById("results").innerHTML = "";
}
