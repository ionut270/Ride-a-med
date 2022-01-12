function calculate_solution() {
    // add distance from dest to time it has
    // sort patients by this number

    // we must keep in mind location of ambulances
    // so dist from ambulance to patient + dist from ambulance to dest

    // if time allows it pick up patients on the way
    // No point in picking up patients that have at least 1 hour to spare

    // sort patients by appointment
    for(var i in data.patients){
        for(var j in data.patients){
            if(
                parseInt(data.patients[i].rdvDuration.split(/h/)[0]) < parseInt(data.patients[j].rdvDuration.split(/h/)[0]) ||
                (
                    parseInt(data.patients[i].rdvDuration.split(/h/)[0]) ===    parseInt(data.patients[j].rdvDuration.split(/h/)[0]) &&
                    parseInt(data.patients[i].rdvDuration.split(/h/)[1]) <      parseInt(data.patients[j].rdvDuration.split(/h/)[1])
                )
            ){
                let aux = data.patients[j];
                data.patients[j] = data.patients[i]
                data.patients[i] = aux;
            }
        }
    }
    // solutie recursiva

    // daca am reusit sa iau toti pacientii pana la final de zi => solutie
    // daca am pacienti ramasi, alege solutia cu numarul cel mai mic de pacienti ramasi
}