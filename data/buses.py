from data.routes import load_routes

routes = load_routes()

bus_position = {bus_id: 0 for bus_id in routes}

def generate_buses():
    buses = []

    for bus_id, route in routes.items():
        index = bus_position[bus_id]
        location = route[index]

        buses.append({
            "id": bus_id,
            "lat": location["lat"],
            "lng": location["lng"],
            "speed": 35
        })

        if index < len(route) - 1:
            bus_position[bus_id] += 1
        else:
            bus_position[bus_id] = 0

    return buses
