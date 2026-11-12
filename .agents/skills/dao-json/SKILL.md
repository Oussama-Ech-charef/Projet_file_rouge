---
name: dao-json
description: Implement PHP DAO classes and CRUD operations backed by JSON files in the medical project.
---

# DAO et fichiers JSON

Lire le README et la structure existante. Creer ou adapter un DAO par entite pour les operations demandees : liste, recherche par ID, creation, modification et suppression. Les DAO lisent et ecrivent les fichiers JSON ; les services valident les donnees et appliquent les regles metier. Utiliser des classes d'entites simples avec proprietes privees, constructeur et getters utiles lorsque pertinent.

Preserver les donnees existantes, gerer les erreurs de lecture, d'ecriture et de JSON invalide, et proteger les ecritures concurrentes. Garantir des identifiants uniques meme apres suppression : ne pas utiliser le nombre d'enregistrements comme prochain identifiant. Signaler les erreurs sans exposer de details techniques.

Respecter les champs et relations approuves : Patient, Consultation, Specialite et Ordonnance. Une ordonnance reference une consultation, sans patient_id direct. Les images restent des fichiers ; JSON stocke leur chemin. Ne pas inventer de champs ni de regles medicales. Verifier les operations modifiees et les cas d'erreur pertinents.