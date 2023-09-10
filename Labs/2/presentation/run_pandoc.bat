cd %CD%
pandoc presentation.md -o presentation.pdf --pdf-engine=lualatex -V mainfront="Times New Roman" -V sansfront="DejaVu Sans" -V monofront="DejaVu Sans Mono"