# Plan de réalisations professionnelles

Objectif : au moment du dépôt du dossier, les réalisations couvrent **ensemble les six
compétences du bloc 1** (E5), et **deux d'entre elles** sont de vrais supports pour l'E6 SLAM.

**Ce plan est une liste de propositions.** Les projets 4 à 8 ne sont pas faits : ils
n'apparaissent nulle part sur le site et ne doivent y figurer qu'une fois réalisés, avec
leurs preuves. Les contextes d'entreprise des projets 4 à 6 sont fictifs et devront être
présentés comme tels.

État au 15 novembre 2026 : seules les deux réalisations du stage de 1re année sont
rédigées (avec des emplacements à compléter) ; la fiche du portfolio est en brouillon.
Trois compétences ne sont couvertes par aucune réalisation : **Gérer le patrimoine
informatique**, **Répondre aux incidents et aux demandes d'assistance et d'évolution** et
**Mettre à disposition des utilisateurs un service informatique**.

> Les technologies indiquées sont des propositions. Si tes professeurs imposent un langage
> ou un contexte (souvent un « atelier de professionnalisation » commun à la classe),
> garde le sujet et adapte la technologie.

## Vue d'ensemble

| N° | Réalisation | Cadre | Durée | E6 | État |
|---|---|---|---|---|---|
| 1 | Portfolio professionnel en ligne | Formation | en continu | | Fiche en brouillon, à compléter après la mise en ligne |
| 2 | Site web d'InBelli Consulting sur Odoo | Stage 1 | fait | | Rédigée, emplacements à compléter |
| 3 | Vidéo de lancement « Hook Total » | Stage 1 | fait | | Rédigée, résultat et captures CapCut à compléter |
| 4 | Application web de gestion des demandes d'assistance | Formation | 6 semaines | **Oui** | À faire |
| 5 | Inventaire du parc informatique : application Java et API | Formation | 6 semaines | **Oui** | À faire |
| 6 | Mise en service de GLPI sur Debian avec sauvegardes | Formation | 2 à 3 semaines | | À faire |
| 7 | Outil de collecte automatique pour ma veille | Formation | 1 à 2 semaines | | À faire |
| 8 | Réalisation du stage de 2e année (Erasmus+) | Stage 2 | durée du stage | possible | À définir |

## Tableau de couverture des compétences

« X » : compétence prouvée par tes notes actuelles. « prévu » : compétence visée, à ne cocher
qu'une fois le travail fait.

| Réalisation | Patrimoine | Incidents | Présence en ligne | Mode projet | Mise à disposition | Développement pro |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| 1. Portfolio | | | | | prévu | X |
| 2. Site Odoo (stage 1) | | | X | | | |
| 3. Vidéo de lancement (stage 1) | | | X | X | | X |
| 4. Gestion des demandes d'assistance | prévu | prévu | | prévu | prévu | |
| 5. Inventaire du parc | prévu | | | prévu | prévu | |
| 6. GLPI et sauvegardes | prévu | prévu | | | prévu | |
| 7. Outil de veille | | | | prévu | | prévu |
| 8. Stage 2 | selon les missions | | | prévu | | prévu |
| **Total si tout est réalisé** | **3** | **2** | **2** | **5 à 6** | **4** | **3 à 4** |

Si tout est réalisé, chaque compétence est couverte au moins deux fois : si un projet
prend du retard, le tableau reste complet.

---

## 4. Application web de gestion des demandes d'assistance (support E6 n° 1)

**Contexte fictif.** *Adour Expertise* est un cabinet d'expertise comptable de Tarbes :
22 salariés, 25 postes, un prestataire informatique qui passe une demi-journée par semaine.
Les pannes sont signalées par courriel ou oralement : des demandes se perdent et personne
ne sait où elles en sont.

**Objectifs**

