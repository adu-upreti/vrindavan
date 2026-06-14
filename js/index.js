// index.js — Vrindavan Homepage

// Navbar: scroll state + mobile menu
const navbar    = document.getElementById('navbar');
const navToggle = document.getElementById('navToggle');
const navLinks  = document.getElementById('navLinks');
const navOverlay = document.getElementById('navOverlay');

window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 60);
}, { passive: true });

function closeMobileNav() {
  navLinks.classList.remove('open');
  navToggle.classList.remove('open');
  navOverlay.classList.remove('open');
  navToggle.setAttribute('aria-expanded', 'false');
  document.body.style.overflow = '';
}

function openMobileNav() {
  navLinks.classList.add('open');
  navToggle.classList.add('open');
  navOverlay.classList.add('open');
  navToggle.setAttribute('aria-expanded', 'true');
  document.body.style.overflow = 'hidden';
}

navToggle.addEventListener('click', () => {
  const isOpen = navLinks.classList.contains('open');
  isOpen ? closeMobileNav() : openMobileNav();
});

navOverlay.addEventListener('click', closeMobileNav);

navLinks.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', closeMobileNav);
});

// Hero gallery slideshow
(function () {
  const slides = document.querySelectorAll('.gallery-slide');
  const dots   = document.querySelectorAll('.gdot');
  const label  = document.getElementById('galleryLabel');
  if (!slides.length) return;

  const labels = [
    'Fresh &amp; Delicious',
    'Made with Love 🙏',
    'Pure Vegetarian 🌿',
    'Served Daily ☀️',
    'Taste of Vrindavan'
  ];

  let current = 0;

  function goTo(n) {
    slides[current].classList.remove('active');
    dots[current].classList.remove('active');
    current = (n + slides.length) % slides.length;
    slides[current].classList.add('active');
    dots[current].classList.add('active');
    if (label) {
      label.style.opacity = '0';
      setTimeout(() => {
        label.innerHTML = labels[current];
        label.style.opacity = '1';
      }, 300);
    }
  }

  let timer = setInterval(() => goTo(current + 1), 2500);

  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => {
      clearInterval(timer);
      goTo(i);
      timer = setInterval(() => goTo(current + 1), 2500);
    });
  });
})();