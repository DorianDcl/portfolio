---
titre: "La course à la gravure en 2 nanomètres"
resume: "Comment l'industrie des semi-conducteurs franchit la barrière des 2 nm : nouveaux transistors, machines de lithographie hors norme et assemblage de puces en trois dimensions."
theme: "Matériel et semi-conducteurs"
date: 2026-11-15
outils: [Google Alerts, Feedly, LinkedIn]
# Mes sources : une entrée par article lu (voir docs/VEILLE-METHODE.md).
# Les trois articles ci-dessous ont été trouvés par Claude pour vérifier les faits
# de la synthèse. Lis-les ; si tu les gardes, enlève les « # » en début de ligne.
sources: []
#  - titre: "TSMC A14 Validation Nears 90% of Target; Customer Interest Builds Ahead of 2028 Mass Production"
#    editeur: TrendForce
#    date: 2026-07-16
#    url: https://www.trendforce.com/news/2026/07/16/news-tsmc-says-a14-internal-validation-nears-90-of-target-strong-customer-interest-ahead-of-2028-mass-production/
#    note: "[À COMPLÉTER : ce que j'en retiens]"
#  - titre: "TSMC reiterates it doesn't need High-NA EUV for 1.4nm-class process technology"
#    editeur: Tom's Hardware
#    url: https://tech.yahoo.com/computing/articles/tsmc-reiterates-doesnt-high-na-202742547.html
#    note: "[À COMPLÉTER : ce que j'en retiens]"
#  - titre: "TSMC annonce le process de fabrication A14"
#    editeur: eeNews Europe
#    url: https://www.eenewseurope.com/fr/tsmc-annonce-le-process-de-fabrication-a14/
#    note: "[À COMPLÉTER : ce que j'en retiens]"
documents:
  - Présentation-la-course-au-2-nanomètres.pdf
brouillon: false
---

## Pourquoi ce sujet

L'industrie des semi-conducteurs miniaturise sans cesse les transistors pour
gagner en puissance et réduire la consommation d'énergie. À 2 nanomètres, on
atteint des dimensions où les lois de la physique deviennent un obstacle. J'ai
suivi la façon dont les acteurs majeurs du secteur, comme TSMC et ASML,
franchissent cette barrière.

## Ma démarche de veille

Je m'appuie sur trois outils complémentaires :

- **Google Alerts** m'envoie une notification dès qu'un article est publié sur mes mots-clés (TSMC, ASML).
- **Feedly** regroupe les flux RSS de la presse spécialisée au même endroit, ce qui m'évite de visiter chaque site.
- **LinkedIn** me permet de suivre des ingénieurs et des analystes du secteur, pour un regard plus critique que les annonces commerciales.

Cette organisation transforme un grand volume d'informations en quelques
articles triés, que je résume ensuite.

## Les deux obstacles : l'effet tunnel et la chaleur

À cette échelle, la barrière qui retient les électrons devient si fine qu'ils
peuvent la traverser : c'est **l'effet tunnel**. Dans l'architecture classique,
appelée **FinFET**, la grille contrôle le canal sur trois côtés seulement et le
courant fuit par le bas. Le second obstacle est **la chaleur** : plus les
transistors sont serrés, plus la surchauffe menace la puce.

La réponse s'appelle **GAAFET** (*Gate-All-Around*) : la grille entoure
complètement de fins feuillets de silicium. C'est comme serrer un tuyau
d'arrosage à pleine main au lieu de poser trois doigts dessus : les fuites
sont bloquées et la puce chauffe moins.

## L'actualité : TSMC et ASML

- **TSMC** a lancé la production en volume de son procédé 2 nm, appelé N2, au quatrième trimestre 2025. C'est sa première génération de transistors GAAFET.
- **ASML** livre ses nouvelles machines de lithographie **High-NA EUV** : plus grandes qu'un bus, elles coûtent environ 350 millions d'euros pièce. Leur précision revient à viser une pièce de monnaie sur la Lune depuis la Terre.
- À ne pas confondre : TSMC fabrique ses puces N2 avec les machines EUV de la génération précédente et a indiqué ne pas avoir besoin des machines High-NA pour ce procédé.

## Au-delà de la finesse : chiplets et empilement 3D

L'industrie innove aussi par l'architecture. Au lieu d'une seule grosse puce,
on assemble plusieurs petits modules spécialisés, les **chiplets**, dans un même
boîtier. Une couche de connexion, l'**interposeur**, les relie entre eux avec
une forte densité et une faible latence ; l'ensemble forme le **package**. Les
composants peuvent aussi être empilés en trois dimensions, ce qui augmente la
densité sans agrandir la puce. Le gain est important pour les infrastructures
de cloud et d'intelligence artificielle.

## Ce que j'en retiens pour mon métier

- **Anticiper** : connaître les prochaines générations de processeurs aide à éviter l'obsolescence du matériel.
- **Sobriété énergétique** : des processeurs plus efficaces réduisent l'empreinte carbone des services numériques.
- **Conseiller** : comprendre le matériel permet de mieux maîtriser le logiciel qui tourne dessus et d'éclairer les choix d'investissement.

La suite est déjà annoncée : le nœud de 1,4 nanomètre (A14) est prévu pour 2028.

## Sources

[À COMPLÉTER : la liste datée des articles que j'ai lus, dans l'en-tête de ce fichier (voir docs/VEILLE-METHODE.md)]
