# Implementasi Algoritma RSA (Kriptografi Asimetris)

## Deskripsi
Repository ini berisi implementasi sederhana algoritma kriptografi **RSA (Rivest–Shamir–Adleman)** menggunakan bahasa **Python**. 

Implementasi ini bertujuan untuk menunjukkan bagaimana proses **pembangkitan kunci (key generation), enkripsi, dan dekripsi** dilakukan secara matematis pada algoritma RSA.

---

# Konsep RSA
RSA merupakan algoritma **kriptografi kunci publik (public-key cryptography)** atau **kriptografi asimetris**. Algoritma ini menggunakan dua kunci yang berbeda, yaitu:

- **Kunci Publik (Public Key)** → digunakan untuk proses enkripsi pesan  
- **Kunci Privat (Private Key)** → digunakan untuk proses dekripsi pesan  

Keamanan algoritma RSA bergantung pada kesulitan dalam memfaktorkan bilangan besar yang merupakan hasil perkalian dua bilangan prima.

---

# Tahapan Algoritma RSA

## 1. Pembangkitan Kunci (Key Generation)

Langkah-langkah pembangkitan kunci pada RSA adalah sebagai berikut:

1. Memilih dua bilangan prima besar
   p dan q
2. Menghitung nilai modulus
   n = p × q
3. Menghitung fungsi totien Euler
   φ(n) = (p − 1)(q − 1)

