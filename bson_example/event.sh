#! /bin/sh

#pygmentize -f svg -P "style=monokai" -P "fontfamily='Cantarell, sans-serif;'" event.json | xmllint --format - > event.svg
pygmentize -f svg -P "style=fruity" -P "fontfamily='Cantarell, sans-serif;'" event.json | xmllint --format - > event.svg
sed -i -e 's/&#160;&#160;&#160;&#160;/GRUIK/g' event.svg
sed -i -e 's/GRUIK/\&#160;/g' event.svg
sed -i -e 's/fb660a/ffb13b/g' event.svg
sed -i -e 's/ffffff/e9ebaa/g' event.svg
#sed -i -e 's/err/s2/g' event.tex
