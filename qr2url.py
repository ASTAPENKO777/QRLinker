import qrcode
import cv2


def generate_qr_code(url, filename='qrcode.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR-код збережено як {filename}")

def read_qr_code(filename='qrcode.png'):
    img = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)
    
    if data:
        print(f"Розпізнане посилання: {data}")
    else:
        print("QR-код не розпізнано.")

def main():
    print("1. Згенерувати QR-код з посилання")
    print("2. Розпізнати QR-код")
    choice = input("Виберіть опцію (1/2): ")

    if choice == '1':
        url = input("Введіть посилання: ")
        generate_qr_code(url)
    elif choice == '2':
        filename = input("Введіть назву файлу з QR-кодом (за замовчуванням 'qrcode.png'): ") or 'qrcode.png'
        read_qr_code(filename)
    else:
        print("Невірний вибір.")

if __name__ == "__main__":
    main()
