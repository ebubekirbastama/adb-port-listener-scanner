import subprocess
import re
import requests
import time

def run_adb_command(cmd):
    """adb shell komutunu çalıştırır ve çıktıyı döner."""
    result = subprocess.run(['adb', 'shell'] + cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ADB komutu hata verdi: {' '.join(cmd)}")
        print(result.stderr)
        return None
    return result.stdout

def parse_netstat(output):
    """
    adb shell netstat -a çıktısını parse eder,
    LISTEN (ya da LISTENING) durumundaki TCP portları döner.
    """
    ports = []
    # Windows'da LISTENING olabilir, Linux'da LISTEN
    pattern = re.compile(r'^tcp.*:(\d+)\s+.*(LISTEN|LISTENING)', re.IGNORECASE)
    for line in output.splitlines():
        match = pattern.search(line)
        if match:
            port = match.group(1)
            ports.append(int(port))
    return list(set(ports))  # tekrarları kaldır

def adb_forward(port):
    """adb forward tcp:port tcp:port komutunu çalıştırır."""
    result = subprocess.run(['adb', 'forward', f'tcp:{port}', f'tcp:{port}'], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ADB forward hatası: {result.stderr}")
        return False
    return True

def curl_port(port):
    """Localhost'ta belirtilen porta HTTP GET yapar."""
    url = f"http://localhost:{port}"
    try:
        response = requests.get(url, timeout=5)
        print(f"Port {port} - HTTP {response.status_code}")
        print(response.text[:200])  # İlk 200 karakteri göster
    except Exception as e:
        print(f"Port {port} - HTTP isteği başarısız: {e}")

def main():
    print("ADB ile netstat -a çalıştırılıyor...")
    output = run_adb_command(['netstat', '-a'])
    if not output:
        print("Netstat çıktısı alınamadı.")
        return

    ports = parse_netstat(output)
    if not ports:
        print("Hiç LISTEN portu bulunamadı.")
        return

    print(f"Bulunan LISTEN portları: {ports}")

    for port in ports:
        print(f"\nPort {port} için adb forward ayarlanıyor...")
        if adb_forward(port):
            print(f"Port {port} yönlendirme başarılı, HTTP isteği gönderiliyor...")
            time.sleep(1)  # Kısa bekleme
            curl_port(port)
        else:
            print(f"Port {port} için adb forward başarısız.")

if __name__ == '__main__':
    main()
