FUENTES = programas/programa1.py programas/programa2.py programas/programa3.py \
programas/programa4.py programas/programa5.py integrantes.txt


entrega: $(FUENTES) Makefile
	rm -f lab1.tar.gz
	tar -cvf lab1.tar $(FUENTES)
	gzip lab1.tar