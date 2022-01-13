var unit = 800;
var cell_size = 10;

function normalizeLongLat(lat, long) {
    var avg = 10;
    var n_percent = avg * 2 / 100;
    var s_percent = unit / 100;

    return [((lat + avg) / n_percent) * s_percent, ((long + avg) / n_percent) * s_percent]
}

var vehicles = []

// for this problem i dont need classed as Objects work as classes anyhow
function setup() {
    time.push(Date.now()); // time[3] will be start timestamp

    calculate_solution();

    for (var i in data.vehicles) {
        data.vehicles[i].now = data.places[data.vehicles[i].start]
    }

    for (var i in data.patients) {
        data.patients[i].now = data.places[data.patients[i].start]
    }

    createCanvas(unit, unit);
}

function draw() {
    updateTime();

    background(220);
    fill(256, 256, 256);
    for (var place of data.places) {
        let coord = normalizeLongLat(place.lat, place.long)
        rect(coord[0], coord[1], cell_size, cell_size);
    } // map is static

    for (var vehicle of data.vehicles) {
        let place = vehicle.now
        let coord = normalizeLongLat(place.lat, place.long)

        fill(0, 256, 0);
        rect(coord[0] + 2.5, coord[1] + 2.5, cell_size / 2);
    }

    for (var patient of data.patients) {
        let place = patient.now
        let coord = normalizeLongLat(place.lat, place.long)

        fill(0, 0, 0);
        textSize(10);
        text(`${patient.id}:${patient.category}`, coord[0] + 2.5 - cell_size, coord[1] + 2.5 - cell_size);
        fill(256, 0, 0);
        rect(coord[0] + 2.5, coord[1] + 2.5, cell_size / 2);
    }

    fill(0, 0, 0);
    textSize(16);
    text(`${time[0]}h${time[1]}m`, unit / 2, 30);
}
