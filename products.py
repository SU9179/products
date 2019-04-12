import os #operating system 作業系統
#讀取檔案
def read_file(filename):#將檔案名設定為參數
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line: #不將標題列出
                continue #continue跟break一樣只能寫在迴圈裡，continue是跳到下一次迴圈的意思
            name, price = line.strip().split(',')
            products.append([name, price])
    return products #return 可以把結果存下來

#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ')
        price = int(price)
        products.append([name, price])
    print(products)
    return products

#印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        #寫入檔案及讀取檔案都會牽涉到語言編碼(encoding)
        #excel 在讀取檔案時若沒有使用UTF-8編碼，中文仍會是亂碼
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')
            # + 只能相同資料型別


def main():
    filename = 'products.csv'
    if os.path.isfile(filename):#os作業系統裡的path模組中的isfile函式用來檢查檔案在不在
        print('找到檔案了')
        products = read_file(filename)
    else:
        print('找不到檔案.....')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()

# refactor 重構程式 