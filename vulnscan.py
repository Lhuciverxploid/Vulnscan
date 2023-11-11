import requests
import re
from tqdm import tqdm
from time import sleep

def cek_kerentanan(url):
    print("### Cek Kerentanan ###\n")

    # Cek kerentanan SQL injection
    print("Memeriksa SQL Injection:")
    sleep(1)
    with tqdm(total=10, bar_format="{l_bar}{bar}{r_bar}", leave=False) as pbar:
        for _ in range(10):
            sleep(0.1)
            pbar.update(1)
    pbar.close()

    response = requests.get(url + "' OR 1=1 --")
    if response.status_code == 200:
        print("Kerentanan: SQL injection")
        print("Deskripsi: Kerentanan ini memungkinkan penyerang untuk mengeksekusi kode arbitrer di server web.")
        print("Dampak: Pengungkapan data sensitif, menjalankan kode berbahaya, atau bahkan mengambil alih akun atau situs web.")
        print("Cara Mengatasi:")
        print("- Gunakan prepared statements atau parameterized queries.")
        print("- Validasi dan bersihkan input pengguna.")
        print("- Batasi hak akses pengguna ke database.\n")
    else:
        print("Tidak ditemukan kerentanan SQL injection\n")

    # Cek kerentanan cross-site scripting
    print("Memeriksa Cross-site Scripting:")
    sleep(1)
    with tqdm(total=10, bar_format="{l_bar}{bar}{r_bar}", leave=False) as pbar:
        for _ in range(10):
            sleep(0.1)
            pbar.update(1)
    pbar.close()

    response = requests.get(url + "'><script>alert('Vuln!');</script>")
    if response.status_code == 200:
        print("Kerentanan: Cross-site scripting")
        print("Deskripsi: Kerentanan ini memungkinkan penyerang untuk menjalankan kode JavaScript di browser pengguna.")
        print("Dampak: Menjalankan kode berbahaya, mencuri cookie atau sesi pengguna, atau bahkan menampilkan pesan atau pop-up palsu.")
        print("Cara Mengatasi:")
        print("- Validasi dan bersihkan input pengguna.")
        print("- Implementasikan Content Security Policy (CSP).")
        print("- Encode output sebelum menampilkan ke dalam HTML.\n")
    else:
        print("Tidak ditemukan kerentanan Cross-site scripting\n")

    # Cek kerentanan directory traversal
    print("Memeriksa Directory Traversal:")
    sleep(1)
    with tqdm(total=10, bar_format="{l_bar}{bar}{r_bar}", leave=False) as pbar:
        for _ in range(10):
            sleep(0.1)
            pbar.update(1)
    pbar.close()

    response = requests.get(url + "/../etc/passwd")
    if response.status_code == 200:
        print("Kerentanan: Directory traversal")
        print("Deskripsi: Kerentanan ini memungkinkan penyerang untuk mengakses file-file di luar direktori web.")
        print("Dampak: Pengungkapan data sensitif, menjalankan kode berbahaya, atau bahkan mengubah atau menghapus file-file penting.")
        print("Cara Mengatasi:")
        print("- Gunakan whitelist untuk menentukan file yang dapat diakses.")
        print("- Hindari langsung mengizinkan input pengguna untuk membentuk path file.")
        print("- Batasi hak akses pengguna pada server.\n")
    else:
        print("Tidak ditemukan kerentanan Directory traversal\n")

    # Cek kerentanan parameter manipulation
    print("Memeriksa Parameter Manipulation:")
    sleep(1)
    with tqdm(total=10, bar_format="{l_bar}{bar}{r_bar}", leave=False) as pbar:
        for _ in range(10):
            sleep(0.1)
            pbar.update(1)
    pbar.close()

    response = requests.get(url + "?user=admin&role=user")
    if "role=admin" in response.text:
        print("Kerentanan: Parameter manipulation")
        print("Deskripsi: Kerentanan ini memungkinkan penyerang untuk memanipulasi parameter URL untuk mendapatkan hak akses yang tidak seharusnya.")
        print("Dampak: Pengambilalihan akses, perubahan data pengguna, atau eksekusi tindakan tidak sah.")
        print("Cara Mengatasi:")
        print("- Validasi dan enkripsi parameter yang dikirim melalui URL.")
        print("- Gunakan sesi atau token untuk mengelola hak akses pengguna.\n")
    else:
        print("Tidak ditemukan kerentanan Parameter manipulation\n")

    # Cek kerentanan insecure direct object references (IDOR)
    print("Memeriksa Insecure Direct Object References (IDOR):")
    sleep(1)
    with tqdm(total=10, bar_format="{l_bar}{bar}{r_bar}", leave=False) as pbar:
        for _ in range(10):
            sleep(0.1)
            pbar.update(1)
    pbar.close()

    response = requests.get(url + "/user?id=1")
    if "private_document.pdf" in response.text:
        print("Kerentanan: Insecure Direct Object References (IDOR)")
        print("Deskripsi: Kerentanan ini memungkinkan penyerang untuk mengakses objek atau data yang seharusnya tidak dapat diakses.")
        print("Dampak: Pengungkapan atau perubahan data yang seharusnya bersifat pribadi atau terbatas.")
        print("Cara Mengatasi:")
        print("- Gunakan kontrol akses yang kuat.")
        print("- Jangan gunakan referensi langsung ke objek dalam URL.\n")
    else:
        print("Tidak ditemukan kerentanan Insecure Direct Object References (IDOR)\n")

