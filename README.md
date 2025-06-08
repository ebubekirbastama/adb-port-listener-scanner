
📱🔍 ADB Port Listener Scanner
==============================

Bu araç, ADB (Android Debug Bridge) ile bağlı Android cihazınızda çalışan servisleri bulur ve test eder. 
🛠️ Geliştiriciler ve güvenlik uzmanları için idealdir.

🎯 Amaç
--------
🔎 Android cihazda çalışan servisleri tespit etmek  
🔁 Portları yerel makinenize yönlendirmek (`adb forward`)  
🌐 HTTP tabanlı servisleri test etmek  

🚀 Nasıl Kullanılır?
---------------------
1️⃣ Android cihazınızı USB ile bağlayın  
2️⃣ `adb devices` komutu ile cihazın göründüğünden emin olun  
3️⃣ Python ortamınızda gerekli kütüphaneyi yükleyin:

   ```
   pip install requests
   ```

4️⃣ Uygulamayı çalıştırın:

   ```
   python adb_port_scanner.py
   ```

⚙️ Ne Yapar?
-------------
📡 `adb shell netstat -a` ile cihazdaki portları listeler  
🎧 `LISTEN` veya `LISTENING` durumundaki TCP portları ayıklar  
🔁 Her port için `adb forward tcp:PORT tcp:PORT` çalıştırır  
🌐 `http://localhost:PORT` adresine HTTP GET isteği gönderir  
📄 HTTP yanıt kodunu ve ilk 200 karakteri terminalde gösterir  

⚠️ Uyarılar
-------------
⚠️ Portların hepsi HTTP servisi olmayabilir  
⚠️ Cihazınızda `netstat` komutu yoksa çalışmaz  
⚠️ ADB bağlantısının stabil olması gerekir  

👨‍💻 Geliştirici
-----------------
🧑 Ebubekir bastama
🌐 GitHub: https://github.com/ebubekirbastama/

📜 Lisans
----------
 MIT License – Özgürce kullanabilir, dağıtabilirsiniz.

🔚 Keyifli testler! 🔍📲
