import requests
import json

url = 'https://3.bp.blogspot.com/_QLg_FohS148/TA9VElq_3xI/AAAAAAAAAWs/fqQe9dIQtxo/s1600/2005_07_21_shrek_cat.jpg' # 'http://i.imgur.com/n9z3sLg.jpg'

# Meio para abrir aquivos pesados
response = requests.get(url, stream=True) # stream=True Realisa o sedido sem descarregar o conteúdo. A conecção continua aberta
with open('image.jpg', 'wb') as file:
    for chunk in response.iter_content(): # descarrega o conteúdo pouco a pouco
        file.write(chunk)


response.close()