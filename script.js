// Fonction principale pour vérifier si un nombre est premier
async function verifierNombre() {
    // Récupérer les éléments du DOM
    const nombre = document.getElementById('monInput').value;
    const resultatDiv = document.getElementById('resultat');
    const bouton = document.getElementById('boutonVerifier');

    // Vérifier qu'un nombre est bien entré
    if (!nombre) {
        alert('Entre un nombre d\'abord !');
        return;
    }

    // Afficher un message de chargement
    resultatDiv.innerText = '⏳ L\'IA réfléchit...';
    resultatDiv.className = 'loading';
    bouton.disabled = true;

    try {
        // Appeler l'API FastAPI
        console.log('Appel de l\'API pour le nombre:', nombre);
        const reponse = await fetch(`http://localhost:8000/ai_premier/${nombre}`);
        console.log(reponse)
        const data = await reponse.json();

        console.log('Réponse de l\'API :', data);

        // Afficher le résultat
        resultatDiv.innerText = data.message || data.response || JSON.stringify(data.nombre);

        // Ajouter une classe selon le résultat
        if (data.is_prime === true || (data.message && data.message.toLowerCase().includes('premier'))) {
            resultatDiv.className = 'prime';
        } else {
            resultatDiv.className = 'not-prime';
        }

    } catch (erreur) {
        console.error('Erreur lors de l\'appel API:', erreur);
        resultatDiv.innerText = '❌ Erreur : Vérifie que ton API FastAPI est bien lancée !';
        resultatDiv.className = 'not-prime';
    }

    // Réactiver le bouton
    bouton.disabled = false;
}

// Permettre d'appuyer sur Entrée pour valider
document.addEventListener('DOMContentLoaded', function() {
    const input = document.getElementById('monInput');

    input.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            verifierNombre();
        }
    });

    console.log('✅ Page chargée, prêt à tester !');
});