---
name: api-json-php
description: Build or modify PHP JSON API endpoints and their service interactions for the medical project.
---

# API JSON PHP

Lire le README et inspecter les endpoints existants. Les endpoints recoivent la requete, decodent le JSON, appellent les services et renvoient du JSON ; ils ne lisent pas directement les fichiers de donnees. Les services valident les donnees et appliquent les regles metier avant d'appeler les DAO.

Pour les operations demandees, prendre en charge les methodes HTTP correspondantes : GET pour lire, POST pour creer, PUT pour modifier et DELETE pour supprimer. Suivre le format de reponse du README avec success, message, data et errors, y compris en cas d'erreur ; utiliser un code HTTP adapte. Gerer les requetes et JSON invalides et ne pas exposer les details techniques. Conserver un code PHP simple, avec try, catch et throw lorsque necessaire. Verifier les reponses et erreurs reellement concernees.