$(function () {

    // $(".js-create-client").click(function () {
    //   var btn = $(this);
    //   $.ajax({
    //     url: btn.attr('data-url'),
    //     type: 'get',
    //     dataType: 'json',
    //     beforeSend: function () {
    //       $("#newClient").modal("show");
    //     },
    //     success: function (data) {
    //       $("#newClient .modal-content").html(data.html_form);
    //     }
    //   });
    // });

    // $("#newClient").on("submit", ".js-client-create-form", function () {
    //     var form = $(this);
    //     $.ajax({
    //       url: form.attr("action"),
    //       data: form.serialize(),
    //       type: form.attr("method"),
    //       dataType: 'json',
    //       success: function (data) {
    //         if (data.form_is_valid) {
    //           $("#clientList tbody").html(data.client_list);
    //           $("#newClient").modal("hide");
    //         }
    //         else {
    //           $("#newClient .modal-content").html(data.html_form);
    //         }
    //       }
    //     });
    //     return false;
    //   });
  
      var loadForm = function () {
        var btn = $(this);
        console.log(btn.attr("data-url"));
        $.ajax({
          url: btn.attr('data-url'),
          type: 'get',
          dataType: 'json',
          beforeSend: function () {
            $("#newClient").modal("show");
          },
          success: function (data) {
            $("#newClient .modal-content").html(data.html_form);
          }
        });
      };
  
     var saveForm = function () {
          var form = $(this);
          $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
              if (data.form_is_valid) {
                $("#clientList tbody").html(data.client_list);
                $("#newClient").modal("hide");
              }
              else {
                $("#newClient .modal-content").html(data.html_form);
              }
            }
          });
          return false;
        };
    
     /* Binding */

  // Create client
  $(".js-create-client").click(loadForm);
  $("#newClient").on("submit", ".js-client-create-form", saveForm);

  // Update client
  $("#clientList").on("click", ".js-update-client", loadForm);
  $("#newClient").on("submit", ".js-client-update-form", saveForm);

  //Delete client
  $("#clientList").on("click", ".js-delete-client", loadForm);
  $("#newClient").on("submit", ".js-client-delete-form", saveForm);

  //ping client
  $("#monitorTable").on('click', '.js-ping-client', loadForm);
 

$("#monitorTable").on('click', '.js-create-status', function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr('data-url'),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#newClient").modal("show");
        },
        success: function (data) {
          $("#newClient .modal-content").html(data.html_form);
        }
      });
    });

$("#newClient").click(function () {
      var form = $(this);
      console.log(form.attr("action"));
      console.log(form.data);
        $.ajax({
          url: form.attr("action"),
          data: form.serialize(),
          type: form.attr("method"),
          dataType: 'json',
          success: function (data) {
            if (data.form_is_valid) {
              //alert("Status created.")
              $('.alert').alert();
              $("#newClient").modal("hide");
            }
            else {
              $("#newClient .modal-content").html(data.html_form);
            }
          }
        });
        return false;
      });

//pdf
$(".js-pdf-client").click(function () {
  var btn = $(this);
  
  // $.ajax({
  //   url: btn.attr('data-url'),
  //   type: 'get',
  //   dataType: 'json',
  //   beforeSend: function () {
  //     $("#newStatus").modal("show");
  //   },
  //   success: function (data) {
  //     $("#newStatus .modal-content").html(data.html_form);
  //   }
  // });
});

      //create_status_1

  $(".js-create-status").click(function () {
        var btn = $(this);
        $.ajax({
          url: btn.attr('data-url'),
          type: 'get',
          dataType: 'json',
          beforeSend: function () {
            $("#newStatus").modal("show");
          },
          success: function (data) {
            $("#newStatus .modal-content").html(data.html_form);
          }
        });
      });
  
  $("#newStatus").on("submit", ".js-create-status-form-1", function () {
        var form = $(this);
        console.log(form.attr("action"));
        console.log(form.data);
          $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
              if (data.form_is_valid) {
                //alert("Status created.")
                $("#statusTable tbody").html(data.status_list)
                $("#newStatus").modal("hide");
              }
              else {
                $("#newStatus .modal-content").html(data.html_form);
              }
            }
          });
          return false;
        });

      $("#statusTable").on('click', '.js-update-status', function () {
        var btn = $(this);
        $.ajax({
          url: btn.attr('data-url'),
          type: 'get',
          dataType: 'json',
          beforeSend: function () {
            $("#newStatus").modal("show");
          },
          success: function (data) {
            $("#newStatus .modal-content").html(data.html_form);
          }
        });
      });

      $("#newStatus").on("submit", ".js-update-status-form", function () {
        var form = $(this);
          $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
              if (data.form_is_valid) {
                $("#statusTable tbody").html(data.status_list);
                $("#newStatus").modal("hide");
              }
              else {
                $("#newStatus .modal-content").html(data.html_form);
              }
            }
          });
          return false;
        });
  
        $("#statusTable").on('click', '.js-delete-status', function () {
          var btn = $(this);
          console.log(btn.attr('data-url'));
          $.ajax({
            url: btn.attr('data-url'),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
              $("#newStatus").modal("show");
            },
            success: function (data) {
              $("#newStatus .modal-content").html(data.html_form);
            }
          });
        });
  
        $("#newStatus").on("submit", ".js-status-delete-form", function () {
          var form = $(this);
            $.ajax({
              url: form.attr("action"),
              data: form.serialize(),
              type: form.attr("method"),
              dataType: 'json',
              success: function (data) {
                if (data.form_is_valid) {
                  $("#statusTable tbody").html(data.status_list);
                  $("#newStatus").modal("hide");
                }
                else {
                  $("#newStatus .modal-content").html(data.html_form);
                }
              }
            });
            return false;
          });

});