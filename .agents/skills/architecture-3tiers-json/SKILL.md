---
name: architecture-3tiers-json
description: Organize the medical project in three tiers using simple PHP classes, services, DAO and JSON storage.
---

# Architecture 3 tiers

Lire le README et inspecter le code existant avant de modifier le projet. Respecter les fichiers et noms existants sans creer de doublons. Utiliser HTML, JavaScript, Tailwind CSS, PHP et JSON.

Organiser les responsabilites simplement :
- Presentation : pages, JavaScript, API et controllers recoivent les requetes et produisent les reponses.
- Business : classes d'entites et services ; les services valident les donnees et appliquent les regles approuvees.
- Data access : DAO qui gerent la lecture et l'ecriture des fichiers JSON.

Flux : interface → fetch → API/controller → service → DAO → fichiers JSON. L'endpoint decode la requete et transmet les donnees au service. Ne pas acceder aux fichiers depuis la presentation ni placer les regles metier dans les DAO. Un controller distinct est utile seulement s'il clarifie le code. Garder les classes simples : proprietes privees typees, constructeur et getters utiles ; eviter les abstractions vides.

Une organisation possible est `frontend/` et `backend/` avec `api/`, `class/`, `services/`, `dao/` et `data/`. Adapter cette structure a l'existant. Implementer uniquement le sprint demande et verifier le flux entre couches.