from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    cards = [
        {   
            "id": 1,
            "titulo": "IFNexus",
            "descricao": "O IFNexus é uma vitrine digital desenvolvida para divulgar e valorizar os projetos criados por estudantes e servidores do IFRN.",
            "imagem": "/static/img1.jpg",
            "tag": "Informática",
        },
        {
            "id": 2,
            "titulo": "SIMER",
            "descricao": "Sistema que monitora o consumo de energia em tempo real, identifica os maiores gastos e sugere formas de economizar.",
            "imagem": "/static/img2.jpg",
            "tag": "Eletrotécnica",
        },
        {
            "id": 3,
            "titulo": "EcoFios",
            "descricao": "Projeto voltado à produção de fios ecológicos reutilizando sobras de tecido. Busca reduzir o desperdício na indústria têxtil.",
            "imagem": "/static/img3.jpg",
            "tag": "Têxtil",
        },
        {
            "id": 4,
            "titulo": "Modus",
            "descricao": "Criação de roupas sustentáveis usando materiais ecológicos para reduzir o impacto ambiental da moda.",
            "imagem": "/static/img4.jpg",
            "tag": "Vestuário",
        },
        
    ]
    return render_template('index.html', cards=cards)

if __name__ == '__main__':
    app.run(debug=True)
