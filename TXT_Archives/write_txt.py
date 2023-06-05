with open("TXT_Archives/notes.txt", 'w',encoding="UTF-8") as archive: # Abriendo el archivo con with.
  archive.write('YouTuber: Soy Dalto. Llamado Lucas Dalto. \n') #  Con write, podemos sobreescribir el archivo.
  archive.writelines(['El Youtuber:', '\n' '- Soy Dalto']) # Con writelines, no se sobreescribe el archivo.
  for i in range(5): archive.writelines(f"\nLinea {i+1} agregada.")