def total_carrito(request):
    Total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                Total += value["acumulado"]
    return {"total_carrito": Total}