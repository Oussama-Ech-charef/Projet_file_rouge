# Prototype (fonctionnalités, classes)

Avant d'entamer le développement complet du projet principal, j'ai réalisé un projet technique servant de prototype fonctionnel (Proof of Concept) : une application web de **Cabinet Médical / Téléconsultation**. Ce prototype permet aux praticiens de gérer les consultations médicales, les dossiers des patients, les ordonnances et la classification par spécialité médicale.

La plateforme permet à un cabinet médical de centraliser la prise en charge des patients, d'assurer le suivi des consultations (en présentiel ou à distance) et de délivrer des ordonnances médicales de façon structurée.

## Fonctionnalités Clés

- **Gestion des Patients (Patient Management) :** Création, consultation, mise à jour et suivi des dossiers patients (nom, prénom, coordonnées, antécédents) avec opérations CRUD complètes.
- **Gestion des Consultations (Consultation Management - Classe principale) :** Planifier, enregistrer, modifier et suivre les consultations médicales (motif, date/heure, type : présentiel ou téléconsultation, diagnostic, statut).
- **Gestion des Spécialités (Spécialité Management - Classe de classification) :** Créer, modifier et organiser les spécialités médicales (ex : Médecine générale, Cardiologie, Dermatologie, Pédiatrie) pour catégoriser les actes et consultations.
- **Gestion des Ordonnances (Ordonnance Management) :** Générer, modifier et associer des ordonnances médicales (médicaments, posologie, durée de traitement) directement rattachées aux consultations.

## Classes principales du modèle

- **Consultation (Classe principale) :** Représente l'acte médical ou la séance de téléconsultation liant le patient, le médecin, le diagnostic et les prescriptions.
- **Spécialité (Classe de classification) :** Permet de classer et catégoriser les consultations selon le domaine médical concerné.
- **Patient :** Représente le patient bénéficiaire des soins et consultations médicales.
- **Ordonnance :** Représente la prescription médicale détaillée délivrée à l'issue d'une consultation.

## Relations principales

- **Patient ↔ Consultation :** Relation **One-to-Many (1:N)** — Un patient peut effectuer plusieurs consultations au fil du temps, mais chaque consultation est attribuée à un seul patient.
- **Spécialité ↔ Consultation :** Relation **One-to-Many (1:N)** — Une spécialité médicale regroupe plusieurs consultations, et chaque consultation est rattachée à une spécialité précise.
- **Consultation ↔ Ordonnance :** Relation **One-to-One (1:1)** (ou **One-to-Many (1:N)**) — Une consultation médicale donne lieu à l'émission d'une ordonnance contenant les prescriptions adaptées au diagnostic.
