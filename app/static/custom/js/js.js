$(document).ready(function () {
    // click on button submit
    $("#submit-create-team").on('click', function () {
        // send ajax
        //     url: , // url where to submit the request
        $.ajax('/team/preview/', {
            type: "POST", // type of action POST || GET
            //dataType: 'json', // data type
            data: $("#create_team").serialize(), // post data || get data
            success: function (result) {
                // you can see the result from the console
                // tab of the developer tools
                console.log(result);
                document.body.innerHTML = result;
            },
            error: function (xhr, resp, text) {
                console.log(xhr, resp, text);
            }
        })
        // Team preview
    });

    $("#create_team").on('submit', function (e) {
        e.preventDefault();
        // Create team
        //$.ajax();
        $.ajax('/team/create', {
            type: "POST", // type of action POST || GET
            //dataType: 'json', // data type
            data: $("#create_team").serialize(), // post data || get data
            success: function (result) {
                // you can see the result from the console
                // tab of the developer tools
                console.log(result);
                document.body.innerHTML = result;
            },
            error: function (xhr, resp, text) {
                console.log(xhr, resp, text);
            }
        });
        return false;
    })
});