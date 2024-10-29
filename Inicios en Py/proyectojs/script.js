
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

// Funcionalidad de filtrado y 
const filterButton = document.getElementById('applyFilter');
const moviesGrid = document.getElementById('moviesGrid');
const originalMovies = Array.from(moviesGrid.children);

filterButton.addEventListener('click', () => {
    const filterYear = document.getElementById('filterYear').value.trim();
    const sortBy = document.getElementById('sortBy').value;

    const movies = Array.from(moviesGrid.getElementsByClassName('movie-item'));

  // Filtrar por año
    const filteredMovies = filterYear ? 
      movies.filter(movie => movie.dataset.year === filterYear) : 
      movies;

  // Ordenar por título o año
    const sortedMovies = filteredMovies.sort((a, b) => {
      if (sortBy === 'title') {
        return a.dataset.title.localeCompare(b.dataset.title);
      } else if (sortBy === 'year') {
        return parseInt(a.dataset.year) - parseInt(b.dataset.year);
      }
    });

  // Limpiar y agregar películas filtradas y ordenadas
    moviesGrid.innerHTML = '';
    sortedMovies.forEach(movie => moviesGrid.appendChild(movie));
  });


// Funcionalidad del botón "Inicio"
const inicioButton = document.getElementById('inicio');
inicioButton.addEventListener('click', (event) => {
    event.preventDefault(); // Prevenir el comportamiento por defecto del enlace


  // Limpiar la cuadrícula y mostrar todas las películas en su orden original
    moviesGrid.innerHTML = '';
    originalMovies.forEach(movie => moviesGrid.appendChild(movie));

  // Limpiar los filtros y restablecer los valores
    document.getElementById('filterYear').value = '';
    document.getElementById('sortBy').value = 'title';
  });