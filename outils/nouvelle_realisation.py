#!/usr/bin/env python3
"""Crée le dossier d'une nouvelle réalisation à partir du modèle.

Utilisation :  python outils/nouvelle_realisation.py "Titre de la réalisation" formation
(le deuxième mot est la période : formation, stage-1 ou stage-2)
"""
import datetime as dt
import re
import shutil
import sys
import unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
PERIODES = ("formation", "stage-1", "stage-2")


def slug(texte: str) -> str:
    texte = unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", texte.lower()).strip("-")


def main() -> int:
    if len(sys.argv) < 2 or not sys.argv[1].strip():
        print("Indique un titre, par exemple : \"Application de gestion de tickets\"")
        return 1
    titre = sys.argv[1].strip()
    periode = sys.argv[2].strip() if len(sys.argv) > 2 else "formation"
    if periode not in PERIODES:
        print(f"Période inconnue : {periode}. Valeurs possibles : {', '.join(PERIODES)}")
        return 1
    dossier = RACINE / "realisations" / slug(titre)
    if dossier.exists():
        print(f"Le dossier realisations/{dossier.name} existe déjà.")
        return 1
    shutil.copytree(RACINE / "realisations" / "_modele", dossier)
    fichier = dossier / "projet.md"
    texte = fichier.read_text(encoding="utf-8")
    texte = texte.replace('titre: "Titre de la réalisation"', f'titre: "{titre.replace(chr(34), "")}"')
    texte = texte.replace("periode: formation", f"periode: {periode}")
    texte = texte.replace("date_debut: 2026-01-01", f"date_debut: {dt.date.today().isoformat()}")
    fichier.write_text(texte, encoding="utf-8")
    print(f"Dossier créé : realisations/{dossier.name} (en brouillon tant que « brouillon: true »).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
