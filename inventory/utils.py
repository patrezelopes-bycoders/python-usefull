def discount(sales, purchases):
    "some business rule"
    total_sales = 0
    total_purchases = 0
    for sale in sales:
        if sale.product.pk == 1:
            sale.price = 0
            sale.save()
        if sale.product.pk == 2:
            sale.price = sale.prince * (1 - 0.10)
            sale.save()
            total_sales += sale.price

    for purchase in purchases:
        if purchase.product.pk == 3:
            purchase.price = 0
            purchase.save()
        if purchase.product.pk == 10:
            purchase.price = sale.prince * (1 - 0.10)
            purchase.save()
            total_purchases += purchase.price

    return total_sales, total_purchases