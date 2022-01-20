#membuat portofolio kasir Indomaret

#langkahnya yaitu:

'''
- daftar barang:#aman
  - minyak = harga
  - gula = harga
  - beras = harga
- input barang #aman
- menghitung barang # aman 
- proses pembayaran
'''
import sys
daftar_barang = {
                'minyak' : {'Tropical':28000,'Bimoli':26000,'Filma':24500},
                'Gula':{'Gulaku':12500,'Gmp':12500},
                'Beras':{'Sania':50000,'Sipulen':80000,'Top Koki':60000}
                }  
list_belanja = []
harga_belanja = []

class wallet():
    def __init__(self,arg1,arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        print('\t\t\t'+'-'*39)
        print(f'\t\t\t|{arg2:^37}|')
        print('\t\t\t'+'-'*39)
        for i,j in zip(list_belanja,harga_belanja):
            print(f'\t\t\t{i:<19}={j:^19,}\n')
        print('\t\t\t'+'-'*37,'+'.ljust(2))
        kembalian = self.pembayaran(arg1)
        for a,b,c in zip(('Total Belanja','Jumlah Bayar', 'Kembalian'),(total_belanja,arg1,kembalian),('\n\n','\n','\n')):
            print(f'\t\t\t{a:<19}={b:^19,}{c}')
        print('\t\t\t  {}\t  {}'.format('Distributor','Customer'))
        print('\n\n'+'\t\t\t  {:^11}\t  {}'.format('Indomaret','........'))
        
    
    def pembayaran(self,arg1):
        kembalian = arg1 - total_belanja
        return kembalian
    
    def file(self):
        file = open('Riwayat Pembayaran Indomaret','w')
        file.write('\t\t\t'+'-'*39+'\n')
        file.write(f'\t\t\t|{self.arg2:^37}|\n')
        file.write('\t\t\t'+'-'*39+'\n')
        for i,j in zip(list_belanja,harga_belanja):
            file.write(f'\t\t\t{i:<19}={j:^19,}\n')
        file.write('\t\t\t'+'-'*37+'+'.ljust(2)+'\n')
        kembalian = self.pembayaran(self.arg1)
        for a,b,c in zip(('Total Belanja','Jumlah Bayar', 'Kembalian'),(total_belanja,self.arg1,kembalian),('\n\n','\n','\n')):
            file.write(f'\t\t\t{a:<19}={b:^19,}{c}')
        file.write('\n')
        file.write('\t\t\t  {}\t  {}'.format('Distributor','Customer'))
        file.write('\n\n'+'\t\t\t  {:^11}\t  {}'.format('Indomaret','........'))
        
        
print('  ','-'*80)
print('  ',format('|','<40'),format('|','>39'))
print('  ',format('|','<30'),format('Selamat Datang','^18'),format('|','>30'))
print('  ',format('|','<30'),format('Di Indomaret','^18'),format('|','>30'))
print('  ',format('|','<40'),format('|','>39'))
print('  ','-'*80,end = '\n\n')
print('\t\t\t'+'-'*39)
print('\t\t\t|{:^37}|'.format(''))
print('\t\t\t|{'':^37}|'.format('Daftar Barang'))
print('\t\t\t|{:^37}|'.format(''))
print('\t\t\t'+'-'*39)
print('\t\t\t|{:^4}|{:^16}|{:^15}|'.format('No', 'Barang', 'Harga'))
print('\t\t\t'+'-'*39)
angka = 0
for k in daftar_barang.values():
    for i,j in zip(k.values(),k.keys()):
        angka+=1
        print(f'\t\t\t|{angka:^4}|{j:^16}|{i:^15,}|')
        print('\t\t\t'+'-'*39)

while True:
    try:
        count = int(input('Masukkan jumlah inputan max 5 = '))
        jml = count
        while 6 > count > 0:
            print('input data ke - {:d}'.format(jml-count+1))
            barang = input("masukkan daftar barang : ").title()
            for k ,s in zip(daftar_barang.values(),daftar_barang.keys()):
                if barang in tuple(k.keys()) and barang.istitle():
                    list_belanja.append(barang)
                    harga_belanja.append(daftar_barang[s][barang])
                    break       
            else:
                print('Masukkan barang sesuai yang tertera') 
                continue
            count -=1
        break      
    except:
        print('masukkan tipe angka')
total_belanja = 0            
print('\t\t\t'+'-'*39)
print(f'\t\t\t| No | Daftar Belanja | Harga Belanja |')
print('\t\t\t'+'-'*39)
for i,j,d in zip(list_belanja,harga_belanja,range(1,len(list_belanja)+1)):
    print(f'\t\t\t|{d:^4}|{i:^16}| Rp{j:^12,}|')
    print('\t\t\t'+'-'*39)
    total_belanja += j
print('\t\t\t|{:^21}| RP{:^12,}|'.format('Total Belanja',total_belanja))
print('\t\t\t'+'-'*39)
while True:
    pilih_pembayaran = input('Pilih Pembayaran Anda [Shopeepay/Ovo/Dana] = ')
    if pilih_pembayaran in ("shopeepay".lower(),"shopeepay".upper(),"shopeepay".title()):
        pilih_pembayaran = pilih_pembayaran.title()
        break
    elif pilih_pembayaran in ("ovo".lower(),"ovo".upper(),"ovo".title()):
        pilih_pembayaran = pilih_pembayaran.title()
        break
    elif pilih_pembayaran in ("dana".lower(),"dana".upper(),"dana".title()):
        pilih_pembayaran = pilih_pembayaran.title()
        break
    else:
        print('your input is uncorrect')
while True:
    try:
        money = int(input('masukkan Jumlah Uang = '))
        if money >= total_belanja:
            money = money
            break
        else:
            print('Your money is minus')
    except:
        print('please input Numeric')
transaction = wallet(money,pilih_pembayaran)
pilihan_1 = input('do you want to print transaction [Yes / No]: ').title()
if pilihan_1.istitle():
    transaction.file()
else:
    sys.exit()
