## 2.3 2TUP

### Définition

La méthode **2TUP** (*Two Tracks Unified Process*) est une méthode de développement logiciel agile et itérative. Elle est parfaitement adaptée au contexte de notre projet de **Cabinet Médical / Téléconsultation**, à ses exigences de confidentialité des données de santé et aux besoins des **praticiens et patients**.

Sa particularité repose sur une architecture en « Y » qui sépare distinctement deux axes de réflexion :

- **la branche fonctionnelle**, consacrée à la compréhension des utilisateurs, des processus médicaux et des besoins métier (prise en charge du patient, consultations, téléconsultation, prescription d'ordonnances) ;
- **la branche technique**, consacrée à l'étude des contraintes techniques, à la sécurité des données médicales, à la conception de l'architecture et au choix des technologies.

La branche fonctionnelle permet de définir les **fonctionnalités clés telles que la gestion des consultations médicales, le suivi des patients, la délivrance des ordonnances et la classification par spécialité**, tandis que la branche technique permet de déterminer l'architecture et les outils nécessaires, tels que **PHP / Laravel, MySQL, Tailwind CSS et l'architecture MVC**.

Ces deux branches progressent en parallèle, puis se rejoignent dans une phase de réalisation. Cette organisation permet de limiter les risques, de vérifier la cohérence entre les besoins métier et la solution technique, et de faire évoluer progressivement le produit.

### Schéma

Le schéma suivant présente le fonctionnement général de la méthode 2TUP appliquée à notre application de cabinet médical et téléconsultation.

![schema](images.jpg)

**Figure 2 : Processus 2TUP appliqué au projet Cabinet Médical / Téléconsultation**

La branche fonctionnelle part de la capture des besoins et aboutit à l'analyse fonctionnelle. En parallèle, la branche technique part des besoins techniques et aboutit à la définition de l'architecture et des technologies. La convergence des deux branches déclenche la phase de réalisation, qui comprend la conception, le codage, les tests, la recette et le déploiement.

### Conclusion

La méthode 2TUP fournit un cadre de travail structuré et adaptable pour la réalisation du projet **Cabinet Médical / Téléconsultation**. La séparation entre les branches fonctionnelle et technique facilite la compréhension des flux médicaux et permet de prendre les décisions techniques au moment opportun.

En réunissant ces deux branches dans une phase de réalisation progressive, la méthode favorise la maîtrise des risques liés à la sécurité des données de santé, l'amélioration continue et l'alignement du produit final sur les besoins des **professionnels de santé et des patients**.
