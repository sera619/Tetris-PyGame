run:
	python .\main.py

build:
	pyinstaller .\main.spec

clean:
	if exist "./build" rd /s /q build
	if exist "./dist" rd /s /q dist
	if exist "./src/__pycache__" rd /s /q .\src\__pycache__