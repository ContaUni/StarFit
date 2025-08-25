document.addEventListener("DOMContentLoaded", () => {
    const passwordFields = document.querySelectorAll('input[type="password"]');

    passwordFields.forEach(field => {
        const toggle = document.createElement('span');
        toggle.textContent = '👁️';
        toggle.title = 'Mostrar senha';
        toggle.style.cursor = 'pointer';
        toggle.style.marginLeft = '8px';
        toggle.style.userSelect = 'none';
        toggle.style.fontSize = '18px';

        field.parentNode.appendChild(toggle);

        toggle.addEventListener('click', () => {
            if (field.type === 'password') {
                field.type = 'text';
                toggle.textContent = '🙈';
                toggle.title = 'Esconder senha';
            } else {
                field.type = 'password';
                toggle.textContent = '👁️';
                toggle.title = 'Mostrar senha';
            }
        });
    });
});
