#!/usr/bin/env python3
"""Construit le site du portfolio à partir des fichiers de contenu.

Utilisation :  python outils/construire.py
Résultat    :  le dossier _site/ (c'est lui qui est publié sur GitHub Pages).

Tu n'as normalement jamais besoin de modifier ce fichier : tout le contenu
se trouve dans les dossiers contenu/, realisations/ et veille/.
"""
from __future__ import annotations

import datetime as dt
import difflib
import os
import re
import shutil
import sys
import unicodedata
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from PIL import Image, ImageOps

RACINE = Path(__file__).resolve().parent.parent
OUTILS = RACINE / "outils"

# Deux modes, totalement séparés :
#   python outils/construire.py             -> le vrai site, dans _site/ (le seul publié)
#   python outils/construire.py --objectif  -> l'aperçu FICTIF, dans objectif/_apercu/ (jamais publié)
MODE_OBJECTIF = "--objectif" in sys.argv
SOURCE = RACINE / "objectif" if MODE_OBJECTIF else RACINE
SORTIE = SOURCE / "_apercu" if MODE_OBJECTIF else RACINE / "_site"
BANDEAU = "VERSION OBJECTIF – FICTIVE – NE PAS PUBLIER"

PERIODES = {
    "formation": "Réalisation en cours de formation",
    "stage-1": "Réalisation en milieu professionnel en cours de première année",
    "stage-2": "Réalisation en milieu professionnel en cours de seconde année",
}
PERIODES_COURT = {
    "formation": "En formation",
    "stage-1": "Stage de 1re année",
    "stage-2": "Stage de 2e année",
}
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
        "septembre", "octobre", "novembre", "décembre"]
EXT_IMAGES = {".png", ".jpg", ".jpeg", ".webp", ".gif"}
LARGEUR_MAX = 1600      # largeur maximale des images affichées en grand
LARGEUR_MINI = 720      # largeur des vignettes

erreurs: list[str] = []
avertissements: list[str] = []


# --------------------------------------------------------------------------
# Petits outils
# --------------------------------------------------------------------------
def erreur(fichier: Path | str, message: str) -> None:
    chemin = fichier.relative_to(RACINE) if isinstance(fichier, Path) else fichier
    erreurs.append(f"{chemin} : {message}")


def avertir(message: str) -> None:
    avertissements.append(message)


def slug(texte: str) -> str:
    """Transforme « Été 2026 : Site Odoo » en « ete-2026-site-odoo »."""
    texte = unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", texte.lower()).strip("-")


