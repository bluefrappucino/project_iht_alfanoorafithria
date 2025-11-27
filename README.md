# Python (Odoo) Internship Technical Test Module

Modul kustom ini dikembangkan untuk memenuhi persyaratan Ujian Teknis Python (Odoo) Developer - Internship.

## Informasi Modul

| Detail | Nilai |
| :--- | :--- |
| **Nama Teknis Modul** | `project_iht` |
| **Deskripsi** | Inheritance pada modul Project Odoo untuk penambahan field kustom. |
| **Dependensi** | `project`, `base`, `web` |

## Fitur yang Diimplementasikan

Modul ini berfokus pada demonstrasi kemampuan pengembangan *full-stack* Odoo.

### 1. Inheritance Model Project

* Melakukan inheritance pada Model bawaan Odoo: `project.project`.
* Menambahkan 3 field kustom:
    * `lokasi_proyek` (Text)
    * `source_aplikasi_pendukung` (Char/URL)
    * `daftar_perkerja_remote` (Text/JSON)

### 2. View Customization (XML)

* Melakukan inheritance pada Form View Project (`project.edit_project`).
* Menyisipkan ketiga field kustom di Form View Project agar dapat dilihat dan diedit oleh pengguna.

## Cara Pengujian

Untuk memverifikasi fungsionalitas, lakukan langkah-langkah berikut:

1.  **Instalasi:** Instal modul `project_iht` di Odoo (pastikan mode *Developer* aktif).
2.  **Akses Data:** Navigasi ke menu **Projects** > **Projects**.
3.  **Verifikasi:** Buka salah satu form Project. Tiga field kustom baru (`Lokasi Proyek`, `Aplikasi Pendukung`, dan `Daftar Pekerja Remote (JSON)`) akan muncul di Form View.

## Kolaborasi & Kontak

* **Penguji:** User `asiasiapac` telah diundang sebagai kolaborator.
* **Pengembang:** saya Alfa Noora Fithria dengan user `bluefrappucino`

---
