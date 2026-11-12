# Cabinet Medical / Teleconsultation

## Projet et methode

Projet Fil Rouge de fin d'annee, developpe progressivement sprint par sprint, avec une vision Web et Mobile. Realiser uniquement le sprint demande et conserver le travail existant. Avant toute modification, lire les documents existants (analyse du projet, dictionnaire de donnees, dependances fonctionnelles, identifiants, MCD et instructions .github), inspecter le projet et presenter un plan. Travailler par etapes, verifier chaque etape, presenter un rapport et attendre la prochaine instruction. Ne pas inventer de fonctionnalites, champs ou relations ; demander une clarification pour une decision importante ambigue.

## Technologies

- HTML
- JavaScript
- Tailwind CSS
- PHP
- JSON pour le stockage des donnees et les echanges API

Ne pas ajouter Laravel, React, NativePHP, Bootstrap, de bibliotheques ou API externes non demandees. Garder le code simple et organise.

## Donnees JSON

Stocker les donnees dans des fichiers JSON pour quatre entites : Consultation (classe principale), Specialite (classe de classification), Ordonnance et Patient. Ne pas ajouter d'entite sans instruction. Chaque enregistrement possede un identifiant unique.

- Un patient peut avoir plusieurs consultations ; chaque consultation appartient a un patient.
- Une specialite peut concerner plusieurs consultations ; chaque consultation concerne une specialite.
- Une consultation peut donner lieu a plusieurs ordonnances ; chaque ordonnance appartient a une consultation.
- Une ordonnance contient consultation_id, mais pas patient_id : le patient est retrouve par la consultation.
- Une specialite contient un champ image avec le chemin ou le nom du fichier. Les images physiques restent dans assets/images/ et ne sont pas stockees dans JSON.

Les DAO gerent la lecture et l'ecriture des fichiers JSON, les erreurs de lecture et d'ecriture, le JSON invalide et les acces concurrents. Preserver les donnees existantes.

## Documentation des donnees

Garder coherents les fichiers JSON, dictionnaire_donnees.csv, dependances_fonctionnelles.md, identifiants.md, mcd.mmd et le code. Utiliser les noms deja presents dans le projet sans creer de doublons. Le dictionnaire utilise les colonnes Interface, Name, Signification, Type, Obligatoire et Calcule. Documenter les champs approuves, les dependances fonctionnelles, les identifiants et les relations. Ne pas ajouter patient_id a Ordonnance.

## Images et specialites

Si des images de specialites sont utilisees dans le Dashboard, inspecter les fichiers existants et stocker leur chemin dans JSON. Ne pas inventer de fichiers ni utiliser de placeholders.

## Architecture et PHP

Respecter une architecture 3 tiers simple avec POO et DAO :

1. Presentation : pages, HTML, Tailwind CSS, JavaScript, controllers et endpoints API.
2. Business : entites, services, validations, regles et exceptions metier.
3. Data Access : DAO et operations de lecture/ecriture JSON.

Flux : utilisateur -> presentation -> controller -> service -> DAO -> fichiers JSON. Ne pas contourner les couches, placer la logique metier dans les DAO ou acceder directement aux fichiers JSON depuis les pages ou endpoints. Eviter les abstractions inutiles.

Prevoir les classes Patient, Consultation, Specialite et Ordonnance et leurs DAO correspondants. Chaque DAO gere les operations de son entite : findAll, findById, create, update et delete ; les noms peuvent suivre le code existant. Les services appliquent les validations et regles avant d'appeler les DAO.

Utiliser try, catch, throw et Exception lorsque necessaire. Les DAO signalent les erreurs d'acces aux donnees, les services gerent les regles metier et les controllers preparent les reponses. Ne pas exposer les details techniques ou sensibles.

## API JSON

Fournir les ressources /api/patients, /api/consultations, /api/specialites et /api/ordonnances, avec GET (liste et ID), POST, PUT et DELETE. Passer par controllers, services et DAO. Toutes les reponses, y compris les erreurs, utilisent les champs success, message, data et errors. Utiliser les codes HTTP 200, 201, 400, 404, 422 et 500 selon le cas.

## JavaScript et chargement

Initialiser les interactions apres DOMContentLoaded et verifier l'existence des elements avant d'ajouter des listeners. Utiliser fetch pour l'API et preventDefault uniquement lorsque necessaire. Gerer les erreurs reseau, les reponses invalides et success: false avec throw Error et catch ou try/catch. Mettre a jour l'interface sans rechargement complet lorsque pertinent.

Pour toute operation asynchrone concernee, afficher un spinner dans le bouton, desactiver celui-ci et empecher les doubles clics. Afficher le resultat puis masquer le spinner et reactiver le bouton dans finally, meme en cas d'erreur.

## Structure du projet

Inspecter la structure existante avant de creer des dossiers. Organiser le code autour de presentation (controllers, api, pages), business (entities, services), data (dao et fichiers JSON), includes et assets (CSS, JS, images). Conserver les fichiers existants appropries sans doublons.

## Interface

Le projet comporte uniquement un Dashboard de gestion, inspire du projet technique. Ne pas creer de Home publique ni de page Login pour ce sprint.

## Dashboard et CRUD

Afficher une sidebar avec Dashboard, Consultations, Specialites, Ordonnances et Patients. Consultation est la classe principale et Specialite la classe de classification. Chaque section presente les donnees reelles dans un tableau avec les champs approuves. Implementer le CRUD complet pour les quatre entites et dans l'API. Le bouton View charge les details depuis JSON par identifiant ; afficher `Record not found.` si absent et permettre le retour au tableau. Update charge les valeurs existantes. Delete ne supprime que l'enregistrement selectionne ; pas de suppression en masse. Search et Filter utilisent les donnees reelles et affichent un etat de chargement si necessaire.

## Qualite et verification

Valider les donnees cote serveur avant ecriture, proteger les fichiers de donnees, gerer les erreurs sans exposer d'informations sensibles, eviter les doublons et respecter les trois couches. Ne pas inventer de regles medicales ou de validations non definies. Verifier les donnees et relations, la documentation, le CRUD, les reponses et codes API, les erreurs, les spinners, les images et le responsive.

## Rapport et limites

Apres le travail demande, fournir un rapport indiquant ce qui a ete implemente, les fichiers modifies ou crees, les changements JSON, l'architecture, les endpoints, les verifications effectivement realisees et les points a clarifier. Ne pas declarer des tests non executes. Ne pas implementer automatiquement les futurs sprints ou fonctionnalites non demandees ; attendre la prochaine instruction. Laravel et une application mobile appartiennent aux etapes futures sauf instruction explicite.
