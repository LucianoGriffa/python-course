with open("TXT_Archives/notes.txt", encoding="UTF-8") as archive: # Abriendo el archivo con with
  print(archive.read())

# No es necesario cerrarlo con with open