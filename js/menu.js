// menu.js — Vrindavan Menu Page

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

// Category filter
const filterBtns = document.querySelectorAll('.filter-btn');
const menuSections = document.querySelectorAll('.menu-section');

filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    const cat = btn.dataset.cat;
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    menuSections.forEach(sec => {
      if (cat === 'all' || sec.dataset.category === cat) {
        sec.classList.remove('hidden');
      } else {
        sec.classList.add('hidden');
      }
    });

    // Scroll to top of menu main
    if (cat !== 'all') {
      const target = document.getElementById(cat);
      if (target) {
        setTimeout(() => {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 50);
      }
    }
  });
});

// Hash navigation (e.g. menu.html#momo)
window.addEventListener('DOMContentLoaded', () => {
  const hash = window.location.hash.replace('#', '');
  if (hash) {
    const matchBtn = document.querySelector(`.filter-btn[data-cat="${hash}"]`);
    if (matchBtn) {
      matchBtn.click();
    }
  }
});