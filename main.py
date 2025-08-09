import cv2

img = cv2.imread("images.jpeg")
if img is None:
    print("No se pudo cargar la imagen.")
else:
    # Invertir horizontalmente (flipCode=1)
    img_invertida = cv2.flip(img, 0)
    cv2.imwrite("copia_invertida_vertical.jpeg", img_invertida)
    print("Imagen invertida guardada como copia_invertida_vertical.jpeg")
