#첫 번째 실습
def check_and_clear(box):
    if '불량품' in box.key:
        print('불량품이 있으면 box를 clear합니다.')
        box.clear()

#두 번째 실습
products = {'풀':800, '딱풀':1200, '색종이':1000, '색연필':5000, '스케치북':3500}
catalog = {'겨울용 실내화':12000, '잠자리채':8000, '딱풀':1400}

products.update(catalog)

print(products)