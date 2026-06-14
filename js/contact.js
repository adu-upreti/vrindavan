// contact.js — Vrindavan Contact Page

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

// Live open/closed status based on Nepal time (UTC+5:45)
function updateOpenStatus() {
  const now = new Date();
  const utc = now.getTime() + now.getTimezoneOffset() * 60000;
  const nepal = new Date(utc + (5 * 60 + 45) * 60000);
  const hours   = nepal.getHours();
  const minutes = nepal.getMinutes();
  const totalMins = hours * 60 + minutes;

  // Open: 6:00 AM (360) to 11:00 PM (1380)
  const isOpen = totalMins >= 360 && totalMins < 1380;

  const statusEl  = document.getElementById('openStatus');
  const dotEl     = document.querySelector('.open-dot');
  if (!statusEl || !dotEl) return;

  if (isOpen) {
    statusEl.textContent = 'We are Open Now';
    statusEl.style.color = '#16a34a';
    dotEl.style.background = '#4ade80';
  } else {
    statusEl.textContent = 'Currently Closed — Opens 6:00 AM';
    statusEl.style.color = '#dc2626';
    dotEl.style.background = '#f87171';
    dotEl.style.animation = 'none';
  }
}

updateOpenStatus();

// Scroll reveal for contact cards
const cards = document.querySelectorAll('.ci-card, .social-card');
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
