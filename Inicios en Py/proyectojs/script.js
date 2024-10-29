
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

// Activar submenús en hover
document.querySelectorAll('.dropdown-submenu').forEach(function (element) {
  element.addEventListener('mouseenter', function () {
    let submenu = element.querySelector('.dropdown-menu');
    submenu.classList.add('show');
  });
  element.addEventListener('mouseleave', function () {
    let submenu = element.querySelector('.dropdown-menu');
    submenu.classList.remove('show');
  });
});

// Obtener el contenedor de películas y el año actual
const currentYear = new Date().getFullYear();

// Contadores de clics en cada película
const movieClickCounts = {};

// Funcionalidad para el botón "Novedades"
document.getElementById('novedades').addEventListener('click', (event) => {
  event.preventDefault();

  // Filtrar películas del año actual
  const movies = Array.from(moviesGrid.getElementsByClassName('movie-item'));
  const currentYearMovies = movies.filter(movie => parseInt(movie.dataset.year) === currentYear);

  // Mostrar solo las películas del año actual
  moviesGrid.innerHTML = '';
  currentYearMovies.forEach(movie => moviesGrid.appendChild(movie));
});

// Funcionalidad para el botón "Favoritos"
document.getElementById('favoritos').addEventListener('click', (event) => {
  event.preventDefault();

  // Filtrar películas con más clics (mayor a 0)
  const movies = Array.from(moviesGrid.getElementsByClassName('movie-item'));
  const favoriteMovies = movies.filter(movie => movieClickCounts[movie.dataset.title] > 0);

  // Ordenar las películas por cantidad de clics en orden descendente
  favoriteMovies.sort((a, b) => movieClickCounts[b.dataset.title] - movieClickCounts[a.dataset.title]);

  // Mostrar solo las películas favoritas
  moviesGrid.innerHTML = '';
  favoriteMovies.forEach(movie => moviesGrid.appendChild(movie));
});

// Funcionalidad para contar clics en las películas
moviesGrid.addEventListener('click', (event) => {
  const movieCard = event.target.closest('.movie-item');
  if (movieCard) {
    const movieTitle = movieCard.dataset.title;

    // Incrementa el contador de clics para esta película
    movieClickCounts[movieTitle] = (movieClickCounts[movieTitle] || 0) + 1;
  }
});