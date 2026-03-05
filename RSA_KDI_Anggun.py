def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (g, x, y)

def mod_inverse(e, phi):
    # d ≡ e^{-1} (mod phi)
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise ValueError("Tidak ada inverse modular (e dan phi tidak coprime).")
    return x % phi

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    r = int(n ** 0.5)
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

def rsa_keygen_manual(p, q, verbose=True):
    if not is_prime(p) or not is_prime(q) or p == q:
        raise ValueError("p dan q harus bilangan prima dan berbeda.")

    n = p * q
    phi = (p - 1) * (q - 1)

    e_candidates = [3, 5, 17, 257, 65537]
    e = None

    for cand in e_candidates:
        if cand < phi and gcd(cand, phi) == 1:
            e = cand
            break

    if e is None:
        cand = 3
        while cand < phi:
            if gcd(cand, phi) == 1:
                e = cand
                break
            cand += 2

    d = mod_inverse(e, phi)

    if verbose:
        print("\n")
        print("=== RSA KEY GENERATION ===")
        print(f"1) Pilih p (prima) = {p}")
        print(f"2) Pilih q (prima) = {q}")
        print(f"3) Hitung n = p*q = {n}")
        print(f"4) Hitung phi(n) = (p-1)(q-1) = {phi}")
        print(f"5) Pilih e (coprime dengan phi) = {e}  (gcd(e,phi)={gcd(e,phi)})")
        print(f"6) Hitung d = e^-1 mod phi = {d}")
        print("\nKunci Publik  (e, n) =", (e, n))
        print("Kunci Privat  (d, n) =", (d, n))
        print("\nCatatan Distribusi Kunci:")
        print("- Kunci publik (e,n) boleh dibagikan untuk proses enkripsi.")
        print("- Kunci privat (d,n) wajib dirahasiakan untuk proses dekripsi.")
        print("========================================\n")

    return (e, n), (d, n)

def encrypt_text(plaintext, public_key, verbose=True):
    e, n = public_key
    cipher_nums = []

    if verbose:
        print("\n")
        print("=== ENKRIPSI RSA ===")
        print(f"Plaintext: {plaintext}")
        print("Konversi tiap karakter -> ASCII -> rumus C = M^e mod n\n")

    for ch in plaintext:
        m = ord(ch)  # ASCII
        if m >= n:
            raise ValueError(
                f"Nilai ASCII '{ch}' = {m} harus < n={n}. "
                "Gunakan p dan q lebih besar."
            )

        c = mod_exp(m, e, n)
        cipher_nums.append(c)

        if verbose:
            print(f"Karakter '{ch}' -> M={m}")
            print(f"C = {m}^{e} mod {n} = {c}\n")

    if verbose:
        print("Ciphertext (angka-angka):", cipher_nums)
        print("================================\n")

    return cipher_nums

def decrypt_text(cipher_nums, private_key, verbose=True):
    d, n = private_key
    plaintext_chars = []

    if verbose:
        print("=== DEKRIPSI RSA ===")
        print("Gunakan rumus M = C^d mod n, lalu konversi ASCII -> karakter\n")

    for c in cipher_nums:
        m = mod_exp(c, d, n)
        ch = chr(m)
        plaintext_chars.append(ch)

        if verbose:
            print(f"C={c}")
            print(f"M = {c}^{d} mod {n} = {m} -> '{ch}'\n")

    plaintext = "".join(plaintext_chars)

    if verbose:
        print("Plaintext hasil dekripsi:", plaintext)
        print("================================\n")

    return plaintext

def main():
    print("RSA\n")

    while True:
        try:
            p = int(input("Masukkan p (prima): "))
            q = int(input("Masukkan q (prima): "))

            if not is_prime(p) or not is_prime(q):
                print("Error: p dan q harus bilangan prima.\n")
                continue

            if p == q:
                print("Error: p dan q tidak boleh sama.\n")
                continue

            break
        except ValueError:
            print("Error: masukkan angka yang valid.\n")

    public_key, private_key = rsa_keygen_manual(p, q, verbose=True)

    plaintext = input("Masukkan plaintext (teks pendek): ")
    cipher = encrypt_text(plaintext, public_key, verbose=True)
    decrypted = decrypt_text(cipher, private_key, verbose=True)

    print("=== HASIL AKHIR ===")
    print("Plaintext awal :", plaintext)
    print("Ciphertext     :", cipher)
    print("Plaintext akhir:", decrypted)

    if decrypted == plaintext:
        print("\nSukses: hasil dekripsi sama dengan plaintext.")
    else:
        print("\nGagal: hasil dekripsi berbeda (cek p,q,n).")

if __name__ == "__main__":
    main()