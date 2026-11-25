# Mode d'emploi du portfolio

Tout se fait depuis le site **github.com**, sur n'importe quel ordinateur, sans rien
installer. À chaque modification enregistrée, le site se reconstruit et se met en
ligne tout seul en une à deux minutes.

**Sommaire**

1. [Mettre le site en ligne (une seule fois)](#1-mettre-le-site-en-ligne-une-seule-fois)
2. [Modifier un texte](#2-modifier-un-texte)
3. [Ajouter une réalisation](#3-ajouter-une-réalisation)
4. [Ajouter des images et des documents](#4-ajouter-des-images-et-des-documents)
5. [Mettre à jour la veille](#5-mettre-à-jour-la-veille)
6. [Mettre à jour le CV](#6-mettre-à-jour-le-cv)
7. [Le tableau de synthèse E5](#7-le-tableau-de-synthèse-e5)
8. [Si quelque chose ne marche plus](#8-si-quelque-chose-ne-marche-plus)
9. [Aller plus loin](#9-aller-plus-loin)

---

## 1. Mettre le site en ligne (une seule fois)

1. Crée un compte sur <https://github.com> (choisis un pseudo sérieux : il apparaît dans l'adresse du site).
2. En haut à droite : **+** > **New repository**.
   - *Repository name* : `portfolio`
   - Coche **Public** (obligatoire pour l'hébergement gratuit).
   - Ne coche rien d'autre, puis **Create repository**.
3. Sur la page qui s'affiche, clique sur le lien **uploading an existing file**.
4. Décompresse le fichier `portfolio.zip` sur ton ordinateur, ouvre le dossier obtenu,
   sélectionne **tout son contenu** (Ctrl + A) et fais-le glisser dans la page GitHub.
   Clique sur **Commit changes**.

   > **Attention au dossier `.github`.** Sous Windows, il est parfois masqué
   > (Explorateur > Affichage > Afficher > Éléments masqués). S'il manque après l'envoi,
   > le site ne se publiera pas : vérifie qu'il apparaît bien dans la liste des fichiers sur GitHub.

   > **N'envoie jamais le dossier `objectif`** (la version fictive qui te sert de cible). Le dépôt
   > est public : range ce dossier ailleurs sur ton ordinateur. S'il arrive quand même sur GitHub,
   > la publication se bloque et te demande de le supprimer.

5. Onglet **Settings** > **Pages** (menu de gauche) > *Source* : choisis **GitHub Actions**.
6. Onglet **Actions** : clique sur **Publier le site** puis **Run workflow** > **Run workflow**.
   Au bout d'une à deux minutes, une coche verte apparaît.
7. Ton site est à l'adresse `https://TON-PSEUDO.github.io/portfolio/`.
8. Ouvre le fichier `contenu/site.yml` (voir le point 2) et écris cette adresse après
   `url_portfolio:`. Elle sera reprise dans le tableau de synthèse et sur le CV.

> **Ne change plus cette adresse ensuite** : c'est celle que le jury aura dans ton tableau de synthèse.

---

## 2. Modifier un texte

1. Sur GitHub, ouvre le fichier à modifier (tableau ci-dessous).
2. Clique sur le **crayon** en haut à droite du fichier.
3. Modifie le texte.
4. Clique sur **Commit changes…** (bouton vert), puis encore **Commit changes**.
5. Attends une à deux minutes et recharge ton site.

| Je veux changer… | Fichier |
|---|---|
| Mon nom, mon courriel, mes liens GitHub et LinkedIn, l'adresse du site | `contenu/site.yml` |
| Le texte de la page d'accueil | `contenu/pages/accueil.md` |
| La présentation du BTS SIO | `contenu/pages/bts-sio.md` |
| Le texte de la page Parcours | `contenu/pages/parcours.md` |
| Le texte de la page Contact | `contenu/pages/contact.md` |
| Mon CV (et les dates du parcours) | `contenu/cv.yml` |
| Une réalisation | `realisations/nom-du-dossier/projet.md` |
| Une veille | `veille/nom-du-fichier.md` |

### Trois règles pour ne rien casser

- Dans les fichiers `.yml` et dans l'en-tête des fichiers `.md` (la partie entre les deux
  lignes `---`), **ne touche pas à ce qui est avant les deux-points**, seulement au texte après.
- Si ton texte contient lui-même deux-points, mets-le **entre guillemets** :
  `titre: "Stage : création d'un site"`.
- Respecte les espaces en début de ligne (les listes commencent par deux espaces et un tiret).

### Les emplacements [À COMPLÉTER : …]

Quand une information manque, le texte contient un emplacement entre crochets, par exemple
`[À COMPLÉTER : dates exactes du stage]`. Il est **surligné en jaune sur le site** et rappelé
dans le résumé de chaque publication (onglet Actions). Remplace tout l'emplacement, crochets
compris, par la vraie information. N'écris que ce qui est vrai et que tu sauras expliquer à
l'oral ; si un passage ne te concerne pas, supprime-le.

### Mémo Markdown (pour le texte sous l'en-tête)

```markdown
## Un titre de partie
Un paragraphe. **Du gras**, *de l'italique*, [un lien](https://exemple.fr).

- une liste
- à puces

1. une liste
2. numérotée

| Colonne 1 | Colonne 2 |
|---|---|
| un tableau | simple |
```

---

## 3. Ajouter une réalisation

### Étape 1 : créer le dossier (30 secondes)

1. Onglet **Actions** > dans la liste de gauche, **Créer une réalisation**.
2. À droite, **Run workflow** : écris le **titre**, choisis la **période**
   (`formation`, `stage-1` ou `stage-2`), puis **Run workflow**.
3. Une minute plus tard, un nouveau dossier existe dans `realisations/`,
   par exemple `realisations/application-de-gestion-de-tickets/`.

> *Autre méthode* : appuie sur la touche **.** (point) quand tu es sur la page du dépôt.
> Un éditeur s'ouvre dans le navigateur : clic droit sur `realisations/_modele` > *Copy*,
> clic droit sur `realisations` > *Paste*, puis renomme le dossier (minuscules, tirets, pas d'accents).

### Étape 2 : remplir le fichier `projet.md`

Ouvre `realisations/ton-dossier/projet.md` et clique sur le crayon. L'en-tête ressemble à ceci :

```yaml
---
titre: "Application de gestion de tickets"
resume: "Application web permettant aux salariés de signaler un incident et au technicien de le suivre."
organisation: "Adour Expertise (contexte fictif)"
periode: formation
date_debut: 2026-12-01
date_fin: 2027-01-20
technologies: [PHP, MySQL, HTML, CSS, Git]
competences:
  - incidents
  - mise-a-disposition
  - mode-projet
liens:
  - texte: Code source sur GitHub
    url: https://github.com/ton-pseudo/tickets
e6: true
brouillon: true
---
```

Les **compétences** s'écrivent exactement ainsi (liste fixe) :

| À écrire | Compétence du bloc 1 |
|---|---|
| `patrimoine` | Gérer le patrimoine informatique |
| `incidents` | Répondre aux incidents et aux demandes d'assistance et d'évolution |
| `presence-en-ligne` | Développer la présence en ligne de l'organisation |
| `mode-projet` | Travailler en mode projet |
| `mise-a-disposition` | Mettre à disposition des utilisateurs un service informatique |
| `developpement-pro` | Organiser son développement professionnel |

Sous l'en-tête, remplis les parties déjà prévues : Contexte, Besoin, Objectifs, Étapes,
Difficultés et solutions, Résultat, Compétences mobilisées, Bilan.

### Étape 3 : publier

Tant que la ligne `brouillon: true` est présente, la réalisation **n'apparaît pas** sur le
site : tu peux la rédiger en plusieurs fois. Quand elle est prête, écris `brouillon: false`
et enregistre. Elle apparaît alors automatiquement :

- dans la liste des réalisations (avec les filtres),
- sur sa propre page, avec sa galerie et ses documents,
- dans le tableau des compétences du site,
- dans le tableau de synthèse `.xlsx`,
- dans le bloc « compétences travaillées » de l'accueil.

---

## 4. Ajouter des images et des documents

1. Ouvre le dossier `realisations/ton-dossier/images/` (ou `documents/`).
2. **Add file** > **Upload files**, fais glisser tes fichiers, puis **Commit changes**.

**Images (captures d'écran)**

- Formats : PNG ou JPG. Elles sont **redimensionnées et allégées automatiquement**, inutile de les retoucher.
- Elles s'affichent par ordre alphabétique : nomme-les `01-…`, `02-…`, `03-…`.
- Le nom du fichier devient la légende : `02-page-de-connexion.png` donne « Page de connexion ».
- Pour une légende plus précise, ajoute dans l'en-tête de `projet.md` :

  ```yaml
  legendes:
    02-page-de-connexion.png: "Page de connexion, avec le message d'erreur en cas de mot de passe incorrect"
  ```

- La première image sert de vignette dans la liste.

**Documents** (PDF, schémas, documentation…) : ils sont listés automatiquement en bas de
la page, avec leur type et leur taille. Donne-leur un nom clair, par exemple
`Cahier-des-charges.pdf`.

> **Le site est public.** Avant de déposer une capture ou un document : pas de mot de passe,
> pas de données personnelles, pas de document confidentiel de l'entreprise. En cas de doute,
> demande à ton maître de stage.

---

## 5. Mettre à jour la veille

Une veille = un fichier dans `veille/`.

**Compléter une veille existante** (le plus fréquent) : ouvre le fichier, par exemple
`veille/gravure-2-nanometres.md`, et ajoute une source en haut de la liste `sources:` :

```yaml
sources:
  - titre: "Titre de l'article"
    editeur: "Nom du site"
    date: 2027-01-12
    url: https://exemple.fr/article
    note: "Ce que j'en retiens, en une phrase."
```

Change aussi la ligne `date:` (date de mise à jour) et, si besoin, le texte de la partie
« L'actualité ». Le rythme conseillé et le modèle de fiche complet (avec la ligne `impact:`)
sont dans `docs/VEILLE-METHODE.md`.

**Créer une nouvelle veille** : dans `veille/`, **Add file** > **Create new file**, nomme-le
`mon-sujet.md`, colle le contenu de `veille/_modele.md`, remplis-le, puis passe
`brouillon: false`.

**Joindre un document** (diaporama en PDF…) : dépose-le dans `veille/documents/`, puis écris
son nom exact dans l'en-tête :

```yaml
documents:
  - Mon-diaporama.pdf
```

---

## 6. Mettre à jour le CV

Modifie `contenu/cv.yml`. La page « CV » du site **et** le PDF téléchargeable sont refaits
automatiquement à partir de ce fichier.

Pour ajouter une expérience, copie un bloc existant et change le texte :

```yaml
experiences:
  - dates: "2027"
    poste: Stagiaire développeur web
    lieu: Nom de l'entreprise, Ville (Pays)
    precision: Stage de 2e année de BTS SIO, programme Erasmus+
    missions:
      - Première mission
      - Deuxième mission
```

Si tu préfères ton propre CV mis en page ailleurs, dépose-le sous le nom exact
`contenu/cv.pdf` : c'est lui qui sera proposé au téléchargement.

Ton numéro de téléphone et ton adresse ne figurent volontairement pas sur le site.

---

## 7. Le tableau de synthèse E5

- Sur le site, la page **Compétences** affiche le tableau croisé, toujours à jour.
- Le bouton **Télécharger le tableau (.xlsx)** donne le même tableau au format Excel,
  fabriqué à partir des mêmes données : le site et le tableau ne peuvent pas se contredire.

> **Important.** Ce fichier reprend la structure du tableau de synthèse, mais ce n'est pas
> le fichier officiel. Pour le dépôt du dossier :
> 1. récupère auprès de tes professeurs le **modèle .xlsx de la circulaire de ta session** ;
> 2. ouvre les deux fichiers côte à côte et recopie les intitulés, les dates et les croix ;
> 3. vérifie que l'adresse du portfolio est la bonne.
>
> Quand tu auras le modèle officiel, envoie-le à Claude : le programme pourra être adapté
> pour remplir directement ce fichier.

---

## 8. Si quelque chose ne marche plus

**Le site ne change pas après une modification**

1. Attends deux minutes et recharge la page avec **Ctrl + F5**.
2. Ouvre l'onglet **Actions** du dépôt.
   - Rond orange : la publication est en cours.
   - **Coche verte** : c'est publié.
   - **Croix rouge** : une erreur a bloqué la publication. Pas de panique : **l'ancienne version du site reste en ligne**.
3. Clique sur la ligne à croix rouge. Le résumé explique le problème en français, par exemple :

   ```
   ❌ Le site n'a PAS été mis à jour
   - realisations/tickets/projet.md : « mode projet » n'existe pas dans « competences ».
     Voulais-tu écrire « mode-projet » ? Valeurs possibles : patrimoine, incidents, …
   ```

4. Corrige le fichier indiqué et enregistre : la publication repart toute seule.

**Les messages les plus courants**

| Message | Cause | Correction |
|---|---|---|
| « … n'existe pas dans competences » | Compétence mal écrite | Recopie-la depuis le tableau du point 3 |
| « l'en-tête est mal écrit (vers la ligne N) » | Deux-points dans un texte, guillemet oublié, espaces décalés | Mets le texte entre guillemets, réaligne les lignes |
| « … n'est pas une date valide » | Date écrite en toutes lettres | Écris `2026-06-16` ou `2026-06` |
| « le document … est introuvable » | Nom différent entre l'en-tête et le fichier déposé | Copie-colle le nom exact du fichier |
| « est en brouillon » | Normal | Passe `brouillon: false` pour publier |

**Revenir en arrière**

Ouvre le fichier concerné > **History** (en haut à droite) > clique sur une ancienne version
pour revoir son contenu, copie-le et recolle-le dans le fichier actuel. Rien n'est jamais perdu.

**Une image ne s'affiche pas** : vérifie qu'elle est bien dans le dossier `images/` de la
réalisation et que c'est un fichier PNG ou JPG.

**Toujours bloqué ?** Copie le message d'erreur et envoie-le à Claude avec le contenu du fichier concerné.

---

## 9. Aller plus loin

### Travailler sur ton ordinateur (facultatif)

Utile pour prévisualiser avant de publier. Il faut Python et Git :

```
git clone https://github.com/TON-PSEUDO/portfolio.git
cd portfolio
pip install -r outils/requirements.txt
python outils/construire.py
python -m http.server 8000 --directory _site
```

Puis ouvre <http://localhost:8000>. Pour publier : `git add .`, `git commit -m "message"`, `git push`.

### Changer l'apparence

Les couleurs sont regroupées au début de `outils/style/site.css` (bloc `:root`).
Les gabarits des pages sont dans `outils/gabarits/`.

### La version « objectif »

Le dossier `objectif` (fourni à part) contient une version fictive du portfolio, qui sert de
modèle et de cible. Elle n'est jamais publiée : son mode d'emploi et la méthode pour faire
passer un élément réalisé vers le vrai portfolio sont dans `objectif/LISEZ-MOI.md`, la liste
des actions dans `objectif/ECART.md`.

### Une interface d'édition visuelle (CMS) : utile ou pas ?

Il existe des interfaces gratuites, comme **Sveltia CMS** ou **Decap CMS**, qui ajoutent au
site une page d'administration avec des formulaires.

| Avantages | Inconvénients |
|---|---|
| Formulaires à remplir au lieu de fichiers texte | Une configuration de plus à maintenir, qui peut tomber en panne |
| Envoi des images par glisser-déposer | Connexion à GitHub à paramétrer (jeton d'accès personnel ou service tiers) |
| Aperçu pendant la saisie | Moins formateur : à l'oral, savoir expliquer Git et Markdown est un atout pour un étudiant SLAM |

**Conseil** : commence sans. L'éditeur de github.com suffit pour ce portfolio, et moins il y
a de pièces, moins il y a de pannes. Si la saisie te pèse au bout de quelques semaines,
Sveltia CMS pourra être ajouté sans rien changer au contenu existant.
