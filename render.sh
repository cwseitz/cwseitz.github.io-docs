for file in `find tex -name "*.tex"`; do 	
	echo "Rendering $file";
	pdflatex --interaction=nonstopmode --output-directory=output $file
done;
