$(document).ready(function() {
    let speed = 200;
    const upBut = document.querySelector('[data-up]');
    upBut.addEventListener("click", () => {
        if ($("#speed").val() != '') {
            speed = $("#speed").val();
        }
        let query = `${window.origin}/up`;
        let data = {"up": true, "speed": parseInt(speed), "secs": parseInt($("#secs").val())};
        fetch(query, {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(data),
            cache: "no-cache",
            headers: new Headers({
                'content-type': 'application/json'
            })
        })
    });
    const downBut = document.querySelector('[data-down]');
    downBut.addEventListener("click", () => {
        if ($("#speed").val() != '') {
            speed = $("#speed").val();
        }
        let query = `${window.origin}/up`;
        let data = {"up": false, "speed": parseInt(speed), "secs": parseInt($("#secs").val())};
        fetch(query, {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(data),
            cache: "no-cache",
            headers: new Headers({
                'content-type': 'application/json'
            })
        })
    });
    const stopBut = document.querySelector('[data-stop]');
    stopBut.addEventListener("click", () => {
        let query = `${window.origin}/up`;
        let data = {"up": false, "speed": 0, "secs": 0};
        fetch(query, {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(data),
            cache: "no-cache",
            headers: new Headers({
                'content-type': 'application/json'
            })
        })    });
});
