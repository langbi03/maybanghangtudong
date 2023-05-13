
products = {
  "coca": 10000,
  "pepsi": 10000,
  "bimbim": 10000,
  "nuocloc": 5000
}


money = 0
selected_products = []


print("Danh sách sản phẩm:")
for product, price in products.items():
  print(product, " - Giá tiền:", price)

money = int(input("Vui lòng nhập số tiền của bạn: "))


while True:
  selected_product = input("Vui lòng chọn sản phẩm hoặc nhấn Enter để hoàn tất: ")
  if selected_product == "":
    break
  if selected_product not in products:
    print("Sản phẩm không hợp lệ.")
    continue
  if products[selected_product] > money:
    print("Số tiền không đủ để mua sản phẩm này.")
    continue
  selected_products.append(selected_product)
  money -= products[selected_product]
  print("Bạn đã mua", selected_product)


total = 0
for product in selected_products:
  total += products[product]
print("Số tiền còn lại của bạn là:", money)
if total > 0:
  print("Cảm ơn bạn đã mua hàng. Tổng số tiền:", total)
else:
  print("Không có sản phẩm nào được mua.")
