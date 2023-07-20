# Project "Platform Investasi"

## 1. Deskripsi Project:
"Platform Investasi" adalah sebuah aplikasi sederhana yang dibangun menggunakan framework Streamlit. Tujuan dari aplikasi ini adalah untuk membantu pengguna menghitung nilai investasi setelah jangka waktu tertentu dengan tingkat bunga yang ditentukan. Pengguna dapat memasukkan jumlah investasi, tingkat bunga tahunan, dan jumlah tahun, dan aplikasi akan menghitung dan menampilkan nilai investasi akhir. Selain itu, aplikasi juga menyediakan fitur tambahan berupa grafik investasi untuk memvisualisasikan perkembangan nilai investasi dari tahun ke tahun.

### Fitur-fitur Aplikasi:

1. **Input Nilai Investasi:** Pengguna dapat memasukkan jumlah investasi awal dalam mata uang USD.
2. **Input Tingkat Bunga Tahunan:** Pengguna dapat memasukkan tingkat bunga tahunan dalam bentuk persentase (%).
3. **Input Jumlah Tahun:** Pengguna dapat memasukkan jumlah tahun untuk menghitung investasi di masa depan.
4. **Hitung Hasil Investasi:** Aplikasi akan menghitung nilai investasi setelah jangka waktu yang ditentukan berdasarkan nilai investasi awal dan tingkat bunga yang diberikan.
5. **Konversi Mata Uang:** Aplikasi mendukung beberapa mata uang (USD, EUR, GBP, JPY, IDR), sehingga pengguna dapat memilih mata uang yang diinginkan untuk menampilkan hasil investasi.
6. **Grafik Investasi:** Aplikasi menyajikan grafik yang memvisualisasikan perkembangan nilai investasi dari tahun ke tahun berdasarkan tingkat bunga yang diberikan.

### Cara Menjalankan Aplikasi:
1. Pastikan Python sudah terinstal.
2. Clone repositori ini.
3. Install library yang dibutuhkan dengan menjalankan perintah berikut di terminal atau command prompt:
   ```
   pip install streamlit forex-python
   ```
4. Jalankan aplikasi dengan perintah:
   ```
   streamlit run invest-app.py
   ```
