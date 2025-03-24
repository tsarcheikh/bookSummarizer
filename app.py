from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://hook.eu2.make.com/woto9wm3v7oeeqr76f36rj37mndvuw3b"  # Remplace par ton URL de webhook

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = {
            "book_title": request.form['book_title'],
            "language": request.form['language'],
            "summary_type": request.form['summary_type'],
            "email": request.form['email']
        }

        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 200:
            return jsonify({"success": True, "message": "Données envoyées avec succès !"})
        else:
            return jsonify({"success": False, "message": "Erreur lors de l'envoi au webhook."}), 500

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)