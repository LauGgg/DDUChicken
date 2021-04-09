from flask import Flask, render_template, request, make_response, jsonify, redirect, session, flash
# from python.EmuControl2 import Emu
from time import sleep

app = Flask(__name__)

# emu = Emu()
# emu.start()
# ids = emu.scanUnits()

# for id in ids:
#     print(str(id))

# emu.wheelMode(5)
# emu.wheelMode(7)

@app.route("/", methods=["GET"])
def home():
    return render_template("door.html")

@app.route("/up", methods=["GET", "POST"])
def door():
    data = request.get_json()
    print(data)
    if data['up']:
        print('den går op')
        # emu.moveWheel(5, - data['speed'])
        # emu.moveWheel(7, data['speed'])
    else:
        print('down')
        # emu.moveWheel(5, data['speed'])
        # emu.moveWheel(7, - data['speed'])  
    if data['secs'] != None and data['secs'] != 0:
        print('venter ', data['secs'], ' sekunder.')
        # sleep(data['secs'])
        # emu.moveWheel(5, 0)
        # emu.moveWheel(7, 0)
    return 'ok'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005, debug=True)
