# TradingView Ciya Tester

Bu proje, TradingView stratejilerini test etmek için kullanılan bir araçtır.

## Kurulum

### MacOS için:

1. Python'u yükleyin (Python 3.8 veya üstü önerilir):
```bash
brew install python
```

2. Sanal ortam oluşturun ve aktive edin:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Gerekli paketleri yükleyin:
```bash
pip3 install requests
```

### Windows için:

1. Python'u yükleyin:
   - [Python'un resmi sitesinden](https://www.python.org/downloads/) Python 3.8 veya üstünü indirin
   - Kurulum sırasında "Add Python to PATH" seçeneğini işaretleyin

2. Sanal ortam oluşturun ve aktive edin:
```cmd
python -m venv venv
venv\Scripts\activate
```

3. Gerekli paketleri yükleyin:
```cmd
pip install requests
```

## Kullanım

### MacOS için:
1. Sanal ortamı aktive edin (eğer aktif değilse):
```bash
source venv/bin/activate
```

2. Programı çalıştırın:
```bash
python3 main.py
```

### Windows için:
1. Sanal ortamı aktive edin (eğer aktif değilse):
```cmd
venv\Scripts\activate
```

2. Programı çalıştırın:
```cmd
python main.py
```

## Proje Yapısı

- `main.py`: Ana program dosyası
- `tester.py`: Test fonksiyonlarını içeren modül
- `venv/`: Python sanal ortam dizini
- `.gitignore`: Git tarafından izlenmeyecek dosyaların listesi 