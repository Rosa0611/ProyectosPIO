// Funcionalidad del modo oscuro
const toggleButton = document.getElementById('darkModeToggle');
const body = document.body;

toggleButton.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
    if (body.classList.contains('dark-mode')) {
    toggleButton.textContent = 'Modo Claro';
    } else {
    toggleButton.textContent = 'Modo Oscuro';
        }
});

// Funcionalidad de filtrado y orden
const filterButton = document.getElementById('applyFilter');
const moviesGrid = document.getElementById('moviesGrid');

filterButton.addEventListener('click', () => {
    const filterYear = document.getElementById('filterYear').value;
    const sortBy = document.getElementById('sortBy').value;

    let movies = Array.from(moviesGrid.children);

  // Filtrar por año
    if (filterYear) {
    movies = movies.filter(movie => movie.dataset.year === filterYear);
    }

  // Ordenar
    movies.sort((a, b) => {
        if (sortBy === 'title') {
            return a.dataset.title.localeCompare(b.dataset.title);
        } else if (sortBy === 'year') {
            return parseInt(a.dataset.year) - parseInt(b.dataset.year);
        }
    });

  // Vaciar la cuadrícula y agregar las películas filtradas y ordenadas
    moviesGrid.innerHTML = '';
    movies.forEach(movie => moviesGrid.appendChild(movie));
});