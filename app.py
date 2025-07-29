from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)
kullanicilar = []

@app.route('/')
def index():
    return render_template("index.html", kullanicilar=kullanicilar)

@app.route('/ekle', methods=["POST"])
def ekle():
    yeni_kullanici = request.form.get("kullanici")
    if yeni_kullanici:
        kullanicilar.append(yeni_kullanici)
    return redirect(url_for("index"))

@app.route('/karistir')
def karistir():
    karisik = kullanicilar.copy()
    random.shuffle(karisik)
    return render_template("karistir.html", kullanicilar=karisik)

@app.route('/sec', methods=["POST"])
def sec():
    try:
        sayi = int(request.form.get("sayi"))
        secilen = random.sample(kullanicilar, min(sayi, len(kullanicilar)))
    except:
        secilen = []
    return render_template("sec.html", secilen=secilen)

if __name__ == '__main__':
    app.run(debug=True)
