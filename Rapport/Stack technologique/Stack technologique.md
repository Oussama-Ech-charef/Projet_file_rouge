Dans le cadre de ce projet de **Cabinet Médical / Téléconsultation**, plusieurs technologies modernes et complémentaires ont été sélectionnées pour garantir la performance, la sécurité renforcée des données de santé, la maintenabilité et l'ergonomie de l'application.

### Technologies Backend

- **PHP 8.2+ et Laravel 12.0** : Ce duo technologique est utilisé pour développer le backend en architecture MVC, garantissant un environnement sécurisé, robuste et structuré pour la manipulation des dossiers patients et des consultations.
- **Spatie Laravel Permission** : Gestion rigoureuse des rôles et des autorisations médicales (Médecin, Secrétaire médicale, Patient).
- **API RESTful** : Architecture de services pour la communication sécurisée entre les interfaces web et la logique métier de l'application.

### Technologies Frontend

- **Blade Templates** : Moteur de rendu HTML natif de Laravel, utilisé pour structurer les vues sous forme de composants modulaires et réutilisables (fiches patients, tableaux de bord de consultations, générateurs d'ordonnances).
- **Tailwind CSS** : Framework CSS utilitaire permettant de concevoir une interface sur mesure, moderne, responsive et claire pour les praticiens.
- **Alpine.js** : Framework JavaScript léger et réactif, utilisé pour le dynamisme du frontend (recherche rapide de patients, modales de consultation, filtres par spécialité médicale).
- **Vite** : Outil de build moderne optimisant la compilation des ressources CSS et JavaScript pour des temps de chargement minimes.

### Base de données

- **MySQL** : Système de gestion de base de données relationnelle (SGBDR) fiable, utilisé pour stocker l'ensemble des données médicales (patients, spécialités, consultations, ordonnances).

### Outils de modélisation et de conception

- **Mermaid & PlantUML** : Outils de génération textuelle de diagrammes utilisés pour modéliser le domaine médical (diagrammes de classes, flux de consultation, architecture logicielle).
