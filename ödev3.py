class Personel:
    def __init__(self, adı, departmanı, çalışma_yılı, maaşı):
        # Kurucu metod (constructor), Personel sınıfından bir nesne oluşturulduğunda çağrılır.
        # self parametresi, sınıfın mevcut örneğine işaret eder.
        # adı, departmanı, çalışma yılı, maaşı: Personel sınıfına ait özelliklerdir.
        self.adı = adı
        self.departmanı = departmanı
        self.çalışma_yılı = çalışma_yılı
        self.maaşı = maaşı

    def __str__(self):
        # __str__ metodunun özel bir kullanımı vardır: print() fonksiyonuyla bir sınıf örneği yazdırıldığında,
        # bu metodun döndürdüğü string gösterilir.
        return f"Adı: {self.adı}, Departmanı: {self.departmanı}, Çalışma Yılı: {self.çalışma_yılı}, Maaşı: {self.maaşı}"


class Firma:
    def __init__(self):
        # Firma sınıfının kurucu metodu. Personel listesini boş bir liste olarak başlatır.
        self.personel_listesi = []

    def personel_ekle(self, personel):
        # Bir personel eklemek için kullanılır. personel parametresi, Personel sınıfının bir örneğidir.
        self.personel_listesi.append(personel)

    def personel_listele(self):
        # Firma bünyesindeki tüm personelleri ve onların bilgilerini listeler.
        for personel in self.personel_listesi:
            print(personel)

    def maaş_zammı(self, personel, zam_oranı):
        # Belirli bir personelin maaşına zam yapar.
        # personel: Zam yapılacak personelin örneği.
        # zam_oranı: Yapılacak zam miktarı, yüzde olarak.
        for p in self.personel_listesi:
            if p == personel:
                p.maaşı += p.maaşı * zam_oranı / 100

    def personel_çıkart(self, personel):
        # Belirli bir personeli firma bünyesinden çıkartır.
        self.personel_listesi = [p for p in self.personel_listesi if p != personel]

# Örnek kullanım:
personel1 = Personel("Ahmet", "Muhasebe", 5, 5000)
personel2 = Personel("Ayşe", "IT", 3, 7000)

firma = Firma()
firma.personel_ekle(personel1)
firma.personel_ekle(personel2)

print("Personel Listesi:")
firma.personel_listele()

firma.maaş_zammı(personel1, 10)  # Ahmet'in maaşına %10 zam yapılıyor.
firma.personel_çıkart(personel2)  # Ayşe çıkartılıyor.

print("\nGüncel Personel Listesi:")
firma.personel_listele()  # Güncel personel listesi yazdırılıyor.
