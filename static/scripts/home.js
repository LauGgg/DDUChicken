$(document).ready(function() {
    let date = new Date();
    const monthNames = ["Januar", "Februar", "Marts", "April", "Maj", "Juni", "Juli", "August", "September", "Oktober", "November", "December"];
    $('[data-date]').html(date.getDate() + ' ' + monthNames[date.getMonth()]);   
});