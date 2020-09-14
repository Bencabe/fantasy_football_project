function changeTemplate(clicked) {
    $("#page-content").load('/draft/change_template/' + clicked)
}

function changeTemplateLeagues(clicked) {
    let league = document.getElementById('select-league-dropdown').value
    $("#page-content").load('/draft/change_template_leagues/' + clicked +'/'+ league)
}

// $(document).ready( function() {
//     $("#public_league").on("click", function() {
//         $("#page-content").load('/draft/change_template');

//     });
// });