def lire_yaml(fichier: Path) -> dict:
    try:
        donnees = yaml.safe_load(fichier.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        ligne = getattr(getattr(exc, "problem_mark", None), "line", None)
        ou = f" (vers la ligne {ligne + 1})" if ligne is not None else ""
        erreur(fichier, f"le fichier est mal écrit{ou}. Vérifie les espaces en début "
                        "de ligne et mets entre guillemets les textes qui contiennent « : ».")
        return {}
    if not isinstance(donnees, dict):
        erreur(fichier, "le fichier devrait contenir des lignes « nom: valeur ».")
        return {}
    return donnees


def lire_markdown(fichier: Path) -> tuple[dict, str]:
    """Sépare l'en-tête (entre deux lignes ---) du texte en Markdown."""
    texte = fichier.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    if not texte.startswith("---"):
        return {}, texte
    morceaux = texte.split("\n---", 1)
    if len(morceaux) < 2:
        erreur(fichier, "l'en-tête commence par « --- » mais la ligne « --- » de fin est absente.")
        return {}, ""
    entete_brut = morceaux[0][3:]
    corps = morceaux[1].lstrip("-").lstrip("\n")
    try:
        entete = yaml.safe_load(entete_brut) or {}
    except yaml.YAMLError as exc:
        ligne = getattr(getattr(exc, "problem_mark", None), "line", None)
        ou = f" (vers la ligne {ligne + 2})" if ligne is not None else ""
        erreur(fichier, f"l'en-tête est mal écrit{ou}. Vérifie les espaces en début de ligne "
                        "et mets entre guillemets les textes qui contiennent « : ».")
        return {}, corps
    if not isinstance(entete, dict):
        erreur(fichier, "l'en-tête devrait contenir des lignes « nom: valeur ».")
        return {}, corps
    return entete, corps


MARQUEUR = re.compile(r"\[À COMPLÉTER[^\]]*\]")


def en_html(texte: str, origine: str = "") -> str:
    """Convertit le Markdown en HTML et signale les emplacements [À COMPLÉTER : …]."""
    nombre = len(MARQUEUR.findall(texte))
    if nombre and origine:
        avertir(f"{origine} : {nombre} emplacement(s) [À COMPLÉTER] encore visible(s) sur le site.")
    html = markdown.markdown(texte, extensions=["extra", "sane_lists"], output_format="html5")
    return MARQUEUR.sub(lambda m: f'<mark class="a-completer">{m.group(0)}</mark>', html)


def en_liste(valeur) -> list:
    if valeur is None:
        return []
    if isinstance(valeur, (list, tuple)):
        return [v for v in valeur if v not in (None, "")]
    return [valeur]


def lire_date(valeur, fichier: Path, champ: str):
    """Accepte 2026-06-16, 2026-06 ou 2026. Renvoie (date, précision) ou None."""
    if valeur in (None, ""):
        return None
    if isinstance(valeur, dt.datetime):
        return valeur.date(), "jour"
    if isinstance(valeur, dt.date):
        return valeur, "jour"
    texte = str(valeur).strip()
    for motif, precision in ((r"^(\d{4})-(\d{1,2})-(\d{1,2})$", "jour"),
                             (r"^(\d{4})-(\d{1,2})$", "mois"), (r"^(\d{4})$", "annee")):
        m = re.match(motif, texte)
        if m:
            nombres = [int(x) for x in m.groups()] + [1, 1]
            try:
                return dt.date(nombres[0], nombres[1], nombres[2]), precision
            except ValueError:
                break
    erreur(fichier, f"« {champ}: {texte} » n'est pas une date valide. "
                    "Écris par exemple 2026-06-16 (année-mois-jour) ou 2026-06.")
    return None


def date_fr(d) -> str:
    if not d:
        return ""
    date, precision = d
    if precision == "annee":
        return str(date.year)
    if precision == "mois":
        return f"{MOIS[date.month - 1]} {date.year}"
    jour = "1er" if date.day == 1 else str(date.day)
    return f"{jour} {MOIS[date.month - 1]} {date.year}"


def periode_fr(debut, fin) -> str:
    if debut and fin and debut != fin:
        return f"du {date_fr(debut)} au {date_fr(fin)}"
    if debut and not fin:
        return f"depuis {date_fr(debut)}" if debut[1] == "jour" else date_fr(debut)
    return date_fr(debut or fin)


def taille_lisible(octets: int) -> str:
    if octets < 1024 * 1024:
        return f"{max(1, round(octets / 1024))} Ko"
    return f"{octets / 1024 / 1024:.1f} Mo".replace(".", ",")


def joli_nom(nom_fichier: str) -> str:
    """« 02-page-accueil.png » devient « Page accueil »."""
    base = Path(nom_fichier).stem
    base = re.sub(r"^\d+[-_ ]*", "", base)
    base = re.sub(r"[-_]+", " ", base).strip()
    return base[:1].upper() + base[1:] if base else nom_fichier


# --------------------------------------------------------------------------
# Lecture du contenu
# --------------------------------------------------------------------------
def charger_competences() -> list[dict]:
    donnees = lire_yaml(RACINE / "contenu" / "competences.yml")
    return donnees.get("competences", [])


def traiter_images(dossier: Path, cible: Path, legendes: dict) -> list[dict]:
    """Redimensionne et allège chaque image (format WebP) + crée une vignette."""
    images = []
    if not dossier.is_dir():
        return images
    for fichier in sorted(dossier.iterdir(), key=lambda p: p.name.lower()):
        if fichier.suffix.lower() not in EXT_IMAGES:
            continue
        nom = slug(fichier.stem) or "image"
        try:
            with Image.open(fichier) as brute:
                image = ImageOps.exif_transpose(brute)
                image = image.convert("RGBA" if image.mode in ("RGBA", "LA", "P") else "RGB")
                cible.mkdir(parents=True, exist_ok=True)
                tailles = {}
                for suffixe, largeur in (("", LARGEUR_MAX), ("-mini", LARGEUR_MINI)):
                    copie = image.copy()
                    copie.thumbnail((largeur, largeur * 3), Image.LANCZOS)
                    copie.save(cible / f"{nom}{suffixe}.webp", "WEBP", quality=82, method=6)
                    tailles[suffixe] = copie.size
        except Exception as exc:  # image illisible : on prévient sans tout casser
            erreur(fichier, f"image illisible ({exc}). Enregistre-la à nouveau en PNG ou JPG.")
            continue
        legende = legendes.get(fichier.name) or legendes.get(fichier.stem) or joli_nom(fichier.name)
        images.append({
            "grand": f"images/{nom}.webp", "mini": f"images/{nom}-mini.webp",
            "legende": str(legende),
            "largeur": tailles[""][0], "hauteur": tailles[""][1],
            "mini_largeur": tailles["-mini"][0], "mini_hauteur": tailles["-mini"][1],
        })
    return images


def copier_documents(dossier: Path, cible: Path) -> list[dict]:
    documents = []
    if not dossier.is_dir():
        return documents
    for fichier in sorted(dossier.iterdir(), key=lambda p: p.name.lower()):
        if not fichier.is_file() or fichier.name.startswith(".") or fichier.name == "LISEZ-MOI.txt":
            continue
        cible.mkdir(parents=True, exist_ok=True)
        nom = slug(fichier.stem) + fichier.suffix.lower()
        shutil.copy2(fichier, cible / nom)
        documents.append({"url": f"documents/{nom}", "nom": joli_nom(fichier.name),
                          "type": fichier.suffix.lstrip(".").upper(),
                          "taille": taille_lisible(fichier.stat().st_size)})
    return documents


def verifier_liste_fixe(valeurs: list, autorisees: list[str], fichier: Path, champ: str) -> list[str]:
    bonnes = []
    for valeur in valeurs:
        valeur = str(valeur).strip()
        if valeur in autorisees:
            if valeur not in bonnes:
                bonnes.append(valeur)
            continue
        proches = difflib.get_close_matches(valeur, autorisees, n=1, cutoff=0.5)
        conseil = f" Voulais-tu écrire « {proches[0]} » ?" if proches else ""
        erreur(fichier, f"« {valeur} » n'existe pas dans « {champ} ».{conseil} "
                        f"Valeurs possibles : {', '.join(autorisees)}.")
    return bonnes


def charger_liens(entete: dict, fichier: Path) -> list[dict]:
    liens = []
    for lien in en_liste(entete.get("liens")):
        if isinstance(lien, dict) and lien.get("url"):
            liens.append({"texte": str(lien.get("texte") or lien["url"]), "url": str(lien["url"])})
        elif isinstance(lien, str) and lien.strip():
            liens.append({"texte": lien, "url": lien})
        elif lien:
            erreur(fichier, "chaque lien doit s'écrire « - texte: Mon dépôt » puis « url: https://… ».")
    return liens


def charger_realisations(competences: list[dict]) -> list[dict]:
    ids = [c["id"] for c in competences]
    realisations = []
    base = SOURCE / "realisations"
    for dossier in sorted(p for p in base.iterdir() if p.is_dir()):
        if dossier.name.startswith(("_", ".")):
            continue                      # _modele et dossiers cachés : ignorés
        fichier = dossier / "projet.md"
        if not fichier.exists():
            erreur(dossier, "il manque le fichier projet.md dans ce dossier.")
            continue
        avant = len(erreurs)
        entete, corps = lire_markdown(fichier)
        if len(erreurs) > avant:
            continue                      # en-tête illisible : inutile d'aller plus loin
        if entete.get("brouillon") is True:
            avertir(f"realisations/{dossier.name} est en brouillon : elle n'est pas publiée.")
            continue
        identifiant = slug(dossier.name)
        if not entete.get("titre"):
            erreur(fichier, "il manque la ligne « titre: » dans l'en-tête.")
        periode = str(entete.get("periode") or "").strip()
        if periode not in PERIODES:
            verifier_liste_fixe([periode or "(vide)"], list(PERIODES), fichier, "periode")
            periode = "formation"
        comps = verifier_liste_fixe(en_liste(entete.get("competences")), ids, fichier, "competences")
        if not en_liste(entete.get("competences")):
            avertir(f"realisations/{dossier.name} : aucune compétence indiquée, "
                    "elle n'apparaîtra pas dans le tableau de synthèse.")
        debut = lire_date(entete.get("date_debut"), fichier, "date_debut")
        fin = lire_date(entete.get("date_fin"), fichier, "date_fin")
        if not debut and entete.get("date_debut") in (None, ""):
            erreur(fichier, "il manque « date_debut: » (exemple : 2026-06-16 ou 2026-06).")
        if debut and fin and fin[0] < debut[0]:
            erreur(fichier, "la date de fin est avant la date de début.")
        legendes = entete.get("legendes") if isinstance(entete.get("legendes"), dict) else {}
        cible = SORTIE / "realisations" / identifiant
        realisations.append({
            "id": identifiant,
            "titre": str(entete.get("titre") or dossier.name),
            "resume": str(entete.get("resume") or ""),
            "organisation": str(entete.get("organisation") or ""),
            "periode": periode,
            "periode_nom": PERIODES[periode],
            "periode_court": PERIODES_COURT[periode],
            "debut": debut, "fin": fin,
            "dates": periode_fr(debut, fin),
            "annee": debut[0].year if debut else None,
            "tri": debut[0] if debut else dt.date(1900, 1, 1),
            "technologies": [str(t) for t in en_liste(entete.get("technologies"))],
            "competences": comps,
            "e6": entete.get("e6") is True,
            "liens": charger_liens(entete, fichier),
            "html": en_html(corps, f"realisations/{dossier.name}/projet.md"),
            "images": traiter_images(dossier / "images", cible / "images", legendes),
            "documents": copier_documents(dossier / "documents", cible / "documents"),
            "url": f"realisations/{identifiant}/",
        })
    realisations.sort(key=lambda r: r["tri"], reverse=True)
    return realisations


def charger_veilles() -> list[dict]:
    veilles = []
    base = SOURCE / "veille"
    docs_cible = SORTIE / "veille" / "documents"
    for fichier in sorted(base.glob("*.md")):
        if fichier.name.startswith("_"):
            continue
        avant = len(erreurs)
        entete, corps = lire_markdown(fichier)
        if len(erreurs) > avant:
            continue
        if entete.get("brouillon") is True:
            avertir(f"veille/{fichier.name} est en brouillon : elle n'est pas publiée.")
            continue
        if not entete.get("titre"):
            erreur(fichier, "il manque la ligne « titre: » dans l'en-tête.")
        date = lire_date(entete.get("date"), fichier, "date")
        if not date and entete.get("date") in (None, ""):
            erreur(fichier, "il manque « date: » (exemple : 2026-11-15).")
        sources = []
        for source in en_liste(entete.get("sources")):
            if isinstance(source, dict) and source.get("titre"):
                d = lire_date(source.get("date"), fichier, "date d'une source")
                sources.append({"titre": str(source["titre"]), "url": str(source.get("url") or ""),
                                "editeur": str(source.get("editeur") or ""), "date": date_fr(d),
                                "tri": d[0] if d else dt.date(1900, 1, 1),
                                "note": str(source.get("note") or ""),
                                "impact": str(source.get("impact") or "")})
            elif source:
                erreur(fichier, "chaque source doit s'écrire « - titre: … » puis « url: … ».")
        sources.sort(key=lambda s: s["tri"], reverse=True)
        documents = []
        for nom in en_liste(entete.get("documents")):
            origine = base / "documents" / str(nom)
            if not origine.exists():
                erreur(fichier, f"le document « {nom} » est introuvable dans veille/documents/.")
                continue
            docs_cible.mkdir(parents=True, exist_ok=True)
            propre = slug(origine.stem) + origine.suffix.lower()
            shutil.copy2(origine, docs_cible / propre)
            documents.append({"url": f"veille/documents/{propre}", "nom": joli_nom(origine.name),
                              "type": origine.suffix.lstrip(".").upper(),
                              "taille": taille_lisible(origine.stat().st_size)})
        identifiant = slug(fichier.stem)
        veilles.append({
            "id": identifiant, "titre": str(entete.get("titre") or fichier.stem),
            "resume": str(entete.get("resume") or ""), "theme": str(entete.get("theme") or ""),
            "date": date_fr(date), "tri": date[0] if date else dt.date(1900, 1, 1),
            "outils": [str(o) for o in en_liste(entete.get("outils"))],
            "sources": sources, "documents": documents,
            "html": en_html(corps, f"veille/{fichier.name}"), "url": f"veille/{identifiant}/",
        })
    veilles.sort(key=lambda v: v["tri"], reverse=True)
    return veilles


def charger_page(nom: str) -> dict:
    fichier = SOURCE / "contenu" / "pages" / f"{nom}.md"
    if not fichier.exists():
        erreur(fichier, "ce fichier de page est absent.")
        return {"html": "", "titre": nom}
    entete, corps = lire_markdown(fichier)
    entete["html"] = en_html(corps, f"contenu/pages/{nom}.md")
    return entete


# --------------------------------------------------------------------------
# Écriture du site
# --------------------------------------------------------------------------
def ecrire(env: Environment, gabarit: str, chemin: str, **contexte) -> None:
    cible = SORTIE / chemin
    cible.parent.mkdir(parents=True, exist_ok=True)
    profondeur = chemin.count("/")
    contexte.setdefault("racine", "../" * profondeur)
    contexte["page_url"] = chemin.removesuffix("index.html")
    html = env.get_template(gabarit).render(**contexte)
    if MODE_OBJECTIF:
        html = habiller_objectif(html)
    cible.write_text(html, encoding="utf-8")


ETATS = {"FAIT": ("fait", "Fait"), "À FAIRE": ("afaire", "À réaliser")}


def habiller_objectif(html: str) -> str:
    """Mode objectif : colore ce qui est fait / à réaliser et rend les liens utilisables
    en ouvrant simplement les fichiers (double-clic), sans serveur."""
    def bloc(m):
        classe, libelle = ETATS[m.group(3)]
        return (f'<{m.group(1)}{m.group(2)} class="etat-{classe}">'
                f'<span class="etat etat-{classe}">{libelle}</span> ')
    html = re.sub(r"<(li|p|td|dd|h3)((?:\s[^>]*)?)>\s*(?:<p>)?\[(FAIT|À FAIRE)\]\s*", bloc, html)
    html = re.sub(r"\[(FAIT|À FAIRE)\]\s*",
                  lambda m: f'<span class="etat etat-{ETATS[m.group(1)][0]}">{ETATS[m.group(1)][1]}</span> ', html)

    def lien(m):
        url = m.group(1)
        if url.startswith(("http", "mailto:", "#", "data:")):
            return m.group(0)
        chemin, diese, ancre = url.partition("#")
        if chemin == "" or chemin.endswith("/"):
            chemin += "index.html"
        return f'href="{chemin}{diese}{ancre}"'
    return re.sub(r'href="([^"]*)"', lien, html)


def verifier_etancheite() -> None:
    """Sécurité : rien de la version objectif ne doit se retrouver dans le vrai site."""
    for fichier in SORTIE.rglob("*"):
        if "objectif" in fichier.relative_to(SORTIE).as_posix().lower():
            erreur(fichier, "un fichier de la version objectif se trouve dans le site publié.")
        elif fichier.suffix in (".html", ".css", ".js") and BANDEAU in fichier.read_text(encoding="utf-8", errors="ignore"):
            erreur(fichier, "du contenu de la version objectif (fictive) se trouve dans le site publié.")


def creer_cv_pdf(env: Environment, contexte: dict) -> str | None:
    """Fabrique le PDF du CV. Si un PDF est déposé dans contenu/, il est prioritaire."""
    cible = SORTIE / "documents"
    cible.mkdir(parents=True, exist_ok=True)
    nom_pdf = f"CV-{slug(contexte['site'].get('nom', 'cv'))}.pdf"
    depose = RACINE / "contenu" / "cv.pdf"
    if depose.exists():
        shutil.copy2(depose, cible / nom_pdf)
        return f"documents/{nom_pdf}"
    try:
        from weasyprint import HTML
        html = env.get_template("cv-pdf.html").render(**contexte, racine="")
        HTML(string=html, base_url=str(OUTILS / "style")).write_pdf(cible / nom_pdf)
        return f"documents/{nom_pdf}"
    except Exception as exc:
        avertir(f"le PDF du CV n'a pas pu être créé ({type(exc).__name__}). "
                "Dépose ton CV sous le nom contenu/cv.pdf pour qu'il soit proposé au téléchargement.")
        return None


def construire() -> int:
    if SORTIE.exists():
        shutil.rmtree(SORTIE)
    SORTIE.mkdir()

    site = lire_yaml(SOURCE / "contenu" / "site.yml")
    cv = lire_yaml(SOURCE / "contenu" / "cv.yml")
    competences = charger_competences()
    realisations = charger_realisations(competences)
    veilles = charger_veilles()
    pages = {nom: charger_page(nom) for nom in ("accueil", "bts-sio", "parcours", "contact")}

    par_id = {c["id"]: c for c in competences}
    for c in competences:
        c["realisations"] = [r for r in realisations if c["id"] in r["competences"]]
        if not c["realisations"]:
            avertir(f"compétence pas encore couverte par une réalisation : {c['intitule']}.")
    groupes = [{"id": pid, "nom": nom, "court": PERIODES_COURT[pid],
                "realisations": sorted((r for r in realisations if r["periode"] == pid),
                                       key=lambda r: r["tri"])}
               for pid, nom in PERIODES.items()]
    technologies = sorted({t for r in realisations for t in r["technologies"]}, key=str.lower)

    env = Environment(loader=FileSystemLoader(OUTILS / "gabarits"), autoescape=True,
                      undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True)
    env.filters["slug"] = slug
    contexte = {
        "site": site, "cv": cv, "competences": competences, "par_id": par_id,
        "realisations": realisations, "veilles": veilles, "groupes": groupes,
        "technologies": technologies, "periodes_court": PERIODES_COURT,
        "annee": dt.date.today().year,
        "mise_a_jour": date_fr((dt.date.today(), "jour")),
    }

    # Fichiers fixes : style, script, polices
    shutil.copytree(OUTILS / "style", SORTIE / "style")
    (SORTIE / ".nojekyll").write_text("")

    contexte["objectif"] = MODE_OBJECTIF
    contexte["bandeau"] = BANDEAU
    if MODE_OBJECTIF:
        shutil.copy2(OUTILS / "objectif.css", SORTIE / "style" / "objectif.css")
        contexte["cv_pdf"] = None       # pas de CV fictif en PDF : il pourrait circuler
    else:
        contexte["cv_pdf"] = creer_cv_pdf(env, contexte)

    # Tableau de synthèse E5 (.xlsx), fabriqué avec les mêmes données que le site
    try:
        sys.path.insert(0, str(OUTILS))
        from tableau_e5 import creer_tableau
        (SORTIE / "documents").mkdir(exist_ok=True)
        prefixe = "FICTIF-NE-PAS-DEPOSER-" if MODE_OBJECTIF else ""
        nom_xlsx = f"{prefixe}Tableau-de-synthese-E5-{slug(site.get('nom', ''))}.xlsx"
        creer_tableau(SORTIE / "documents" / nom_xlsx, site, competences, groupes,
                      bandeau=BANDEAU if MODE_OBJECTIF else "")
        contexte["tableau_xlsx"] = f"documents/{nom_xlsx}"
    except Exception as exc:
        contexte["tableau_xlsx"] = None
        avertir(f"le tableau de synthèse .xlsx n'a pas pu être créé ({exc}).")

    ecrire(env, "accueil.html", "index.html", page=pages["accueil"], actif="accueil", **contexte)
    ecrire(env, "page.html", "bts-sio/index.html", page=pages["bts-sio"], actif="bts-sio", **contexte)
    ecrire(env, "cv.html", "cv/index.html", actif="cv", **contexte)
    ecrire(env, "parcours.html", "parcours/index.html", page=pages["parcours"], actif="parcours", **contexte)
    ecrire(env, "realisations.html", "realisations/index.html", actif="realisations", **contexte)
    for r in realisations:
        ecrire(env, "realisation.html", r["url"] + "index.html", r=r, actif="realisations", **contexte)
    ecrire(env, "competences.html", "competences/index.html", actif="competences", **contexte)
    ecrire(env, "veille.html", "veille/index.html", actif="veille", **contexte)
    for v in veilles:
        ecrire(env, "veille-detail.html", v["url"] + "index.html", v=v, actif="veille", **contexte)
    ecrire(env, "contact.html", "contact/index.html", page=pages["contact"], actif="contact", **contexte)
    # La page 404 peut s'afficher à n'importe quelle adresse : ses liens partent de la racine du site.
    from urllib.parse import urlparse
    base = urlparse(str(site.get("url_portfolio") or "")).path or "/"
    ecrire(env, "404.html", "404.html", actif="", racine=base.rstrip("/") + "/", **contexte)

    if not MODE_OBJECTIF:
        verifier_etancheite()
    return len(realisations)


def rapport(nombre: int) -> int:
    lignes = []
    if erreurs:
        lignes.append("## ❌ Le site n'a PAS été mis à jour\n")
        lignes.append("Corrige les points ci-dessous, puis enregistre à nouveau. "
                      "En attendant, l'ancienne version du site reste en ligne.\n")
        lignes += [f"- {e}" for e in erreurs]
    else:
        if MODE_OBJECTIF:
            lignes.append(f"## Aperçu FICTIF construit dans objectif/_apercu/ : {nombre} fiche(s). "
                          "Ouvre objectif/_apercu/index.html. Ne le publie jamais.\n")
        else:
            lignes.append(f"## ✅ Site construit : {nombre} réalisation(s) publiée(s)\n")
    if avertissements:
        lignes.append("\n### À savoir (cela ne bloque pas la publication)\n")
        lignes += [f"- {a}" for a in avertissements]
    texte = "\n".join(lignes)
    print(texte)
    resume = os.environ.get("GITHUB_STEP_SUMMARY")
    if resume:
        with open(resume, "a", encoding="utf-8") as f:
            f.write(texte + "\n")
    return 1 if erreurs else 0


if __name__ == "__main__":
    try:
        total = construire()
    except Exception as exc:  # filet de sécurité : message lisible plutôt qu'un plantage
        erreurs.append(f"Erreur inattendue pendant la construction : {type(exc).__name__} : {exc}")
        total = 0
    sys.exit(rapport(total))
