sudo tlmgr update --self

sudo tlmgr install minted

sudo pip install Pygments

    "latex-workshop.latex.recipes": [
        {
            "name": "pdflatex",
            "tools": [
              "pdflatex"
            ]
        }
    ],
    "latex-workshop.latex.tools": [
        {
            "name": "pdflatex",
            "command": "pdflatex",
            "args": [
                "--shell-escape",
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOC%.tex"
            ]
        }
    ]