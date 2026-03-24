from elektronik import BarangElektronik
from habis_pakai import BarangHabisPakai
from aset_tetap import BarangAsetTetap
from manage import ManageSIMPAN

def main():
    m = ManageSIMPAN("Kantor Pusat")

    b1 = BarangElektronik("E001", "Laptop ASUS", 8500000, 10, "ASUS", 24)
    b2 = BarangElektronik("E002", "Printer Canon", 2300000, 5, "Canon", 12)
    b3 = BarangHabisPakai("H001", "Tinta Printer", 85000, 50, "Botol", "2026-12-31")
    b4 = BarangAsetTetap("A001", "Mesin Fotokopi", 15000000, 2, 2020, "Baik")

    m.tambah_barang(b1)
    m.tambah_barang(b2)
    m.tambah_barang(b3)
    m.tambah_barang(b4)

    m.tampilkan_semua()
    m.laporan_per_kategori()

    m.cek_stok_menipis(batas_minimal=10)

    barang = m.cari_id("E001")
    harga_lama = barang.harga
    m.ubah_harga("E001", 7999000)
    m.catat_riwayat_harga(barang, harga_lama, 7999000)

    m.tampilkan_riwayat_harga()

    m.export_laporan()

if __name__ == "__main__":
    main()