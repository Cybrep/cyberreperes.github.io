#!/usr/bin/env python3
"""
CyberRepères — Préprocesseur éditorial Markdown/Jekyll — V3.2

V3 est conçu autour de la structure graphique réellement utilisée par
CyberRepères. Le contenu éditorial reste en Markdown ; les blocs spéciaux
décrivent uniquement les composants visuels.

Le script NE convertit PAS tout le Markdown en HTML.
Il transforme uniquement les directives CyberRepères en HTML portant les
classes CSS attendues par le site, et conserve le front matter Jekyll.

Usage :
    python scripts/markdown_to_html.py source.md sortie.md

Exemple :
    :::intro home

    CyberRepères rassemble des références, méthodes et ressources pour aider à
    comprendre et structurer les démarches de cybersécurité industrielle.

    :::

    ## Une section

    Texte en **Markdown**.

    :::cards
    ...
    :::

Blocs :
    :::intro home
    :::intro comprendre
    :::intro referentiels
    :::intro methodes
    :::intro normes
    :::cards
    :::chain
    :::points
    :::story

Le script peut être utilisé sur une page Jekyll complète : le bloc
---
layout: default
...
---
est conservé.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


INTRO_THEMES = {
    "home": ("home-hero", "CYBERSÉCURITÉ INDUSTRIELLE"),
    "comprendre": ("catalogue-intro catalogue-intro-comprendre", "COMPRENDRE"),
    "referentiels": ("catalogue-intro catalogue-intro-referentiels", "RÉFÉRENTIELS"),
    "methodes": ("catalogue-intro catalogue-intro-methodes", "MÉTHODES"),
    "normes": ("catalogue-intro catalogue-intro-normes", "NORMES & STANDARDS"),
}

BLOCK_CLASSES = {
    "cards": "home-cards",
    "chain": "home-chain",
    "points": "home-points",
    "story": "home-story",
}


def split_front_matter(text: str) -> tuple[str, str]:
    """Retourne (front_matter, body), sans modifier le front matter."""
    if not text.startswith("---"):
        return "", text

    match = re.match(
        r"\A---[ \t]*\r?\n.*?\r?\n---[ \t]*(?:\r?\n|$)",
        text,
        flags=re.DOTALL,
    )

    if not match:
        return "", text

    return match.group(0), text[match.end():]


def transform_blocks(text: str) -> str:
    """Transforme les directives :::...::: en HTML CyberRepères."""
    pattern = re.compile(
        r"^[ \t]*:::(?P<kind>[A-Za-z0-9_-]+)"
        r"(?:[ \t]+(?P<variant>[A-Za-z0-9_-]+))?[ \t]*\r?\n"
        r"(?P<body>.*?)"
        r"^[ \t]*:::[ \t]*$",
        re.MULTILINE | re.DOTALL,
    )

    def replace(match: re.Match[str]) -> str:
        kind = match.group("kind").lower()
        variant = match.group("variant")
        body = match.group("body").strip()

        if kind == "intro":
            theme = variant or "home"
            if theme not in INTRO_THEMES:
                raise ValueError(
                    f"Thème intro inconnu : {theme}. "
                    f"Disponibles : {', '.join(INTRO_THEMES)}"
                )

            css_class, label = INTRO_THEMES[theme]

            # Le hero de l'accueil possède sa propre structure cible.
            # Le contenu du bloc devient le paragraphe du hero.
            if theme == "home":
                return (
                    '<div class="home-hero">\n\n'
                    '  <div class="home-hero-label">\n'
                    f'    {label}\n'
                    '  </div>\n\n'
                    '  <h1>Des références pour comprendre,<br>'
                    'des repères pour agir.</h1>\n\n'
                    '  <p>\n'
                    f'    {body}\n'
                    '  </p>\n\n'
                    '</div>'
                )

            # Le CSS de catalogue-intro cible explicitement les <p>.
            # On conserve donc une source Markdown propre et on transforme
            # chaque paragraphe séparé par une ligne vide en <p>.
            paragraphs = [
                part.strip()
                for part in re.split(r"\n\s*\n", body)
                if part.strip()
            ]

            rendered_paragraphs = "\n\n".join(
                f"    <p>\n{part}\n    </p>"
                for part in paragraphs
            )

            return (
                f'<div class="{css_class}">\n\n'
                '  <div class="catalogue-intro-label">\n'
                f'    {label}\n'
                '  </div>\n\n'
                '  <div class="catalogue-intro-content">\n\n'
                f'{rendered_paragraphs}\n\n'
                '  </div>\n\n'
                '</div>'
            )

        if kind == "cards":
            return (
                '<div class="home-cards">\n'
                f'{body}\n'
                '</div>'
            )

        if kind == "chain":
            return (
                '<div class="home-chain">\n'
                f'{body}\n'
                '</div>'
            )

        if kind == "points":
            # Le CSS cible des div enfants directs, pas une <ul>.
            # On accepte donc une liste Markdown simple et la convertit
            # directement en <div> pour reproduire la structure validée.
            items = []
            for line in body.splitlines():
                line = line.strip()
                if not line:
                    continue
                if line.startswith("- "):
                    items.append(line[2:].strip())
                elif line.startswith("* "):
                    items.append(line[2:].strip())
                else:
                    items.append(line)

            rendered = "\n".join(f"  <div>{item}</div>" for item in items)

            return (
                '<div class="home-points">\n'
                f'{rendered}\n'
                '</div>'
            )

        if kind == "story":
            return (
                '<div class="home-story">\n'
                f'{body}\n'
                '</div>'
            )

        raise ValueError(
            f"Bloc CyberRepères inconnu : {kind}. "
            "Disponibles : intro, cards, chain, points, story."
        )

    previous = None
    while previous != text:
        previous = text
        text = pattern.sub(replace, text)

    return text


def convert_document(text: str) -> str:
    front_matter, body = split_front_matter(text)
    body = transform_blocks(body).strip()

    if front_matter:
        return f"{front_matter}\n{body}\n"

    return f"{body}\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prétraite une page Markdown/Jekyll CyberRepères."
    )
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("output", nargs="?", type=Path)
    parser.add_argument("--input", dest="input_option", type=Path)
    parser.add_argument("--output", dest="output_option", type=Path)
    args = parser.parse_args()

    source = args.input_option or args.input
    output = args.output_option or args.output

    if not source:
        parser.error("Le fichier source est obligatoire.")

    if not source.exists():
        print(f"ERREUR : fichier introuvable : {source}")
        return 2

    if not output:
        output = source.with_name(f"{source.stem}-generated.md")

    try:
        text = source.read_text(encoding="utf-8")
        result = convert_document(text)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(result, encoding="utf-8")
    except (OSError, ValueError) as exc:
        print(f"ERREUR : {exc}")
        return 2

    print(f"✓ Prétraitement : {source} → {output}")
    print("✓ Front matter Jekyll conservé.")
    print("✓ Markdown standard conservé.")
    print("✓ Blocs CyberRepères convertis selon la structure V3.2.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
