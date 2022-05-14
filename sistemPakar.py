import os

print("------------------------------------------------------------------------")
print("\t\tSelamat Datang Toko Komputer\t\t ")
print("\tUntuk Menentukan Spesifikasi Personal Komputer\t ")
print("Sebagai Pengambilan Keputusan Dalam Membeli Komputer Sesuai Kebutuhan")
print("------------------------------------------------------------------------")


nama = input("\nMasukan Nama Anda : \n")
pilihan = input(
    "\nHi, "+nama+". Apakah Anda Mau Membeli Personal Komputer? (yes/no) : ")

os.system("clear")

while pilihan == "yes":
    print("\nKebutuhan/Kriteria yang diinginkan (DATA 1)\n")
    print("\t a.	Dana yang di sediakan < 3 Jt")
    print("\t b.	Dana yang di sediakan  3-5 Jt")
    print("\t c.	Dana yang di sediakan > 5 Jt")
    print("\t d.	Komputer untuk mengetik")
    print("\t e.	Komputer untuk game")
    print("\t f.	Komputer untuk grafis")
    print("\t g.	Butuh akses internet")
    print("\t h.	Ruangan ber AC")
    print("\t i.	Senang musik")
    print("\t j.	Senang menonton film")
    print("\t k.	Memakai VGA")
    print("\t l.	Tanpa VGA (Integreted)")
    print("-----------------------------------------------------------------------------------------------")
    print("Pilihlah Kebutuhan/Kriteria PC yang anda inginkan")
    print("Contoh : anda membutuhkan pc dengan keriteria/kebutuhan pada point a,b,c,d,e,f,g,h,i.j.k,l ")
    print("Maka anda hanya perlu menginputkan a,b,c,d,e,f,g,h,i.j.k,l")
    print("-----------------------------------------------------------------------------------------------")

    beli = input("Masukan Kebutuhan/Kriteria yang anda inginkan : ")

    if beli == "a,d,g,h,i,j":
        print("\nPaket Ekonomis 1 dengan harga Rp. 2.450.000\n")
        print("Dengan Spesifikasi Seperti Berikut :\n")
        print("\t a.	Gigabyte GA8VM800 PMD")
        print("\t b.	Intel Celleron 2,66 GHZ")
        print("\t c.	DDR3 2Gb PC 3200")
        print("\t d.	VGA Integrated")
        print("\t e.	HD 80 Gb SATA")
        print("\t f.	CD ROM 52X Samsung")
        print("\t g.	CRT 15” Samsung 591")
        print("\t h.	Casing ATX  400W")
        print("\t i.	Speaker Simbadda CST 6000")
        print("\t j.	Modem Prolink Internal\n")

    elif beli == "a,d":
        print("\nPaket Ekonomis 2 dengan harga Rp. 2.550.000\n")
        print("Dengan Spesifikasi Seperti Berikut :\n")
        print("\t a.	Asus P5PE-VM")
        print("\t b.	Intel Celleron 2.26 GHZ")
        print("\t c.	DDR 128 Mb PC 3200")
        print("\t d.	VGA Integrated")
        print("\t e.	HD 40 Gb SATA")
        print("\t f.	CD ROM 52X Samsung")
        print("\t g.	CRT 15” Samsung 591")
        print("\t h.	Casing ATX  400W\n")

    elif beli == "a,e,h,i,j":
        print("\nPaket Ekonomis 3 dengan harga Rp. 2.750.000\n")
        print("Dengan Spesifikasi Seperti Berikut :\n")
        print("\t a.	Asus K8V-VM")
        print("\t b.	AMD Sempron 2800+")
        print("\t c.	DDR 256 Mb PC 3200")
        print("\t d.	VGA Integrated")
        print("\t e.	HD 80 GB SATA")
        print("\t f.	CD ROM 52X LG")
        print("\t g.	CRT 15” Advance")
        print("\t h.	Casing ATX 400W")
        print("\t i.	Speaker Simbadda CST 6000\n")

    elif beli == "a,e,g,h,i,j":
        print("\nPaket Ekonomis 4 dengan harga Rp. 2.900.000\n")
        print("Dengan Spesifikasi Seperti Berikut :\n")
        print("\ta.	Gigabyte K8VM800")
        print("\t b.	AMD Sempron 2800+")
        print("\t c.	DDR 256 Mb PC 3200")
        print("\t d.	VGA Integated")
        print("\t e.	HD 80 Gb SATA")
        print("\t f.	CD ROM 52X LG")
        print("\t g.	CRT 15” Advance")
        print("\t h.	Casing ATX 400W")
        print("\t i.	Speaker Simbadda CST 6000")
        print("\t j.	Modem Prolink Internal\n")

    elif beli == "a,c,e,f,g,k":
        print("\nPaket Ekonomis 5 dengan harga Rp. 5.000.000\n")
        print("Dengan Spesifikasi Seperti Berikut :\n")
        print("\t a.	Gigabyte K8VM800")
        print("\t b.	Processor Intel Core i3-1115G4 (2C / 4T, 3.0 / 4.1GHz, 6MB) ")
        print("\t c.	Graphics NVIDIA Geforce MX350 2GB GDDR5")
        print("\t d.	Chipset Intel SoC Platform")
        print("\t e.	Memory 4GB Soldered DDR4-3200")
        print("\t f.	Memory Slots One memory soldered to systemboard, one DDR4 SO-DIMM slot, dual-channel capable")
        print("\t g.	Max Memory Up to 12GB (4GB soldered + 8GB SO-DIMM) DDR4-3200 offering")
        print("\t h.	Storage 256GB SSD M.2 2242 PCIe 3.0x4 NVMe")
        print("\t i.	2.5"" HDD up to 1TB")
        print("\t j.	Audio Chip High Definition (HD) Audio, Realtek ALC3287 codec")

    else:
        print("Kombinasi Kebutuhan/Kriteria yang anda masukan\nbelum terdaftar pada perpustkaan pengetahuan sistem")

    print("+--------------------------------------------------------------------------------------------------------------+")
    pilihan = input(
        "\nHi, "+nama+". Apakah Anda Mau Membeli Personal Komputer, Lagi? (yes/no) : ")

    if pilihan == "yes":
        os.system("clear")
        print("\t\tSelamat Datang toko komuter\t\t ")
        print("\tUntuk Menentukan Spesifikasi Personal Komputer \t ")
        print("Sebagai Pengambil Keputusan Dalam Pembelian Komputer")

    else:
        print("\n+ Terima Kasih Telah datang di toko kami")
