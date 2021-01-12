# Final Project Sistem Deteksi dan Intrusi

## Face Mask Detection Using Python Machine Learning and PushBullet Notification<br />

![nama](https://img.shields.io/badge/Nama-Fikri%20Haykal-blueviolet)<br />
![nrp](https://img.shields.io/badge/NRP-05311840000006-blueviolet)<br />
![angkatan](https://img.shields.io/badge/Angkatan-2018-blueviolet)<br />
![matkul](https://img.shields.io/badge/Mata%20Kuliah-Sistem Deteksi%20dan%20Intrusi-blueviolet)<br />
![dosen](https://img.shields.io/badge/Dosen%20Pembimbing-Ridho%20Rahman%20Hariadi%20S.Kom,%20M.Sc-blueviolet)<br />

### Deskripsi
Sehubungan dengan adanya pandemi <i>Corona Virus Disease 19</i> atau yang biasa disebut COVID, semua orang diwajibkan memakai masker untuk beraktivitas di luar rumah. Oleh karena itu pengunjung tempat umum perlu dipastikan apakah memakai masker atau tidak. Penjaga tentunya tidak selalu bisa mengecek pengunjung satu per satu. Maka munculah ide untuk membuat program ini yang bisa meringankan tugas penjaga tempat umum. Program ini mendeteksi seseorang yang masuk ke suatu tempat atau ruangan, dan mengecek apakah orang tersebut memakai masker atau tidak. Ketika ada seseorang yang tidak mengenakan masker, maka sistem akan memberi notifikasi pada PushBullet. Program ini dibuat dengan bahasa Python dengan bantuan library Tensorflow, OpenCV serta Keras.

### Requirement
<table>
    <tr>
      <th>Library</th>
      <th>Versi</th>
    </tr>
    <tr>
      <td>Tensorflow</td>
      <td>1.15.2</td>
    </tr>
    <tr>
      <td>Keras</td>
      <td>2.3.1</td>
    </tr>
    <tr>
      <td>Imutils</td>
      <td>0.5.3</td>
    </tr>
    <tr>
      <td>Numpy</td>
      <td>1.18.2</td>
    </tr>
    <tr>
      <td>OpenCV</td>
      <td>4.2.0.*</td>
    </tr>
    <tr>
      <td>Matplotlib</td>
      <td>3.2.1</td>
    </tr>
    <tr>
      <td>Scipy</td>
      <td>1.4.1</td>
    </tr>
  </table>
  
### Cara Kerja
#### 1. OpenCV Menggunakan Kamera
#### 2. Tensorflow dan Keras Mendeteksi Wajah
#### 3. Menampilkan Frame Label
#### 4. Menyimpan Screenshot Frame
#### 5. Membuat Notifikasi PushBullet

### Instalasi
#### 1. Menginstal Anaconda
- Mengunjungi situs resmi <a href="https://www.anaconda.com/products/individual">Anaconda</a>
- Mengunduh installer sesuai sistem operasi
- Menginstal Anaconda
- Membuat <i>Environment</i> baru untuk project

#### 2. Menginstal Requirement
- Membuka Anaconda Prompt
- Berpindah Environtment dengan perintah `activate <nama environment>`
- Menginstal semua library requirement menggunakan `pip install`

#### 3. Mendaftar PushBullet
- Mengunjungi situs resmi <a href="https://www.pushbullet.com/">PushBullet</a>
- Mengunduh installer sesuai sistem operasi
- Menginstal PushBullet
- Melakukan pendaftaran menggunakan akun Google atau Facebook
- Generate token PushBullet

#### 4. Mengatur Token PushBullet
- Membuka file `detect_mask.py`
- Masukkan token PushBullet pada variabel `token`

#### 5. Testing Program
- Membuka Anaconda Prompt
- Berpindah Environtment dengan perintah `activate <nama environment>`
- Berpindah directory sesuai tempat menyimpan project
- Menjalankan program dengan perintah `python detect_mask.py`
