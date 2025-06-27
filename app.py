from flask import Flask, jsonify, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/noticias')
def get_noticias():
     url ='https://g1.globo.com/'
     response = requests.get(url)
     soup = BeautifulSoup(response.text, 'html.parser')


     noticias = []

     blocos = soup.select('a.feed-post-link')
     print(f"Quantidade de blocos encontrados: {len(blocos)}")

    

     for bloco in blocos[:10]: 
        titulo = bloco.get_text(strip=True)
        print(f"Título: {titulo}")
        link = bloco['href']
        noticias.append({'titulo': titulo, 'link': link})


        
        with open('noticias.txt', 'w', encoding='utf-8') as f:
            for noticia in noticias:
                f.write(f"{noticia['titulo']} - {noticia['link']}\n")

     print(noticias)

     return render_template('noticias.html', noticias=noticias)
            
            

            
if __name__ == '__main__':
             print("Servidor Iniciado")
             app.run(debug=True)
