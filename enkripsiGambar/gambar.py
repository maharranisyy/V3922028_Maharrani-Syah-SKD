import cv2
import numpy as np

demo = cv2.imread("D:/SEMESTER 3/SISTEM KEAMANAN DATA/enkripsiGambar/Gambar.jpeg", 0)
r, c = demo.shape
key = np.random.randint(0, 256, size=(r, c), dtype=np.uint8)
cv2.imwrite("D:/SEMESTER 3/SISTEM KEAMANAN DATA/enkripsiGambar/KEY-Gambar.jpeg", key)

cv2.imshow("demo", demo)
cv2.imshow("key", key)

encryption = cv2.bitwise_xor(demo, key)
cv2.imwrite("D:/SEMESTER 3/SISTEM KEAMANAN DATA/enkripsiGambar/ENC-Gambar.jpeg", encryption)
decryption = cv2.bitwise_xor(encryption, key)
cv2.imwrite("D:/SEMESTER 3/SISTEM KEAMANAN DATA/enkripsiGambar/DES-Gambar.jpeg", decryption)

cv2.imshow("encryption", encryption)
cv2.imshow("decryption", decryption)

cv2.waitKey(-1)
cv2.destroyAllWindows()

