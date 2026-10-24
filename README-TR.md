# Afife Batur Library Status Checker
!!! Şuan bazı buglar var en yakın zamanda düzelticem
son zamanlarda afife batur kütüphanesine giderken sistem sürekli çöküyor ve rezervasyon alamıyorum. Zaten bi rezervasyon alma yarışı var hemen dolduğu için sistem geldiğinde hemen öğrenmek istiyordum. Sistem geldiğinde bilgisayarıma mesaj olarak sistem geldi diye mesaj gönderen bi kod yazdım, isterseniz kullanabilirsiniz

# Nasıl çalışıyor?
- Rezervasyon sitesini otomatik açıyor
- Giriş ekranı çıkarsa koda sizin yazacağınız kullanıcı ve şifreyi giriyor (bunu altta nasıl yapacağınız yazıyor)
- Afife Batur alabileceğiniz kütüphanelerde var mı diye bakıyor
- var ise bildirim geliyo
- yok ise her 60 saniye sayfayı yeniliyo

# Kullanıcı ad ve şifre ayarlama   !!! ÖNEMLİ !!!

dosyadaki .env dosyasını açın ve ibb kutuphane sistemine girerken kullandığınız kullanıcı adı ve şifrenizi yazın


## Nasıl Kurulur ve Çalıştırılır?

1. Projeyi indirin

- Yeşil Code butonuna basın.
- Download ZIP seçeneğine tıklayın.
- İndirilen ZIP dosyasına sağ tıklayıp Tümünü Ayıkla seçeneğini seçin.
- Ayıklanan klasörü açın.

2. Python

Bilgisayarınızda Python kurulu değilse https://www.python.org/downloads/ adresinden indirin.

Windows kullanıyorsanız kurulum sırasında Add Python to PATH seçeneği görünürse işaretleyin.

3. Gerekli dosyaları hazırlayın

- Proje klasörünün içindeki .env dosyasını açın.
- LIBRARY_USERNAME karşısına İBB kütüphane sistemindeki kullanıcı adınızı, LIBRARY_PASSWORD karşısına şifrenizi yazın.
- Dosyayı kaydedin.

4. Kurulum komutlarını çalıştırın

- Proje klasörünü açın.
- Klasörün içindeki boş bir alana sağ tık yapın ve "Terminalde aç" tıklayın
- Aşağıdaki komutu yazıp Enter'a basın:

python -m pip install -r requirements.txt

- Kurulum tamamlanınca şu komutu da çalıştırın:

python -m playwright install chromium

5. Programı başlatın

not (her başlatmak istediğinizde dosyaya gidip sağ tık terminal aç yapmanız lazım)

Aynı siyah pencereye şu komutu yazıp Enter'a basın:

python main.py

Program çalışmaya başlayacak ve rezervasyon sitesini kontrol etmek için bir tarayıcı açacaktır. Programın çalışmaya devam etmesi için siyah pencereyi ve tarayıcıyı kapatmayın.

Not: Program Afife Batur Kütüphanesi'nin adını sayfada bulduğunda bildirim gönderir.
winotify nedeniyle bildirim özelliği sadece Windows içindir.
