def priceCheck(products,productPrices,productSold,soldPrices):
    error_count = 0
    for i in range(len(productSold)):
        sold_price = soldPrices[i]
        if productSold[i] in products:
            original_price = productPrices[products.index(productSold[i])]
            if original_price !=sold_price:
                error_count = error_count+1
    return error_count


products = ['eggs','milk','cheese']
productPrices = [2.89,3.29,5.79]
productSold = ['eggs','eggs','cheese','milk']
soldPrices = [2.89,2.99,5.99,3.29]
x = priceCheck(products,productPrices,productSold,soldPrices)
print(x)