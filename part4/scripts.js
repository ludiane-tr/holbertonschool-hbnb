document.addEventListener('DOMContentLoaded', () => {
    console.log("Script chargé !"); // 🔍 Vérifie que le fichier JS est bien chargé

    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        console.log("Formulaire trouvé !"); // 🔍 Vérifie que le formulaire existe

        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault(); // Empêche le rechargement de la page

            const email = document.getElementById('email').value.trim();
            const password = document.getElementById('password').value.trim();
            const errorMessage = document.getElementById('error-message');

            console.log("Email :", email);
            console.log("Password :", password);

            // Vérifie si les champs sont remplis
            if (!email || !password) {
                console.log("Erreur : champs vides !");
                errorMessage.textContent = 'Tous les champs sont obligatoires.';
                errorMessage.style.display = 'block';
                return;
            }

            try {
                console.log("Envoi de la requête à l'API...");
                const response = await fetch('https://your-api-url/login', { // 🔴 Remplace par la vraie URL API
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password })
                });

                console.log("Réponse reçue :", response);

                if (!response.ok) {
                    throw new Error('Identifiants incorrects');
                }

                const data = await response.json();
                console.log("Données reçues :", data);

                document.cookie = `token=${data.access_token}; path=/`; // Stocke le token dans un cookie
                console.log("Token stocké !");

                window.location.href = 'index.html'; // Redirige vers la page principale
            } catch (error) {
                console.error("Erreur lors du login :", error.message);
                errorMessage.textContent = error.message || 'Erreur de connexion. Réessaie plus tard.';
                errorMessage.style.display = 'block';
            }
        });
    } else {
        console.error("❌ Formulaire introuvable !");
    }
});
