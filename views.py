import requests
import time

# By royz
print("\033[92m**************************************")
print("*   WEB SİTE GÖRÜNTÜLEME KASICI \033[93mV3.0\033[92m *")
print("*\033[96m  Create By ROYZ İNSTA EXE.ROYZ   \033[92m  *")
print("**************************************")

url = input("\033[96m[\033[93m+\033[96m] \033[93mWeb Site Link Giriniz\033[91m: ")
interval = 0.1  # By royz

while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("\033[96m[\033[93m+\033[96m] Başarılı geçti\033[93m!")
        else:
            print(f"Hata kodu: {response.status_code}")
    except Exception as e:
        print(f"Hata: {e}")

    time.sleep(interval)