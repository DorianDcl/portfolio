# Portfolio BTS SIO SLAM – Dorian Da Col

Site statique du portfolio (épreuve E5), publié avec GitHub Pages.

- **Pour modifier le contenu : lis [MODE-D-EMPLOI.md](MODE-D-EMPLOI.md).**
- Ce qui reste à faire : [docs/CHECKLIST.md](docs/CHECKLIST.md)
- Méthode de veille : [docs/VEILLE-METHODE.md](docs/VEILLE-METHODE.md)
- Plan de réalisations et planning : [docs/PLAN-REALISATIONS.md](docs/PLAN-REALISATIONS.md)
- Questions à poser aux professeurs : [docs/QUESTIONS-AUX-PROFS.md](docs/QUESTIONS-AUX-PROFS.md)
- Message type pour rédiger une réalisation avec Claude : [docs/MODELE-MESSAGE-CLAUDE.md](docs/MODELE-MESSAGE-CLAUDE.md)

## Où se trouve quoi

| Dossier | Contenu | À modifier ? |
|---|---|---|
| `realisations/` | Un dossier par réalisation (`projet.md`, `images/`, `documents/`) | Oui, souvent |
| `veille/` | Un fichier par synthèse de veille | Oui |
| `contenu/` | CV, textes des pages, informations générales | Oui |
| `outils/` | Le programme qui fabrique le site, les gabarits et le style | Non (sauf pour changer l'apparence) |
| `.github/` | L'automatisation de la mise en ligne | Non |

Le site publié est fabriqué par `outils/construire.py` à chaque modification
(GitHub Actions). Il n'y a rien à installer pour s'en servir.
