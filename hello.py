from flask import Flask
app = Flask(__name__)

pageWeb=["https://www.jeuneafrique.com",
"https://www.cfi.fr/fr/projet/afrique-innovation-entrepreneurs",
"https://www.afrikatech.com","https://startupbrics.com",
"https://www.agenceecofin.com/","https://www.francophonie.org/","https://www.ceoafrique.com",
"https://www.francophonieinnovation.org","https://www.info-afrique.com","http://www.lekiosque-deleco.com",
"https://www.bbc.com/afrique"]


@app.route('/')
def hello_world():
    return 'Hello, Diamilatou!'



@app.route('/site')
def liste_site():
	return str(pageWeb)