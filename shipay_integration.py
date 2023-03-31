import requests
from PIL import Image
import qrcode
import base64
import io
from io import BytesIO
from PIL import Image, ImageTk

auth_data = {
    "access_key": "R7Qq5vHQZBsiHr5e6KT4Ag",
    "client_id": "iUDw0RHjGOKlxwBoXTIlGFVaOR2_4HOhmn-FKL4zSQKc-npYpk8oYwfKqiBU9u1r9Kueer4yuvt1tj6vF8p_6-mwbn9lWC-BiVW1M7zqViIs3-HP3UG9Ql0qZATV6Ogun5gx9i_tMCt3EgUusnbzPjPnGJoJMyTDOj20uaDsKr0",
    "secret_key": "xX24xeAmO16hk-GWaRyL8Vkyco6_LymcPCmpk-KXemUHwIrRf7kzdQTUGgagn5M8V5oSF6oUqzWa408_TGvTeg",
}


def create_order():
    # Autentica na API da Shipay
    auth_response = requests.post("https://api.shipay.com.br/pdvauth", json=auth_data)
    if auth_response.status_code == 200:
        token = auth_response.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        # Cria um pedido na API da Shipay
        order_data = {
            "buyer": {
                "cpf_cnpj": "04497425398",
                "email": "rob.dias@gmail.com",
                "name": "Roberto Dias",
                "phone": "(11) 99999-9999",
            },
            "items": [
                {
                    "ean": "0123456789012",
                    "item_title": "batata doce",
                    "quantity": 1,
                    "sku": "MTC-6110",
                    "unit_price": 10,
                }
            ],
            "order_ref": "pedido-qualquer-123",
            "total": 10,
            "wallet": "pix",
        }
        order_response = requests.post(
            "https://api.shipay.com.br/order", json=order_data, headers=headers
        )
        print("Order response:", order_response.json())

        # Retorna o ID do pedido e o texto do QR Code, caso tenha sido criado com sucesso
    if order_response.status_code == 200:
        order_data = order_response.json()
        order_id = order_data.get("order_id")
        qr_code_data_uri = order_data.get("qr_code")
        qr_code_base64 = qr_code_data_uri.split(",")[1]  # Altere esta linha
        return order_id, qr_code_base64
    else:
        return None, None


def generate_qr_code():
    order_id, qr_code_base64 = create_order()

    if qr_code_base64 is None:
        print("Error: QR code data not found")
        return None

    qr_code_data = base64.b64decode(qr_code_base64)
    image_data = io.BytesIO(qr_code_data)
    img = Image.open(image_data)
    return img
