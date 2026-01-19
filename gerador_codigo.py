import qrcode

#definindo a base da url
base_url = "seu link profissional aqui"

#solicitando o id da página
final_id = input("Digite o ID da página: ")

#juntando os dois
f_string = f"{base_url}{final_id}"

#caminho para salvar o arquivo
file_path = r"C:\\Users\\ferna\\Desktop\\GUSTAVO\\Santander Bootcamp\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(f_string)
img = qr.make_image()
img.save(file_path)

print("QR CODe was generated!")