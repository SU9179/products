products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    products.append([name, price])
    #[name, price]是下面9~11的縮寫
    #p = []
    #p.append(name)
    #p.append(price)
    #9~11 又可以寫成 p = [name, price]
print(products)
