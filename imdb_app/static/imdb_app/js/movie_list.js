document.getElementById('filter-btn').addEventListener('click', () => fetchMovies(1));
document.getElementById('search').addEventListener('keyup', debounce(() => fetchMovies(1), 300));
document.getElementById('sort').addEventListener('change', () => fetchMovies(1));

// Debounce function to limit API calls
function debounce(func, delay) {
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), delay);
    };
}

// Add pagination variables
let currentPage = 1;
const moviesPerPage = 10;

function fetchMovies(page = 1) {
    const search = document.getElementById('search').value;
    const sort = document.getElementById('sort').value;
    const releaseDate = document.getElementById('release-date').value;
    const language = document.getElementById('language').value; // New line to get selected language
    let url = `/api/movies/?page=${page}&`;

    if(search){
        url += `search=${encodeURIComponent(search)}&`;
    }
    if(sort){
        url += `ordering=${encodeURIComponent(sort)}&`;
    }
    if(releaseDate){ // New line to add release date filter
        url += `release_date=${encodeURIComponent(releaseDate)}&`;
    }
    if(language){ // New line to add language filter
        url += `original_language=${encodeURIComponent(language)}&`;
    }

    fetch(url)
    .then(response => response.json())
    .then(data => {
        const tbody = document.querySelector('#movies-table tbody');
        tbody.innerHTML = '';
        data.results.forEach(movie => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${movie.title}</td>
                <td>${movie.original_title}</td>
                <td>${movie.release_date ? new Date(movie.release_date).toLocaleDateString() : 'N/A'}</td>
                <td>$${movie.budget.toLocaleString()}</td>
                <td>$${movie.revenue.toLocaleString()}</td>
                <td>${movie.vote_average}</td>
            `;
            tbody.appendChild(row);
        });

        // Handle pagination display
        handlePagination(data.num_pages, data.current_page);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Function to handle pagination display with limited page buttons and navigation arrows
function handlePagination(totalPages, currentPage) {
    const paginationContainer = document.getElementById('pagination');
    paginationContainer.innerHTML = '';

    // Create Previous Arrow
    const prevButton = document.createElement('button');
    prevButton.innerText = '<';
    prevButton.disabled = currentPage === 1;
    prevButton.onclick = () => {
        if (currentPage > 1) {
            fetchMovies(currentPage - 1);
        }
    };
    paginationContainer.appendChild(prevButton);

    // Determine the range of page buttons to display
    let startPage = Math.max(1, currentPage - 2);
    let endPage = Math.min(totalPages, currentPage + 2);

    // Adjust if at the start or end
    if (currentPage <= 3) {
        endPage = Math.min(5, totalPages);
    }
    if (currentPage >= totalPages - 2) {
        startPage = Math.max(totalPages - 4, 1);
    }

    // Create page buttons
    for (let i = startPage; i <= endPage; i++) {
        const pageButton = document.createElement('button');
        pageButton.innerText = i;
        if (i === currentPage) {
            pageButton.classList.add('active');
        }
        pageButton.onclick = () => {
            fetchMovies(i);
        };
        paginationContainer.appendChild(pageButton);
    }

    // Create Next Arrow
    const nextButton = document.createElement('button');
    nextButton.innerText = '>';
    nextButton.disabled = currentPage === totalPages;
    nextButton.onclick = () => {
        if (currentPage < totalPages) {
            fetchMovies(currentPage + 1);
        }
    };
    paginationContainer.appendChild(nextButton);
}

// Initial fetch on page load
document.addEventListener('DOMContentLoaded', () => {
    fetchMovies(currentPage);
});
