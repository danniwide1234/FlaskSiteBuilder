document.addEventListener('DOMContentLoaded', () => {
    toggleNavMenu();
    togglePasswordVisibility();
    validateForms();
    lazyLoadImages();
    setupEditPageForm(); // New function to handle edit page form
});

// Toggle the navigation menu on smaller screens
function toggleNavMenu() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('header nav ul');
    
    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', () => {
            navMenu.classList.toggle('open');
        });
    }
}

// Password visibility toggle
function togglePasswordVisibility() {
    document.querySelectorAll('.password-toggle').forEach(toggle => {
        toggle.addEventListener('click', () => {
            const target = document.getElementById(toggle.dataset.target);
            if (target) {
                target.type = target.type === 'password' ? 'text' : 'password';
                toggle.textContent = target.type === 'password' ? 'Show' : 'Hide';
            }
        });
    });
}

// Form validation
function validateForms() {
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', (event) => {
            let valid = true;

            form.querySelectorAll('[required]').forEach(field => {
                if (!field.value.trim()) {
                    valid = false;
                    field.classList.add('is-invalid');
                    field.classList.remove('is-valid');
                } else {
                    field.classList.add('is-valid');
                    field.classList.remove('is-invalid');
                }
            });

            if (!valid) {
                event.preventDefault();
                alert('Please fill out all required fields.');
            }
        });
    });
}

// Image lazy loading
function lazyLoadImages() {
    const lazyImages = document.querySelectorAll('img.lazy');

    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    observer.unobserve(img);
                }
            });
        });

        lazyImages.forEach(img => observer.observe(img));
    } else {
        lazyImages.forEach(img => {
            img.src = img.dataset.src;
            img.classList.remove('lazy');
        });
    }
}

// Setup edit page form interaction
function setupEditPageForm() {
    const editLinks = document.querySelectorAll('.edit-page-link');

    editLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault();

            const pageId = link.getAttribute('data-page-id');
            const pageTitle = link.getAttribute('data-page-title');
            const pageContent = link.getAttribute('data-page-content');

            const editForm = document.getElementById('editForm');
            if (editForm) {
                const editPageTitle = document.getElementById('edit_page_title');
                const editPageContent = document.getElementById('edit_page_content');

                if (editPageTitle && editPageContent) {
                    editPageTitle.value = pageTitle;
                    editPageContent.value = pageContent;

                    // Assuming the form action needs to be dynamically set (replace with your logic)
                    editForm.action = `/edit/${pageId}`;

                    // Show the edit form
                    document.getElementById('editPageForm').style.display = 'block';
                }
            }
        });
    });

    // Function to cancel editing
    function cancelEdit() {
        document.getElementById('editPageForm').style.display = 'none';
    }
}
