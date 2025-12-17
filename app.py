from flask import Flask, render_template, request, redirect, jsonify
from users import users
from data.buses import generate_buses
from data.routes import load_routes
import math

app = Flask(__name__)

routes = load_routes()

# ---------------- LOGIN ----------------

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            return redirect("/dashboard")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# ---------------- API ----------------

@app.route("/api/buses")
def buses():
    return jsonify(generate_buses())
@app.route("/api/route/<bus_id>")
def route(bus_id):
    route = routes.get(bus_id)
    if not route:
        return jsonify([])
    return jsonify(route)

@app.route("/api/eta/<bus_id>")
def eta(bus_id):
    route = routes.get(bus_id)
    if not route:
        return jsonify([])

    bus_lat = route[0]["lat"]
    bus_lng = route[0]["lng"]
    speed = 35

    eta_list = []

    for stop in route[1:]:
        distance = math.sqrt(
            (bus_lat - stop["lat"]) ** 2 +
            (bus_lng - stop["lng"]) ** 2
        ) * 111

        eta_list.append({
            "stop": stop["name"],
            "eta": round((distance / speed) * 60, 2)
        })

    return jsonify(eta_list)

# ---------------- RUN ----------------
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

