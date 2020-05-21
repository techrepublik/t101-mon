$(document).ready(function(){
    //new client
    $('.show-form').click(function(){
        $.ajax({
            url: '/clients/new/',
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#newClient').modal('show');
            },
            success: function(data){
                $('#newClient .modal-content').html(data.html_form);
            }
        });
    });

    $('#newClient').on('submit', '.client-form', function(){
        var form = $(this);
        var dataId = $(this).data('pk');
        $.ajax({
            url: 'clients/' + dataId + '/edit/',
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function(data){
                if (data.form_is_valid){
                    console.log('Save successfully');
                    $('#clientList tbody').html(data.client_list);
                    $('#newClient').modal('hide');
                } else {
                    $('#newClient .modal-content').html(data.html_form);
                }
            }
        });
        return false
    });

    //update client
    $('.show-form-update').click(function(){
        var form = $(this);
        console.log(form.attr('data-url') + ' - ok');
        $.ajax({
            url: form.attr('data-url'),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#newClient').modal('show');
            },
            success: function(data){
                $('#newClient .modal-content').html(data.html_form);
            }
        });
    });

    //get client
    $('.show-form-get').click(function(){
        var form = $(this);
        console.log(form.attr('data-url') + ' - ok');
        $.ajax({
            url: form.attr('data-url'),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#newClient').modal('show');
            },
            success: function(data){
                $('#newClient .modal-content').html(data.html_form);
            }
        });
    });
});

        
