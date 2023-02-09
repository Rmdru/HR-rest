from __main__ import Flask, send_file, render_template, request, app
from flask_qrcode import QRcode

qrcode = QRcode(app)


@app.route("/qr")
def qr():
    return render_template("qrcode.html")


@app.route("/qrcode", methods=["GET"])
def get_qrcode():
    # please get /qrcode?data=<qrcode_data>
    data = request.args.get("data", "")
    return send_file(qrcode(data, mode="raw"), mimetype="image/png")
