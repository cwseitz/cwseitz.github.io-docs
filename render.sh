for file in `find tex -name "*.tex"`; do 
	#pdflatex --interaction=nonstopmode --output-directory="..${file:3}" $file
	pdflatex --interaction=nonstopmode --output-directory=output/deep-learning $file
done;