def ambil_informasi(url):
    print("### Ambil Informasi ###\n")

    # Ambil judul website
    print("Mengambil Judul Website:")
    sleep(1)
    with tqdm(total=10, bar_format="{l_bar}{bar}{r_bar}", leave=False) as pbar:
        for _ in range(10):
            sleep(0.1)
            pbar.update(1)
    pbar.close()

    response = requests.get(url)
    title = re.findall(r'<title>(.*?)</title>', response.text)
    if title:
        print("Informasi: Judul website")
        print(f"Nilai: {title[0]}\n")
    else:
        print("Informasi: Judul tidak ditemukan\n")

    # Ambil deskripsi website
    print("Mengambil Deskripsi Website:")
    sleep(1)
    with tqdm(total=10, bar_format="{l_bar}{bar}{r_bar}", leave=False) as pbar:
        for _ in range(10):
            sleep(0.1)
            pbar.update(1)
    pbar.close()

    description_tag = re.findall(r'<meta name="description" content="(.*?)" />', response.text)
    if description_tag:
        description = description_tag[0]
        print("Informasi: Deskripsi website")
        print(f"Nilai: {description}\n")
    else:
        print("Informasi: Deskripsi tidak ditemukan\n")

    # Ambil kata kunci website
    print("Mengambil Kata Kunci Website:")
    sleep(1)
    with tqdm(total=10, bar_format="{l_bar}{bar}{r_bar}", leave=False) as pbar:
        for _ in range(10):
            sleep(0.1)
            pbar.update(1)
    pbar.close()

    keywords_tag = re.findall(r'<meta name="keywords" content="(.*?)" />', response.text)
    if keywords_tag:
        keywords = keywords_tag[0]
        print("Informasi: Kata kunci website")
        print(f"Nilai: {keywords}\n")
    else:
        print("Informasi: Kata kunci tidak ditemukan\n")

    # Ambil tautan internal website
    print("Mengambil Tautan Internal Website:")
    sleep(1)
    with tqdm(total=10, bar_format="{l_bar}{bar}{r_bar}", leave=False) as pbar:
        for _ in range(10):
            sleep(0.1)
            pbar.update(1)
    pbar.close()

    internal_links = re.findall(r'href=["\'](https?://[^"\'>]+)', response.text)
    if internal_links:
        print("Informasi: Tautan Internal Website")
        for link in internal_links:
            print(f"- {link}")
        print()
    else:
        print("Informasi: Tautan internal tidak ditemukan\n")

    # Ambil tautan eksternal website
    print("Mengambil Tautan Eksternal Website:")
    sleep(1)
    with tqdm(total=10, bar_format="{l_bar}{bar}{r_bar}", leave=False) as pbar:
        for _ in range(10):
            sleep(0.1)
            pbar.update(1)
    pbar.close()

    external_links = re.findall(r'href=["\'](https?://[^"\'>]+)', response.text)
    if external_links:
        print("Informasi: Tautan Eksternal Website")
        for link in external_links:
            print(f"- {link}")
        print()
    else:
        print("Informasi: Tautan eksternal tidak ditemukan\n")

    # Ambil formulir dan input pada halaman web
    print("Mengambil Formulir dan Input pada Halaman Web:")
    sleep(1)
    with tqdm(total=10, bar_format="{l_bar}{bar}{r_bar}", leave=False) as pbar:
        for _ in range(10):
            sleep(0.1)
            pbar.update(1)
    pbar.close()

    forms = re.findall(r'<form.*?</form>', response.text, re.DOTALL)
    if forms:
        print("Informasi: Formulir pada Halaman Web")
        for form in forms:
            print(f"- {form}\n")
    else:
        print("Informasi: Tidak ada formulir ditemukan pada halaman web\n")

def main():
    url = input("Masukkan URL website: ")

    # Cek kerentanan
    cek_kerentanan(url)

    # Ambil informasi
    ambil_informasi(url)

if __name__ == "__main__":
    main()
