# Sistem Pendukung Keputusan (SPK) untuk kelayakan pemberian pinjaman menggunakan metode Fuzzy Tsukamoto

| Input Variable    | Linguistik                      | Semesta Pembicaraan       |
| ----------------- | ------------------------------- | ------------------------- |
| Pendapatan        | rendah, sedang, tinggi          | [0, 3, 7, 12...] jt/Bln   |
| Usia              | muda, parobaya, tua, sangat tua | [0, 30, 50, 100...] Tahun |
| Jumlah Tanggungan | sedikit, sedang, banyak         | [0, 2, 3, 10...] Orang    |
| Pengluaran        | rendah, sedang, tinggi          | [0, 1, 3, 10...] jt/Bln   |
| Nilai aset        | sedikit, sedang, banyak         | [0, 10, 40, 100] jt       |

<br>

| Output Variable | Linguistik         | Semesta Pembicaraan |
| --------------- | ------------------ | ------------------- |
| Kelayakan       | tidak layak, layak | [0, 40, 100...]%    |

# Fungsi Keanggotaan

<b>Fungsi Keanggotaan Pendapatan</b>

![pendapatan](resources/membership-functions/pendapatan.png)

<br>

<b>Fungsi Keanggotaan Usia</b>

![usia](resources/membership-functions/usia.png)

<br>

<b>Fungsi Keanggotaan Tanggungan</b>

![tanggungan](resources/membership-functions/tanggungan.png)

<br>

<b>Fungsi Keanggotaan Pengeluaran</b>

![pengeluaran](resources/membership-functions/pengeluaran.png)

<br>

<b>Fungsi Keanggotaan Aset</b>

![aset](resources/membership-functions/aset.png)

<br>

<b>Fungsi Keanggotaan Kelayakan (Output)</b>

![kelayakan](resources/membership-functions/kelayakan.png)

<br>
