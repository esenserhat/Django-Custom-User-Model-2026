# Django Custom User Model Project

This project demonstrates how to implement a custom user model in Django, providing a flexible and extensible authentication system for your web applications.

---

# Django Özel Kullanıcı Modeli Projesi

Bu proje, Django'da özel kullanıcı modeli (custom user model) oluşturmayı ve esnek, genişletilebilir bir kimlik doğrulama sistemi kurmayı göstermektedir.

---

## Purpose / Amaç

**EN:**
The main goal of this project is to show how to:
- Replace Django's default user model with a custom user model (`Account`)
- Add additional fields (such as full name, department, title, phone, photo, etc.)
- Use a custom user manager for user and superuser creation
- Integrate the custom user model with Django's authentication, admin, and password reset workflows

**TR:**
Bu projenin temel amacı:
- Django'nun varsayılan kullanıcı modelini özel bir modelle (`Account`) değiştirmek
- Ek alanlar eklemek (ad-soyad, departman, unvan, telefon, fotoğraf vb.)
- Kullanıcı ve süper kullanıcı oluşturmak için özel bir user manager kullanmak
- Özel kullanıcı modelini Django'nun kimlik doğrulama, admin ve şifre sıfırlama süreçlerine entegre etmek

---

## Features / Özellikler

**EN:**
- Custom user model (`Account`) with email as the unique identifier
- Department and Title models for user categorization
- User profile fields: full name, photo, department, title, phone numbers
- Admin integration for managing users and related models
- Password reset and change functionality
- English UI and email templates

**TR:**
- E-posta ile giriş yapılan özel kullanıcı modeli (`Account`)
- Kullanıcı kategorileri için Departman ve Unvan modelleri
- Kullanıcı profili alanları: ad-soyad, fotoğraf, departman, unvan, telefonlar
- Kullanıcı ve ilişkili modelleri yönetmek için admin paneli entegrasyonu
- Şifre sıfırlama ve değiştirme fonksiyonu
- İngilizce arayüz ve e-posta şablonları

---

## Project Structure / Proje Yapısı

```
├── app_auth/           # Custom user app (models, forms, admin, views) / Özel kullanıcı uygulaması
├── main/               # Main Django project settings and URLs / Ana Django proje ayarları ve URL'ler
├── templates/          # HTML templates (auth, profile, password reset, etc.) / HTML şablonları
├── assets/             # Static files (CSS, JS, images) / Statik dosyalar
├── requirements.txt    # Python dependencies / Python bağımlılıkları
├── manage.py           # Django management script / Django yönetim komutu
```

---

## Quick Start / Hızlı Başlangıç

**EN:**
1. **Clone the repository**
2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
3. **Apply migrations**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. **Create a superuser**
   ```
   python manage.py createsuperuser
   ```
5. **Run the development server**
   ```
   python manage.py runserver
   ```
6. **Access the app**
   - User login, registration, and profile management
   - Admin panel: `/admin`

**TR:**
1. **Depoyu klonlayın**
2. **Bağımlılıkları yükleyin**
   ```
   pip install -r requirements.txt
   ```
3. **Veritabanı migrasyonlarını uygulayın**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. **Süper kullanıcı oluşturun**
   ```
   python manage.py createsuperuser
   ```
5. **Geliştirme sunucusunu başlatın**
   ```
   python manage.py runserver
   ```
6. **Uygulamaya erişin**
   - Kullanıcı girişi, kayıt ve profil yönetimi
   - Admin paneli: `/admin`

---

## Custom User Model Overview / Özel Kullanıcı Modeli Özeti

**EN:**
- Located in `app_auth/models.py`
- Uses `email` as the login field (`USERNAME_FIELD`)
- Additional fields: `full_name`, `photo`, `department`, `title`, `phone_gsm`, `phone_internal`, etc.
- Related models: `Department`, `Title`

**TR:**
- `app_auth/models.py` dosyasında yer alır
- Giriş alanı olarak `email` kullanır (`USERNAME_FIELD`)
- Ek alanlar: `full_name`, `photo`, `department`, `title`, `phone_gsm`, `phone_internal` vb.
- İlişkili modeller: `Department`, `Title`

---

## LoginView and normalize_email

**EN:**
- `LoginView` is a Django class-based view that handles user login with email and password.
- It includes brute-force protection by limiting login attempts and blocking further attempts for 5 minutes after 5 failed tries.
- The `normalize_email` function converts Turkish characters in the email to their Latin equivalents and lowercases the email, ensuring consistent authentication.
- If login is successful, the user is authenticated and redirected; otherwise, appropriate error messages are shown.

**TR:**
- `LoginView`, e-posta ve şifre ile kullanıcı girişini yöneten bir Django class-based view'dur.
- Brute-force saldırılarına karşı koruma sağlar: 5 hatalı denemeden sonra 5 dakika boyunca girişler engellenir.
- `normalize_email` fonksiyonu, e-postadaki Türkçe karakterleri Latin harflerine çevirir ve küçük harfe dönüştürür; böylece kimlik doğrulama tutarlı olur.
- Giriş başarılıysa kullanıcı oturum açar ve yönlendirilir; başarısızsa uygun hata mesajları gösterilir.

---

## License / Lisans

**EN:**
This project is for educational and demonstration purposes.

**TR:**
Bu proje eğitim ve demo amaçlıdır.
