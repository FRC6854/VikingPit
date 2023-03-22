setInterval(function() {
    fetch('/reload')
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            if (data.reload) {
                window.location.reload();
            }
        });
}, 1000);