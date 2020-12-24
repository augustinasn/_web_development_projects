from flask import render_template
from ocr_app import app
from ocr_app.forms import UploadFile
from ocr_app.functions import detect_text, save_img, parse_text


@app.route("/", methods=["GET", "POST"])
def main():
    form = UploadFile()

    if form.validate_on_submit():
        if form.picture.data:
            file = form.picture.data
            fn, fp = save_img(app, file)
            texts = detect_text(fp)
            output = parse_text(texts)

        return render_template("main.html",
                            title="Pagrindinis",
                            form=form,
                            output=output,
                            fn=fn)

    return render_template("main.html",
                           title="Pagrindinis",
                           form=form)