- Un salarié se connecte, déclare une demande (incident ou demande d'évolution), y joint une capture et suit son avancement.
- Le technicien voit toutes les demandes, les trie par priorité, change leur état et répond.
- L'administrateur gère les comptes et les catégories.

**Technologies.** PHP 8 et MySQL ou MariaDB (accès par PDO et requêtes préparées), HTML et CSS,
Git et GitHub. Sécurité : mots de passe hachés (`password_hash`), trois rôles, protection des
formulaires (jeton CSRF), échappement des affichages.

**Compétences du bloc 1.** Incidents (collecter, suivre et orienter des demandes) ; patrimoine
(niveaux d'habilitation par rôle) ; mode projet (planning, suivi des écarts) ; mise à
disposition (recette, déploiement, guide utilisateur).

**Intérêt pour l'E6.** Base de données conçue par toi (MCD puis script SQL), authentification,
architecture en couches, jeu de tests. Prévois une liste d'évolutions possibles : le jury peut
demander de faire évoluer l'application.

**Durée estimée.** 6 semaines à raison de 4 à 5 heures par semaine.

**Preuves à garder au fur et à mesure**

- le cahier des charges d'une page et les maquettes des écrans ;
- le MCD et le script de création de la base ;
- le dépôt GitHub avec des commits réguliers et des messages clairs ;
- le planning prévu et le planning réel (pour analyser les écarts) ;
- le cahier de recette : une liste de tests avec le résultat attendu et le résultat obtenu ;
- des captures de chaque écran, y compris un message d'erreur et un accès refusé ;
- le guide utilisateur en PDF (deux pages).

## 5. Inventaire du parc informatique : application Java et API (support E6 n° 2)

**Contexte fictif.** *Bigorre Logistique*, entreprise de transport de 40 salariés à Ibos,
tient l'inventaire de ses 60 équipements (postes, écrans, imprimantes, téléphones) dans un
tableur que plus personne n'ose modifier. Le responsable veut savoir qui détient quoi et
quels matériels arrivent en fin de garantie.

**Objectifs**

- Application de bureau en Java pour ajouter, modifier, rechercher et affecter un équipement.
- Alerte sur les garanties qui se terminent dans les trois mois.
- Petite API en lecture (liste des équipements au format JSON) pour qu'un autre outil puisse consulter l'inventaire.
- Export de l'inventaire au format CSV.

**Technologies.** Java (interface JavaFX ou Swing), base MySQL ou MariaDB par JDBC, classes
métier et classes d'accès aux données séparées, tests unitaires avec JUnit, Git. Pour l'API :
PHP, ou Java avec Spring Boot si tu l'as vu en cours.

**Compétences du bloc 1.** Patrimoine (recenser et identifier les ressources numériques) ;
mode projet ; mise à disposition (tests, installation sur un poste, accompagnement).

**Intérêt pour l'E6.** Un deuxième type d'application (client lourd, programmation objet),
différent de la première : les deux réalisations se complètent.

**Durée estimée.** 6 semaines.

**Preuves à garder.** Diagramme de classes, script SQL, rapports de tests JUnit (capture),
captures des écrans, exemple de réponse de l'API, fichier CSV exporté, notice d'installation,
dépôt GitHub.

## 6. Mise en service de GLPI sur Debian avec sauvegardes

**Contexte fictif.** Le même cabinet *Adour Expertise* souhaite comparer ton application
(projet 4) avec un outil du marché avant de choisir.

**Objectifs**

- Installer GLPI sur une machine virtuelle Debian (Apache, PHP, MariaDB).
- Créer les profils et les habilitations, saisir une dizaine d'équipements, traiter cinq tickets types du début à la fin.
- Écrire un script de sauvegarde de la base lancé chaque nuit (cron) et **tester une restauration**.
- Rédiger un comparatif d'une page : GLPI ou application sur mesure.

**Technologies.** Debian, VirtualBox, GLPI, MariaDB, script Bash, cron.

**Compétences du bloc 1.** Patrimoine (inventaire, habilitations, sauvegardes, continuité de
service) ; incidents (traitement de demandes) ; mise à disposition (déploiement d'un service).

**Durée estimée.** 2 à 3 semaines. C'est le projet le plus rapide pour couvrir les deux
compétences qui te manquent : à faire en premier si le temps presse.

**Preuves à garder.** Procédure d'installation rédigée par toi, captures (inventaire, ticket
traité, profils), script de sauvegarde, preuve de la restauration, comparatif.

## 7. Outil de collecte automatique pour ma veille

**Contexte.** Projet personnel : aujourd'hui, tu recopies à la main les articles repérés
avec Feedly et Google Alerts.

**Objectifs**

- Un script Python lit quelques flux RSS, garde les articles contenant tes mots-clés et produit une liste datée (titre, source, lien).
- Tu choisis les articles à retenir et tu les ajoutes à ta page de veille avec une phrase de commentaire.
- En option : lancement automatique chaque semaine avec GitHub Actions.

**Technologies.** Python, bibliothèque `feedparser`, Git, GitHub Actions.

**Compétences du bloc 1.** Développement professionnel (outils et stratégie de veille,
environnement d'apprentissage) ; mode projet.

**Durée estimée.** 1 à 2 semaines.

**Preuves à garder.** Code sur GitHub, capture d'une exécution, liste produite, page de
veille mise à jour grâce à l'outil.

## 8. Réalisation du stage de 2e année (Erasmus+)

Elle dépendra des missions. **Avant de partir**, préviens ton tuteur que tu dois ramener une
réalisation décrite dans ton portfolio. **Pendant le stage** :

- tiens un journal de bord quotidien de cinq lignes (fait, problème, solution) ;
- fais des captures au fur et à mesure, en demandant ce que tu as le droit de publier ;
- garde le besoin de départ par écrit (courriel, ticket, cahier des charges) ;
- note les outils de l'équipe : gestion de versions, tickets, réunions, méthode de travail ;
- fais signer l'attestation de stage (modèle de la circulaire) **avant de rentrer**.

Si la mission est un développement, elle peut remplacer le projet 5 comme support de l'E6.

---

## Planning réaliste

Les dates d'examen sont à confirmer avec tes professeurs. En 2026, les dossiers E6 étaient
à déposer début avril dans certaines académies : le planning vise donc une **fin des
développements fin mars 2027**.

| Période | À faire | Résultat attendu |
|---|---|---|
| 16 – 30 novembre 2026 | Mettre le portfolio en ligne. Remplir les emplacements [À COMPLÉTER] des deux fiches de stage, ajouter les captures CapCut. Poser les questions aux professeurs. | Portfolio public, fiches de stage complètes, fiche du portfolio publiée |
| Décembre 2026 | Projet 6 (GLPI). Début du projet 4 : cahier des charges, maquettes, base de données. | Les 6 compétences sont couvertes |
| Janvier 2027 | Projet 4 : développement, tests, guide utilisateur. Une source de veille ajoutée. | Support E6 n° 1 terminé |
| Février 2027 | Projet 5 : conception, développement, tests. (À décaler si le stage tombe à cette période.) | Support E6 n° 2 bien avancé |
| Stage de 2e année (dates à confirmer) | Journal de bord, captures, attestation. | Matière pour la réalisation 8 |
| Mars 2027 | Fin du projet 5. Rédaction de la réalisation 8. Projet 7 s'il reste du temps. Fiches descriptives E6. | Dossier E6 prêt |
| Avril 2027 | Relecture complète, tableau de synthèse officiel, test du site sur un autre ordinateur et sur téléphone. Oraux blancs. | Dossier E5 prêt |
| Mai – juin 2027 | Épreuves (dates officielles à confirmer). Ne plus modifier l'adresse du site. | |

**Si tu manques de temps**, l'ordre de priorité est : 6 (couverture des compétences), 4 et 5
(E6), 8 (stage), puis 7.

**Une habitude à prendre** : à la fin de chaque séance de travail, deux minutes pour faire
une capture et noter une ligne dans le fichier `projet.md` (laissé en brouillon). Rédiger la
réalisation à la fin devient alors très rapide.
