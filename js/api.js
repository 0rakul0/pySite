$("document").ready(function(){
    $("#btn_submit").click(function(){
      
        var peso = parseFloat($("#inp_peso").val());
        var altura = parseFloat($("#inp_altura").val());

        $.ajax({
            url: "https://0rakul0.pythonanywhere.com/api",
            type: "POST",
            contentType: "application/json",
          
            data: JSON.stringify({
                "peso": peso,
                "altura": altura
            }),

        }).done(function(data){
            $("h1").html("IMC: "+ data["resultado"]);
        });
    });
});