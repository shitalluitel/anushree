$('body').on('change', '#id_item', function () {
    var item = $(this).children('option:selected').val();
    var detail = $('#product-detail');

    if (item != '') {
        $.ajax({
            url: '/api/products/tube/' + item + '/',
            error: function () {
                console.log("error");
            },
            success: function (data) {
                for (i in data) {
                    $('#' + i).empty();
                    $('#' + i).append(data[i]);
                }
            },
            type: 'GET'
        });
    }
});


