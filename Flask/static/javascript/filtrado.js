$(document).ready(function(){
    //$ funciona para seleccionar elementos del html
    // se usa para que se ejecute cuando el documento este listo
    $(".buttons button").click(function(){
        var card=$(this).attr("category")
        console.log(card);
        //era para ver si al apretar el boton leia la categorya, pero es inesesario. Si quieren saquen el console.log()

        $(".my-custom-card").hide();
        // selecciona todos los elementos .my-custom-card y los oculta con .hide()
        
        if (card === "todo") {
            $('.my-custom-card').show();
         } else{
            $('.my-custom-card[category="' + card + '"]').show();  
        }
    })
})

