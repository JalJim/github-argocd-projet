from flask import Flask, render_template_string

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template_string("""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HEH Projet - Maroc</title>
    <style>
        /* Reset pour enlever les marges par défaut */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            /* Permet de centrer le contenu verticalement et horizontalement */
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

            /* LE FOND STYLE ROUGE ET VERT */
            /* Utilisation d'un dégradé linéaire en diagonale pour un look moderne */
            background: linear-gradient(135deg, #c1272d 0%, #c1272d 50%, #006233 50%, #006233 100%);
            /* Alternative plus douce : décommentez la ligne suivante si vous préférez un mélange */
            /* background: linear-gradient(45deg, #c1272d, #006233); */
            
            color: white; /* Texte en blanc pour le contraste */
        }

        /* Le conteneur principal qui ressemble à une carte */
        .content {
            text-align: center;
            background: rgba(0, 0, 0, 0.5); /* Fond noir semi-transparent pour faire ressortir le texte */
            padding: 40px;
            border-radius: 20px; /* Bords arrondis */
            box-shadow: 0 15px 35px rgba(0,0,0,0.4); /* Ombre portée pour l'effet 3D */
            max-width: 800px;
            width: 90%; /* Responsive sur mobile */
            border: 2px solid rgba(255, 255, 255, 0.1);
        }

        h1 {
            font-size: 3.5rem;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 2px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }

        /* Style du conteneur vidéo */
        .video-container {
            margin: 30px 0;
            position: relative;
            border-radius: 15px;
            overflow: hidden; /* Pour que la vidéo suive les bords arrondis */
            border: 4px solid white;
            box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        }

        /* La vidéo elle-même */
        video {
            width: 100%;
            height: auto;
            display: block;
            max-height: 400px; /* Hauteur max pour ne pas prendre tout l'écran */
            object-fit: cover; /* Remplit bien le cadre */
        }

        /* Style des noms */
        .names p {
            font-size: 1.8rem;
            font-weight: bold;
            margin: 10px 0;
            background: rgba(255, 255, 255, 0.1);
            display: inline-block;
            padding: 5px 20px;
            border-radius: 50px;
        }

        /* Petit effet au survol des noms */
        .names p:hover {
            background: white;
            color: #c1272d;
            transition: 0.3s ease;
        }

    </style>
</head>
<body>
    <div class="content">
        <h1>HEH Projet</h1>

        <div class="video-container">
            <video controls autoplay muted loop>
                <source src="maroc_edit.mp4" type="video/mp4">
                Votre navigateur ne supporte pas la balise vidéo.
            </video>
        </div>
        
        <div class="names">
            <p>Tricarico</p>
            <p>Adam</p>
        </div>
    </div>
</body>
</html>
""")


if __name__ == "__main__":
    app.run(debug=True)
