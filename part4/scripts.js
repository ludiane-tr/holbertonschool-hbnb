document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();  // Empêcher le rechargement de la page

            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            try {
                const response = await fetch('https://your-api-url/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password })
                });

                if (response.ok) {
                    const data = await response.json();
                    // Stocker le JWT dans un cookie
                    document.cookie = `token=${data.access_token}; path=/`;

                    // Rediriger vers la page principale après une connexion réussie
                    window.location.href = 'index.html';  // Rediriger vers la page principale
                } else {
                    // Afficher un message d'erreur en cas de connexion échouée
                    alert('Échec de la connexion : ' + response.statusText);
                }
            } catch (error) {
                // Gestion des erreurs réseau
                console.error('Erreur réseau:', error);
                alert('Une erreur est survenue, veuillez réessayer.');
            }
        });
    }
});
