
product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 200000,
        "quantity": 20,
        "sold": 6
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 450000,
        "quantity": 2,
        "sold": 7
    }
]
while True:
    print("====== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY ======")
    print("1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Nhập thêm hàng vào kho")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát chương trình")

    choice = input("Chọn chức năng (1-5): ").strip()

    if choice == "1":
        if not product_list:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("Danh sách sản phẩm hiện tại:")
            for i, product in enumerate(product_list):
                if product["quantity"] == 0:
                    status = "Hết hàng"
                elif product["quantity"] <= 5:
                    status = "Sắp hết hàng"
                else:
                    status = "Còn hàng"
                print(f"{i}. Mã SP: {product['product_id']} | Tên: {product['product_name']} | "
                      f"Giá: {product['price']} | Tồn kho: {product['quantity']} | "
                      f"Đã bán: {product['sold']} | Trạng thái: {status}")

    elif choice == "2":
        input_id = input("Nhập mã sản phẩm khách muốn mua: ").strip().upper()
        found = None
        for product in product_list:
            if product["product_id"] == input_id:
                found = product
                break
        
        if not found:
            print("Không tìm thấy sản phẩm cần bán/nhập kho")
            continue
        quantity_input = input("Nhập số lượng khách mua: ").strip()

        if not quantity_input.isdigit() or int(quantity_input) <= 0:
            print("Số lượng mua/nhập kho không hợp lệ")
            continue
            
        buy_quantity= int(quantity_input)
        
        # Bẫy 4: Nhập số lượng mua vượt quá tồn kho
        if buy_quantity > found["quantity"]:
            print("Số lượng trong kho không đủ bán")
            continue
            
        # Xử lý hợp lệ: Cập nhật hệ thống
        found["quantity"] -= buy_quantity
        found["sold"] += buy_quantity
        total_payment = buy_quantity * found["price"]
        print(f"Bán hàng thành công! Tổng số tiền khách cần thanh toán: {total_payment} VNĐ")

    elif choice == "3":
        input_id = input("Nhập mã sản phẩm cần nhập thêm: ").strip().upper()

        found= None
        for product in product_list:
            if product["product_id"] == input_id:
                found = product
                break
                
        if not found:
            print("Không tìm thấy sản phẩm cần bán/nhập kho")
            continue

        quantity_input = input("Nhập số lượng nhập thêm: ").strip()

        if not quantity_input.isdigit() or int(quantity_input) <= 0:
            print("Số lượng mua/nhập kho không hợp lệ")
            continue
            
        quantity = int(quantity_input)

        found["quantity"] += quantity
        print(f"Nhập hàng thành công! Đã thêm {quantity} sản phẩm vào mã {input_id}.")

    elif choice == "5":
        print("Thoát chương trình. Sau đó dừng chương trình.")
        break