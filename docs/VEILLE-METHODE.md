# Ma veille : angle, rythme et modèle de synthèse

## 1. Trois angles possibles pour relier le sujet à l'option SLAM

Le sujet reste « la course à la gravure en 2 nanomètres ». Il s'agit de choisir **la question
de développeur** à laquelle la veille répond. Choisis-en un seul : il deviendra la dernière
partie de ta synthèse et le fil de tes prochaines lectures.

**Angle A. Des puces plus fines, pour quelles applications ? (IA et cloud)**
Question : qu'est-ce que les nouvelles puces changent pour celui qui développe ou héberge une
application, notamment d'intelligence artificielle ?
À suivre : annonces de processeurs et d'accélérateurs gravés en 2 nm, offres des hébergeurs
cloud, coût et consommation des calculs d'IA.
Intérêt : très actuel, facile à relier aux chiplets que tu présentes déjà.
Limite : beaucoup de communication commerciale, il faudra trier.

**Angle B. Le matériel progresse, le code doit-il encore être sobre ? (Green IT)**
Question : si chaque génération de puce consomme moins, pourquoi parle-t-on d'écoconception
logicielle ?
À suivre : consommation des centres de données, effet rebond, référentiels d'écoconception de
services numériques, outils de mesure de la consommation d'un programme.
Intérêt : prolonge ta conclusion actuelle (Green IT) et débouche sur des pratiques de code que
tu peux appliquer et montrer dans tes projets.
Limite : il faut des chiffres sourcés, pas des généralités.

**Angle C. La puissance ne sera plus « gratuite » : la performance devient l'affaire du développeur**
Question : quand graver plus fin coûte de plus en plus cher, comment gagne-t-on en performance ?
À suivre : coût des nouveaux nœuds, architectures spécialisées (chiplets, processeurs ARM),
optimisation logicielle, programmation parallèle.
Intérêt : le plus proche du métier de développeur, original.
Limite : plus technique, demande de bien comprendre ce que tu avances.

> Mon conseil : **l'angle B** si tu veux un lien direct avec tes projets (tu pourras dire « voici
> ce que j'applique dans mon code »), **l'angle A** si tu préfères rester proche de l'actualité.

## 2. Le rythme jusqu'à l'examen

| Fréquence | Durée | Ce que tu fais |
|---|---|---|
| Chaque semaine | 15 minutes | Parcourir Feedly et les alertes Google. Mettre de côté un ou deux articles. |
| Toutes les deux semaines | 20 minutes | Lire **un** article à fond et ajouter une fiche (modèle ci-dessous) dans le fichier de veille. |
| Chaque mois | 30 minutes | Relire les fiches du mois, mettre à jour la partie « L'actualité » de la synthèse et la date. |
| Un mois avant l'épreuve | 1 heure | Relire toute la synthèse, refaire la conclusion, mettre à jour le diaporama. |

De décembre à avril, cela donne une dizaine de fiches datées : c'est ce qui prouve au jury
que la veille est régulière, et pas faite la veille de l'oral.

Pense aussi à adapter tes outils à l'angle choisi : ajoute un ou deux mots-clés dans Google
Alerts et un ou deux flux dans Feedly, et note-les dans la partie « Ma démarche de veille ».

## 3. Le modèle de fiche (une par article lu)

À coller en haut de la liste `sources:` dans l'en-tête du fichier `veille/gravure-2-nanometres.md` :

```yaml
sources:
  - titre: "Titre exact de l'article"
    editeur: "Nom du site ou du journal"
    date: 2026-12-03
    url: https://adresse-de-l-article
    note: "L'information principale, avec mes mots, en une ou deux phrases."
    impact: "Ce que cela change pour un développeur, en une phrase."
```

Règles :

- uniquement des articles que tu as **vraiment lus** ;
- la date est celle de **l'article**, pas celle de ta lecture ;
- privilégie les sources d'origine (communiqué du fabricant, presse spécialisée) ;
- si deux sources se contredisent, note-le : c'est un bon point à l'oral.

Sur le site, ces fiches s'affichent dans la partie « Journal de veille », de la plus récente
à la plus ancienne.

## 4. Le plan de la synthèse (déjà en place dans le fichier)

1. Pourquoi ce sujet
2. Ma démarche de veille (outils, mots-clés)
3. Ce qu'il faut comprendre (effet tunnel, FinFET, GAAFET)
4. L'actualité (mise à jour chaque mois)
5. Ce que j'en retiens pour mon métier de développeur (à réécrire selon l'angle choisi)
6. Journal de veille (les fiches)
