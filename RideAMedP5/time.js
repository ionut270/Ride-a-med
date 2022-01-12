var time = [0, 0]
// keeps time in check
function updateTime() {
    var passed = Date.now() - time[2];
    time[1] = Math.floor(passed / 1000)
    if (time[1] >= 60) {
        time[2] = Date.now()
        time[0]++;
    }

    if (time[0] >= 24) {
        time[0] = 0;
        time[2] = Date.now()
    }
}