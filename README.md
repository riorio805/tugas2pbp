# tugas3pbp

Link to webpage:<br>
-> [on pbp.cs.ui.ac.id](http://sefriano-edsel-tugas.pbp.cs.ui.ac.id)<br>
Previous weeks page: [here](./archive/archive_list.md)<br>

(only works on the website)<br>
Link to main: [here](./main)<br>


Second last checklist items:<br>
[POST, GET](#pog-test)
\- [XML, JSON, HTML](#johns-xml-tml)
\- [JSON good](#json-the-best)
\- [Implementasi](#how-to)<br>
Last checklist item:
[Postman pictures](#images-of-the-elusive-postman)

<br>

## Checklist
- [x] Membuat input `form` untuk menambahkan objek model pada app sebelumnya.
- [x] Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML *by ID*, dan JSON *by ID*.
- [x] Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2.
- [ ] Menjawab beberapa pertanyaan berikut pada `README.md` pada *root folder*.
    - [x] Apa perbedaan antara form `POST` dan form `GET` dalam Django?
    - [x] Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    - [ ] Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    - [x] Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).
- [x] Mengakses kelima URL di poin 2 menggunakan Postman, membuat *screenshot* dari hasil akses URL pada Postman, dan menambahkannya ke dalam `README.md`.
- [x] Melakukan `add`-`commit`-`push` ke GitHub.

**Bonus:**
- [x] Menambahkan pesan "Kamu menyimpan X item pada aplikasi ini" (dengan X adalah jumlah data item yang tersimpan pada aplikasi) dan menampilkannya di atas tabel data. Kalimat pesan boleh dikustomisasi sesuai dengan tema aplikasi, namun harus memiliki makna yang sama.


---
<a id="pog-test"></a>
## pog test [↑](#)
Form `POST` digunakan ketika kita ingin mengubah database dari website tersebut, dan form `GET` digunakan ketika kita ingin mengakses database tersebut. Form `POST` juga digunakan ketika kita berurusan dengan data sensitif/pribadi, karena Django secara otomatis mengenkripsi data yang dikirim melalui `POST` request. Sedangkan, data melalui form `GET` dibundel dan digunakan untuk membuat sebuah URL yang dikirim ke server.

Contoh dari penggunaan form `POST` adalah Form Buat item baru di sebuah aplikasi inventory. Kita menggunakan form `POST` karena berhubungan dengan penambahan sebuah Item dalam database (perubahan database).

Contoh dari penggunaan form `GET` adalah *web search*, seperti Google. Data yang terkirim melewati request bisa dilihat langsung di URL, contohnya:
(https://www.google.com/search?q=django)<br>
Data yang terkirim adalah `{'q': "django"}`

---
<a id="johns-xml-tml"></a>
## johns xml tml [↑](#)
Perbedaan utama dari ketiga format pengiriman data tersebut adalah struktur dan tujuan dari format tersebut.

Struktur dari XML terlihat seperti *tree*, dengan menggunakan tag (dengan attribut opsional) untuk menandakan objek. Tag yang dapat digunakan bisa apa aja, yang menunjukkan tipe objek dari data berikutnya. Tujuan dari XML adalah sebagai tempat penyimpanan data atau untuk mengirim data antara sebuah server dengan server lainnya.

Struktur dari JSON bersifat seperti *dictionary*, dengan setiap objek memiliki atribut masing masing. Tujuan dari JSON adalah sebagai representasi data yang lebih mudah dibaca oleh manusia, dan sebagai format pengiriman data yang lebih ringan daripada XML.

Struktur dari HTML terlihat sama seperti XML, tetapi memiliki struktur tag yang berbeda dari XML. Tag yang dapat digunakan hanya dari yang dispesifikasi saja, seperti `<p>`, `<h1>`, dll. Tujuan dari HTML adalah sebagai template pembuatan sebuah *webpage*, yang dapat menampilkan data secara visual.

---
<a id="json-the-best"></a>
## json the best [↑](#)
JSON paling sering digunakan pada pertukaran data antar aplikasi web dikarenakan beberapa faktors, seperti:

- JSON merupakan format yang relatif sederhana, karena memiliki sintaks yang sedikit.
- Filesize dari JSON lebih ringan dibandingkan format lain, sehingga mempercepat komunikasi antar aplikasi web.
- JSON sangat mudah di-*parse* oleh banyak bahasa pemrograman, seperti JS (pasti), Python, dll.

---
<a id="how-to"></a>
## How to [↑](#)

#### Membuat input `form` untuk menambahkan objek model pada app sebelumnya.
Membuat file baru `forms.py`, lalu membuat class baru bernama `ItemForm` yang meng-*inherit* dari `ModelForm`. Setting dari form yang berada di class Meta dari ItemForm diubah menjadi yang dibutuhkan. Dalam `views.py`, dibuat fungsi baru bernama `create_item` yang menjadi tempat untuk memroses POST request atau GET request. Jika request `GET`, maka mengembalikan website form menggunakan template `create_item.html`, dan jika request `POST`, maka dicek apa form tersebut valid. Jika valid, maka langsung disimpan di database, lalu redirect kembali ke `/main` (tempat display semua item)

#### Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML *by ID*, dan JSON *by ID*.
Untuk melihat objek dalam JSON dan XML, digunakan `serializers.serialize` pada data untuk mengubahnya menjadi format yang benar, lalu diberikan dalam `HTTPResponse` dengan setting tipe konten `application/json`
Untuk melihat objek dalam HTML, disajikan menggunakan template `.html` agar terlihat pada browser yang digunakan.

#### Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2.
Import semua fungsi dari `main.views`, lalu buat path yang menghubungkan URL pattern dengan fungsi tersebut.

#### Menambahkan pesan "Kamu menyimpan X item pada aplikasi ini" (dengan X adalah jumlah data item yang tersimpan pada aplikasi) dan menampilkannya di atas tabel data.
Kita bisa langsung memanggil `len()` pada `QuerySet` yang didapatkan dari `Item.objects.all()` untuk mendapatkan jumlah item yang ada di database. Masukkan jumlah items didalam `context`, lalu ditaruh di template HTML.

---
<a id="images-of-the-elusive-postman"></a>
## Images of the elusive "Postman" [↑](#)
#### HTML
Different regions of the same response.

<img src="./static/main/readme/postman_html1.png" /><br>
Top of the file, contains style and meta things

<img src="./static/main/readme/postman_html2.png" /><br>
Bonus item count display

<img src="./static/main/readme/postman_html3.png" /><br>
A "random" item from the list

<img src="./static/main/readme/postman_html4.png" /><br>
Bottom of the file, contains a button to add an item and a button to go back to root directory

##
#### XML + by id
<img src="./static/main/readme/postman_xml.png" /><br>
XML response

<img src="./static/main/readme/postman_xml_2.png" /><br>
XML response of the item with id==2

##
#### JSON + by id
<img src="./static/main/readme/postman_json.png" /><br>
JSON response

<img src="./static/main/readme/postman_json_2.png" /><br>
XML response of the item with id==2

---
github-markdown.css by <a href="https://github.com/sindresorhus/github-markdown-css">sindresorhus</a> and used under the MIT License<br>
website by sefriano edsel jieftara, class of pbp d