cd %CD%
pandoc report.md -o report.pdf --pdf-engine=lualatex -V mainfront="Times New Roman" -V sansfront="DejaVu Sans" -V monofront="DejaVu Sans Mono"