5. Aplikasi akan berjalan di browser pada alamat `http://localhost:8501`. atau
6. Dapat diakses dengan External URL [berikut](http://135.181.26.148:25144/): `http://135.181.26.148:25144/` 

### Utilities yang Digunakan:

1. [Streamlit](https://www.streamlit.io/): Framework Python yang digunakan untuk membangun aplikasi web interaktif dengan cepat dan mudah.
2. [Forex Python](https://forex-python.readthedocs.io/en/latest/): Library yang digunakan untuk melakukan konversi mata uang dalam aplikasi. Digunakan untuk menghitung nilai investasi dalam mata uang yang dipilih oleh pengguna.
3. [Python](https://www.python.org/): Bahasa pemrograman utama yang digunakan dalam pembuatan aplikasi.
4. [Visual Studio Code](https://code.visualstudio.com/): IDE (Integrated Development Environment) yang digunakan untuk mengembangkan dan mengedit kode aplikasi.
5. [Git](https://git-scm.com/): Sistem kontrol versi yang digunakan untuk mengelola perubahan kode dan kolaborasi tim pengembang.
6. [GitHub](https://github.com/): Platform yang digunakan untuk menyimpan dan berbagi kode aplikasi dengan tim pengembang.

## 2. Penjelasan tentang Sistem Operasi dalam Proses Containerization:

Sistem operasi memainkan peran penting dalam proses containerization karena kontainer mengisolasi aplikasi dan semua dependensinya dari sistem host. Kontainer menggunakan fitur-fitur virtualisasi dari sistem operasi untuk menciptakan lingkungan terisolasi yang memungkinkan aplikasi berjalan tanpa terpengaruh oleh konfigurasi atau library yang ada di sistem host. Dalam proses containerization, image docker dibuat yang berisi aplikasi dan semua dependensinya, dan kemudian image tersebut dijalankan di dalam container yang berjalan pada sistem operasi host. Sistem operasi menyediakan mekanisme yang memungkinkan container berkomunikasi dengan host dan container lainnya, sehingga aplikasi dalam container dapat berjalan dengan aman dan efisien.

## 3. Penjelasan Bagaimana Containerization Membantu Mempermudah Pengembangan Aplikasi:

### Cara Containerization membantu mempermudah pengembangan aplikasi:

1. **Portabilitas:** Kontainer berjalan secara konsisten di berbagai lingkungan, baik di mesin pengembangan, pengujian, maupun produksi. Ini memastikan bahwa aplikasi berjalan dengan benar tanpa perlu khawatir tentang perbedaan konfigurasi antar lingkungan.
2. **Isolasi:** Kontainer memisahkan aplikasi dan dependensinya dari sistem host dan kontainer lainnya. Ini menghindari konflik dan permasalahan yang mungkin muncul akibat dependensi yang saling tumpang tindih.
3. **Skalabilitas:** Dengan menggunakan container, pengembang dapat dengan mudah menambah atau mengurangi salinan aplikasi sesuai permintaan, yang memungkinkan skala horizontal secara efisien.
4. **Pemutakhiran dan Pemeliharaan:** Dalam containerization, pengembang dapat dengan cepat memperbarui aplikasi dan dependensinya dengan image yang telah disiapkan sebelumnya tanpa harus mempengaruhi lingkungan lain.

## 4. Penjelasan tentang DevOps dan Bagaimana DevOps Membantu Pengembangan Aplikasi:
DevOps adalah pendekatan yang menggabungkan Development (Pengembangan) dan Operations (Operasional) dalam pengembangan dan pengelolaan perangkat lunak. Tujuan utama dari DevOps adalah mencapai pengiriman perangkat lunak yang lebih cepat, lebih sering, dan lebih andal. DevOps membantu pengembangan aplikasi dengan cara:
1. **Kolaborasi Tim:** DevOps mendorong kolaborasi erat antara tim pengembang dan operasional untuk menghindari silo informasi dan meningkatkan efisiensi.
2. **Automasi:** Automasi digunakan untuk mengotomatiskan proses pengujian, integrasi, pengiriman, dan pemeliharaan aplikasi. Ini mengurangi kesalahan dan mempercepat siklus pengembangan.
3. **Continuous Integration & Continuous Deployment (CI/CD):** DevOps mengadopsi pendekatan CI/CD, di mana perubahan kode diuji dan diintegrasikan secara otomatis dalam alur kerja yang terus-menerus, memungkinkan pengiriman perangkat lunak yang cepat dan stabil.
4. **Monitor dan Feedback:** DevOps memungkinkan tim untuk memantau kinerja aplikasi secara terus-menerus dan memberikan umpan balik secara cepat, sehingga memungkinkan perbaikan dan iterasi yang lebih cepat.

## 5. Contoh Penerapan DevOps di Perusahaan Gojek:
Gojek, sebagai perusahaan teknologi dan transportasi berbasis aplikasi di Asia Tenggara, telah menerapkan praktik DevOps untuk mengoptimalkan proses pengembangan dan pengiriman produknya. Beberapa contoh penerapan DevOps di Gojek meliputi:
1. **CI/CD Pipeline:** Gojek menggunakan CI/CD pipeline untuk mengotomatiskan proses pengujian dan pengiriman aplikasi. Setiap perubahan kode diuji secara otomatis dan diintegrasikan ke dalam repositori bersama sebelum diterapkan secara produksi.
2. **Infrastruktur Otomatis:** Gojek menggunakan layanan cloud dan alat otomatisasi untuk mengelola infrastruktur dan lingkungan aplikasi, sehingga memungkinkan untuk penskalaan otomatis dan manajemen daya guna.
3. **Pengelolaan Kontainer:** Gojek menggunakan teknologi kontainer seperti Docker dan Kubernetes untuk menyederhanakan penyebaran dan pemeliharaan aplikasi di lingkungan yang berbeda, serta untuk memastikan skala yang lebih cepat dan efisien.
4. **Monitoring dan Analytics:** Gojek mengadopsi berbagai alat pemantauan untuk memantau performa aplikasi secara real-time, sehingga masalah dapat diidentifikasi dan diperbaiki dengan cepat.
5. **Budaya Kolaborasi:** Gojek mendorong budaya kolaboratif antara tim pengembangan dan operasional dengan melakukan pertemuan reguler dan berbagi pengetahuan untuk meningkatkan komunikasi dan efisiensi.

### Implementasi DevOps di Gojek telah membantu perusahaan mencapai pengiriman produk yang lebih cepat, lebih stabil, dan lebih inovatif, sehingga dapat terus bersaing di pasar yang cepat berubah.

### 6. [Publicated Docker Image via Docker Hub](https://hub.docker.com/r/spicynoon/investyu) 
