from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    cards = [
        {   
            "id": 1,
            "titulo": "Projeto 1",
            "descricao": "Descrição do projeto 1",
            "imagem": "/static/img1.jpg",
            "tag": "Informática",
            "cor_tag": "blue"
        },
        {
            "id": 2,
            "titulo": "Projeto 2",
            "descricao": "Descriçãos do projeto 2",
            "imagem": "/static/img2.jpg",
            "tag": "Eletro",
            "cor_tag": "green"
        },
        {
            "id": 3,
            "titulo": "Projeto 3",
            "descricao": "Descriçãos do projeto 3",
            "imagem": "/static/img3.jpg",
            "tag": "Informatica",
            "cor_tag": "green"
        }
        
    ]
    return render_template('index.html', cards=cards)

if __name__ == '__main__':
    app.run(debug=True)
