// Fonction principale pour vérifier si un nombre est premier
async function verifierNombre() {
    // Récupérer les éléments du DOM
    const nombre = document.getElementById('monInput').value;
    const resultatDiv = document.getElementById('resultat');
    const bouton = document.getElementById('boutonVerifier');
    const useAI = document.getElementById('useAI').checked;
    const modeUtilise = document.getElementById('modeUtilise');

    // Vérifier qu'un nombre est bien entré
    if (!nombre) {
        alert('Entre un nombre d\'abord !');
        return;
    }

    // Afficher un message de chargement adapté au mode
    if (useAI) {
        resultatDiv.innerText = '🤖 L\'IA réfléchit...';
    } else {
        resultatDiv.innerText = '💻 L\'ordinateur calcule...';
    }
    resultatDiv.className = 'loading';
    bouton.disabled = true;

    // Choisir le bon endpoint selon le toggle
    const endpoint = useAI ? 'ai_premier' : 'ordi_premier2';

    try {
        console.log(`Appel de l'API : /${endpoint}/${nombre}`);
        const reponse = await fetch(`http://localhost:8000/${endpoint}/${nombre}`);
        const data = await reponse.json();

        console.log('Réponse de l\'API :', data);

        // Afficher le résultat
        resultatDiv.innerText = data.nombre;

        // Ajouter une classe selon le résultat
        // On cherche le mot "premier" dans la réponse pour déterminer la couleur
        const reponseTexte = String(data.nombre).toLowerCase();
        if (reponseTexte.includes('est premier') || reponseTexte.includes('est un nombre premier') || data.nombre === true) {
            resultatDiv.className = 'prime';
        } else {
            resultatDiv.className = 'not-prime';
        }

        // Afficher quel mode a été utilisé
        modeUtilise.innerText = useAI
            ? '⚡ Réponse générée par OpenAI'
            : '⚡ Réponse calculée par l\'algorithme';

    } catch (erreur) {
        console.error('Erreur lors de l\'appel API:', erreur);
        resultatDiv.innerText = '❌ Erreur : Vérifie que ton API FastAPI est bien lancée !';
        resultatDiv.className = 'not-prime';
        modeUtilise.innerText = '';
    }

    // Réactiver le bouton
    bouton.disabled = false;
}

// Mettre à jour le texte du toggle quand on clique
document.addEventListener('DOMContentLoaded', function() {
    const input = document.getElementById('monInput');
    const toggleCheckbox = document.getElementById('useAI');
    const toggleText = document.getElementById('toggleText');

    // Permettre d'appuyer sur Entrée pour valider
    input.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            verifierNombre();
        }
    });

    // Mettre à jour le texte quand on change le toggle
    toggleCheckbox.addEventListener('change', function() {
        if (this.checked) {
            toggleText.innerText = '🤖 Mode IA (OpenAI)';
        } else {
            toggleText.innerText = '💻 Mode Algorithme';
        }
    });

    console.log('✅ Page chargée, prêt à tester !');
});