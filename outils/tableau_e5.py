"""Fabrique le tableau de synthèse E5 (.xlsx) à partir des réalisations du site.

IMPORTANT : ce fichier reprend la structure du tableau de synthèse du BTS SIO
(annexe « Tableau de synthèse des réalisations professionnelles » de la circulaire
nationale), mais ce n'est PAS le fichier officiel. Le jour du dépôt, recopie les
croix dans le modèle .xlsx officiel de ta session, fourni par tes professeurs.
"""
from __future__ import annotations

from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

POLICE = "Arial"
TRAIT = Side(style="thin", color="7F8A99")
BORD = Border(left=TRAIT, right=TRAIT, top=TRAIT, bottom=TRAIT)
GRIS = PatternFill("solid", fgColor="E6EBF1")
BLEU = PatternFill("solid", fgColor="1B4B8F")


def _date(d) -> str:
    if not d:
        return ""
    date, precision = d
    if precision == "jour":
        return date.strftime("%d/%m/%Y")
    if precision == "mois":
        return date.strftime("%m/%Y")
    return str(date.year)


def creer_tableau(cible: Path, site: dict, competences: list[dict], groupes: list[dict],
                  bandeau: str = "") -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Tableau de synthèse"
    nb_cols = 3 + len(competences)
    derniere = get_column_letter(nb_cols)

    def ligne_titre(numero: int, texte: str, taille: int = 11, gras: bool = True) -> None:
        ws.merge_cells(f"A{numero}:{derniere}{numero}")
        cellule = ws[f"A{numero}"]
        cellule.value = texte
        cellule.font = Font(name=POLICE, size=taille, bold=gras)
        cellule.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    ligne_titre(1, f"BTS SERVICES INFORMATIQUES AUX ORGANISATIONS – SESSION {site.get('session', '')}", 12)
    ligne_titre(2, "Épreuve E5 – Support et mise à disposition de services informatiques")
    ligne_titre(3, "Tableau de synthèse des réalisations professionnelles")
    if bandeau:                      # version objectif : impossible à confondre avec le vrai
        ligne_titre(4, bandeau + " NI DÉPOSER – contient des réalisations non faites", 12)
        ws["A4"].font = Font(name=POLICE, size=12, bold=True, color="FFFFFF")
        ws["A4"].fill = PatternFill("solid", fgColor="B42318")
        ws.row_dimensions[4].height = 24

    infos = [
        ("Nom et prénom :", site.get("nom", "")),
        ("Option :", site.get("option", "")),
        ("N° candidat :", site.get("numero_candidat", "")),
        ("Centre de formation :", site.get("centre", "")),
        ("Adresse URL du portfolio :", site.get("url_portfolio", "")),
    ]
    for i, (libelle, valeur) in enumerate(infos, start=5):
        ws[f"A{i}"] = libelle
        ws[f"A{i}"].font = Font(name=POLICE, size=10, bold=True)
        ws.merge_cells(f"B{i}:{derniere}{i}")
        ws[f"B{i}"] = str(valeur or "")
        ws[f"B{i}"].font = Font(name=POLICE, size=10)

    entete = 11
    titres = ["Réalisation", "Début", "Fin"] + [c["intitule"] for c in competences]
    for col, titre in enumerate(titres, start=1):
        cellule = ws.cell(row=entete, column=col, value=titre)
        cellule.font = Font(name=POLICE, size=9, bold=True, color="FFFFFF")
        cellule.fill = BLEU
        cellule.border = BORD
        cellule.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[entete].height = 78

    ligne = entete + 1
    for groupe in groupes:
        ws.merge_cells(start_row=ligne, start_column=1, end_row=ligne, end_column=nb_cols)
        cellule = ws.cell(row=ligne, column=1, value=groupe["nom"])
        cellule.font = Font(name=POLICE, size=10, bold=True)
        cellule.fill = GRIS
        cellule.alignment = Alignment(vertical="center")
        for col in range(1, nb_cols + 1):
            ws.cell(row=ligne, column=col).border = BORD
        ws.row_dimensions[ligne].height = 20
        ligne += 1
        lignes_groupe = groupe["realisations"] or [None]
        for r in lignes_groupe:
            valeurs = ["", "", ""] if r is None else [r["titre"], _date(r["debut"]), _date(r["fin"]) if r["fin"] else "en cours"]
            for col, valeur in enumerate(valeurs, start=1):
                cellule = ws.cell(row=ligne, column=col, value=valeur)
                cellule.font = Font(name=POLICE, size=10)
                cellule.border = BORD
                cellule.alignment = Alignment(vertical="center", wrap_text=True,
                                              horizontal="left" if col == 1 else "center")
            for i, c in enumerate(competences, start=4):
                coche = "X" if r is not None and c["id"] in r["competences"] else ""
                cellule = ws.cell(row=ligne, column=i, value=coche)
                cellule.font = Font(name=POLICE, size=11, bold=True)
                cellule.border = BORD
                cellule.alignment = Alignment(horizontal="center", vertical="center")
            ws.row_dimensions[ligne].height = 30
            ligne += 1

    ligne += 1
    ws.merge_cells(start_row=ligne, start_column=1, end_row=ligne, end_column=nb_cols)
    note = ws.cell(row=ligne, column=1, value=(
        "Document généré automatiquement à partir du portfolio (mêmes données que le site). "
        "À reporter dans le modèle .xlsx officiel de la circulaire nationale de la session."))
    note.font = Font(name=POLICE, size=8, italic=True, color="556170")
    note.alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[ligne].height = 26

    ws.column_dimensions["A"].width = 46
    ws.column_dimensions["B"].width = 12
    ws.column_dimensions["C"].width = 12
    for col in range(4, nb_cols + 1):
        ws.column_dimensions[get_column_letter(col)].width = 17
    ws.freeze_panes = f"B{entete + 1}"
    ws.page_setup.orientation = "landscape"
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.print_title_rows = f"{entete}:{entete}"
    wb.save(cible)
