# Project instructions

- Before changing the medical project, read `Projet_fil_rouge_sprint_3/README.md` and inspect the existing files relevant to the task. Read the project's data documentation and `.github` instructions when present and relevant.
- Work only on the requested sprint and task. Preserve working functionality, existing decisions and approved data fields and relationships. Do not invent features or create duplicate files.
- Use HTML, JavaScript, Tailwind CSS, PHP and JSON for the current project. Store data in JSON files; do not introduce MySQL, PDO or frameworks unless explicitly requested.
- Keep the three tiers distinct: presentation, business services and data access through DAO. Follow the applicable skills in `.agents/skills` for architecture, DAO, API and interface work.
- The approved entities are Patient, Consultation, Specialite and Ordonnance. An ordonnance references a consultation and does not directly contain `patient_id`.
- Before implementation, briefly present the intended changes and affected files. Work step by step and stop after the requested step; ask for clarification when an important decision cannot be inferred.
- Validate data on the server, handle errors without exposing sensitive details, and preserve existing JSON data. Do not invent medical rules.
- Verify changes appropriate to the task and report what changed, files affected, checks actually performed and any outstanding issues. Do not claim tests were run when they were not.
