from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = translator.english_to_french('Hello')
    return render_template(textToTranslate, text=textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = translator.french_to_english('Bonjour')
    return render_template(textToTranslate, text=textToTranslate)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
