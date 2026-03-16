#  🚀 LinkVault MVP (Minimum Viable Product) Özellikleri
Bu döküman,projenin ilk aşamasında geliştirilecek temel özellikleri ve sistem mimarisini tanımlar.

## 1.Amaç
Kullanıcıların internet üzerindeki önemli bağlantıları güvenli bir şekilde saklanmasını,etiketlemesini ve yönetmesini sağlayan bir backend API hizmeti.

## 2.Teknik Yığın (Tech Stack)
* **Dil:** Python 3.10+
* **Framework:** FastAPI
* **Database:** PostgreSQL (Ana Veri),Redis (Cache)
* **ORM:** SQLAlchemy
* **Container:** Docker & Docker Compose
## 3. Fonksiyonel Gereksinimler (Kullanıcı Ne yapabilir?)
- [] **Auth:** Kullanıcı kayıt olabilmeli ve JWT ile giriş yapabilmeli.
- [] **Link CRUD:** Kullanıcı link ekleyebilmeli ,silebilir ve güncellebilmeli.
- [] **Etiketleme:** Her linke birden fazla etiket eklenebilmeli.
- [] **Arama:** Başlığa veya etikete göre filtre yapılabilmeli.

## 4.Sistem Akışı (Workflow)
1.Kullanıcı 'POST /auth/login' ile token alır.
2.Alınan token 'Header' kısmına eklenir.
3.'POST /links ' ile yeni bir veri gönderilir.
4.Veri önce şemadan geçer (Pydantic) ,sonra DB'ye yazılır.



