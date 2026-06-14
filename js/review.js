// review.js — Vrindavan Reviews Page

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

// Scroll reveal for highlight cards
const cards = document.querySelectorAll('.rh-card');
const observer = new IntersectionObserver((entries) => {
  entries.forEach((e, i) => {
    if (e.isIntersecting) {
      setTimeout(() => {
        e.target.style.opacity = '1';
        e.target.style.transform = 'translateY(0)';
      }, i * 80);
      observer.unobserve(e.target);
    }
  });
}, { threshold: 0.1 });

cards.forEach(card => {
  card.style.opacity = '0';
  card.style.transform = 'translateY(20px)';
  card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  observer.observe(card);
});