from flask import Flask, url_for

app = Flask(__name__)


@app.route("/") 
@app.route("/home")
def home_page():
    return f"""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Магозин</title>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
          <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
        </head>
        <body>
            <header>
                <ul class="nav nav-tabs">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="index.html">Главная</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="1.html">Хлебобулочные изделия</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="2.html">Кисломолочные продукты</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="3.html">Мясо</a>
                    </li>
                </ul>
            </header>


          <div class="container">
              <div class="row mt-5">
                <h1 class="text-center mt-5 mb-5">Планеты Солнечной системы</h1>
                <div class="row justify-content-center">
                  <div class="col-md-4">
                    <ul class="list-group">
 
                    </ul>
                  </div>
                </div>
            </div>
          </div>
        </body>
        </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug = True)