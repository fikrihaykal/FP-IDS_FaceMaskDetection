# Final Project Sistem Deteksi dan Intrusi

## Face Mask Detection Using Python Machine Learning and PushBullet Notification<br />

![nama](https://img.shields.io/badge/Nama-Fikri%20Haykal-blueviolet)<br />
![nrp](https://img.shields.io/badge/NRP-05311840000006-blueviolet)<br />
![angkatan](https://img.shields.io/badge/Angkatan-2018-blueviolet)<br />
![matkul](https://img.shields.io/badge/Mata%20Kuliah-Sistem%20Deteksi%20dan%20Intrusi-blueviolet)<br />
![dosen](https://img.shields.io/badge/Dosen%20Pembimbing-Ridho%20Rahman%20Hariadi%20S.Kom,%20M.Sc-blueviolet)<br />


### Daftar Isi
<ol>
    <li><a href="#deskripsi">Deskripsi</a></li>
    <li><a href="#requirement">Requirement</a></li>
    <li><a href="#dataset">Dataset</a></li>
    <li><a href="#cara-kerja">Cara Kerja</a>
        <ol>
            <li><a href="#opencv-menggunakan-kamera">OpenCV Menggunakan Kamera</a>
            <li><a href="#tensorflow-dan-keras-mendeteksi-wajah">Tensorflow dan Keras Mendeteksi Wajah</a>
            <li><a href="#menampilkan-label-frame">Menampilkan Label Frame</a>
            <li><a href="#menyimpan-screenshot-frame">Menyimpan Screenshot Frame</a>
            <li><a href="#membuat-notifikasi-pushbullet">Membuat Notifikasi PushBullet</a>
        </ol>
    </li>
    <li><a href="#instalasi">Instalasi</a>
        <ol>
            <li><a href="#menginstal-anaconda">Menginstal Anaconda</a>
            <li><a href="#menginstal-requirement">Menginstal Requirement</a>
            <li><a href="#menginstal-pushbullet">Menginstal PushBullet</a>
            <li><a href="#mengatur-token-pushbullet">Mengatur Token PushBullet</a>
            <li><a href="#testing-program">Testing Program</a>
        </ol>
    </li>
    <li><a href="#hasil-run-program">Hasil Run Program</a></li>
</ol>


### Deskripsi
Sehubungan dengan adanya pandemi <i>Corona Virus Disease 19</i> atau yang biasa disebut COVID-19, semua orang diwajibkan memakai masker untuk beraktivitas di luar rumah. Oleh karena itu pengunjung tempat umum perlu dipastikan apakah memakai masker atau tidak. Penjaga tentunya tidak selalu bisa mengecek pengunjung satu per satu. Maka munculah ide untuk membuat program ini yang bisa meringankan tugas penjaga tempat umum. Program ini mendeteksi seseorang yang masuk ke suatu tempat atau ruangan, dan mengecek apakah orang tersebut memakai masker atau tidak. Ketika ada seseorang yang tidak mengenakan masker, maka sistem akan memberi notifikasi pada PushBullet. Program ini dibuat dengan bahasa Python dengan bantuan library Tensorflow, OpenCV serta Keras.


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


### Dataset
- Terletak pada folder `dataset`
- Terdapat 2 subdirektori, yaitu `with_mask` dan `without_mask`
- Pada folder `with_mask` terdapat 1915 gambar orang yang memakai masker
- Pada folder `without_mask` terdapat 1918 gambar orang yang tidak memakai masker


### Cara Kerja
#### 1. OpenCV Menggunakan Kamera
Pertama kali pada saat menjalankan script `detect_mask.py`, program akan membuka sebuah window yang berisi tampilan kamera. Dari situ OpenCV akan menghandle dari frame ke frame untuk diolah oleh Tensorflow.

#### 2. Tensorflow dan Keras Mendeteksi Wajah
Setelah mendapat frame dari OpenCV, maka Tensorflow akan mendeteksi apakah ada wajah seseorang dalam frame tersebut. Jika ada, maka akan diolah dan dicek, apakah orang tersebut memakai masker atau tidak. Pada tahap ini, return value yang dihasilkan masih berupa sebuah integer, belum ada pelabelan apakah orang tersebut memakai masker atau tidak.

#### 3. Menampilkan Label Frame
Tahap ini hanya akan dilalui ketika ada wajah seseorang yang terdeteksi pada frame. Pada tahap ini, fungsi menerima return value yang digunakan untuk menentukan apakah orang pada frame tersebut memakai masker atau tidak. Label juga akan ditampilkan pada frame beserta skor dalam bentuk persentase.

#### 4. Menyimpan Screenshot Frame
Tahap ini akan dilalui ketika ada seseorang yang tidak mengenakan masker. Program akan menyimpan frame pada folder `intruder`, setelah itu akan diteruskan untuk dikirim pada Idling PushBullet sebagai notifikasi. File akan disimpan dengan penamaan <b>Timestamp</b> untuk menghindari duplikasi. Selain itu, file disimpan juga digunakan sebagai dokumentasi

#### 5. Membuat Notifikasi PushBullet
Setelah frame disimpan, maka langkah selanjutnya adalah mengirim gambar tersebut untuk digunakan sebagai notifikasi pada PushBullet. Yang dapat diakses di Web, Desktop maupun Mobile App


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


### Hasil Run Program
