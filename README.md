# RSA-Prime-1024-bit
---
# RSA  
# ***Mã Hóa RSA bằng 2 số nguyên tố 1024 bits***  
## ***Các hàm toán học được sử dụng trong mã hóa***  
 * powMod(a,b,m):  
   * Được dùng để tính phép toán a^b mod m  
   * Code :  
   ``` 
   	def powMod(a,b,m)  
   		result = 1
   		a = a % m
   	while b>0:
   		result = result*(a%m)
   		b >> 1
   		a = a*(a%m)
   	return result
   ```  
 * GCD(a,b):  
   * Được dùng tìm ra ước chung lớn nhất của a và b  
   * Code:  
   ``` 
   	def GCD(a,b):
   		if b == 0:
   		return a
   	return (b,a%b)  
   ```  
 * GCD đảo ngược (a,b):  
   * Dùng để tìm ra modulo đảo của 2 số a và b. Hoặc là dùng để tìm ra 2 số x,y thỏa mãn đẳng thức : ax+by = z = GCD(a,b)  
   * Code:  
   ```
    def GCDnguoc(a,b):
      u1,u2,u3 = 1 , 0 , a
      v1,v2,v3 = 0 , 1 , b
      while v3 != 0:
        q = u3 // v3
        t1 , t2 , t3 = u1 - q*v1 , u2 - q*v2 , u3 - q*v3 
        u1 , u2 , u3 = v1 , v2 , v3
        v1 , v2 , v3 =  t1 , t2 , t3  
      return u1 , u2 , u3 
   ```  
## ***Kiểm tra tính nguyên tố***  
 * Firsthandling : kiểm tra tiền xử lí : lấy số đó chia cho 1000 số nguyên tố đầu tiên : nếu số đó mà chia hết cho 1 trong 1000 số đó thì loại. Còn lại được chọn tiếp tục vào bước kiểm tra tiếp theo.  
   * Code :  
   ```  
    def firsthandling(a):
      for i in simpleprime:
        ìf a == 1:
          return True
        if a%i == 0:
          return False
      return True
   ```
 * Fermat nhỏ : khẳng định rằng nếu p là 1 số nguyên tố, thì với số a nguyên bất kì ; a và p nguyên tố cùng nhau ta có công thức tính kiểm tra tính nguyên tố chắc chắn hơn : a^(p−1) ≡ 1 (modp)  
   * Code :  
   ```  
    def fermat(p,x):
      for i in range(x):
        a = simpleprimep[i]
        if thuattoan.powMod(a,p-1,p) != 1 :
          return False
        return True
   ```
 * Rabin Miller : thuật toán cao cấp nhất để sau khi qua 2 bước kiểm tra trên thì có thể 99% kiểm tra được số đó sẽ là số nguyên tố với tỉ lệ sai số rất nhỏ = 1/(ln4)^k  
   * Diễn giải thuật toán : cho N là 1 số. Gán q = N-1 (q lẻ, nếu q chẵn: q = q/2) khi t = 0 ( t = t + 1 nếu q chẵn)  
     * Ta có chia dần N-1 cho 2, ta phân tích N-1 = (2^t).q (q lẻ)  
     * gán C = 20. C là số trường hợp kiểm tra bằng Rabin Miller. C = 20 bởi vì 1 số trải qua được 20 lần kiểm tra như vậy tì 99% sẽ là số nguyên tố với tỉ lệ sai sót của kì nhỏ  
     * Tiếp theo ta chọn 1 số a ngẫu nhiên trong khoảng 1<a<N. Gán e = 0, b ≡ a^q (mod n). Ta xảy ra 2 trường hợp :  
     * TH1 : b = 1, c = c-1. Khi c > 0, chuyển lại về bước chọn a ngẫu nhiên. Còn khi c = 0. In ra là số nguyên tố  
     * TH2 : b !≡ +-1 (mod N). Ta đặt b = b^e mod N. e = e+1. Cứ tiếp tục tính với số e tăng dần lên đến khi b = 1 và c = 0  
   * Code :   
   ```  
    def RabinMiller(p,x):
      n = p - 1
      t = 0
      while n%2 == 0:
        n // 2
        t = t + 1
      a = randrange(2 ,p-1)
      x = (a ** n) % p
      if x == 1 or x == p-1:
        return True
      while t > 1:
        x = (x*x) % p
        if x == 1:
          return False
        if x == p-1:
          return True
        t -= 1
      return False
   ```
## ***Sinh số nguyên tố***  
 * Tạo hàm random 1 số bằng bao nhiêu bit và đảm bảo rằng số đó luôn luôn lẻ  
   * Code :
   ```
    def Random(b):
      a = random.getrandbits(b)
      a = a | (1 << (b-1))
      a = a | 1
      return a
   ```
 * Để sinh số ta chạy kiểm tra bằng các hàm kiểm tra tính nguyên tố ở trên, ta sẽ được 2 số có độ dài 1024 bits  
 
## ***Tạo cặp khóa***  
 * Lấy ra 2 số q và p ta vừa sinh ra  
 * Ta tính n = q*p  , e = (q-1)(p-1)
 * Lấy E sao cho (E,e) = 1  
 * Tính d là modulo đảo ngược của E, sử dụng thuật toán GCD ngược.  
 * Và ta có cặp khóa: 
   * Khóa công khai(public key): (n,E)  
   * Khóa bí mật(private key) : (n,d)  
 * [linkcode](  https://github.com/HoangNguyen242/RSA/blob/master/taokhoa.py)  
 
## ***Mã hóa RSA***  
 * Decode(mã hóa):  
   * Import thư viện base64 : dùng để chuyển thông tin bí mật thành dạng các con số  
   * Ta ghép các con số sau khi đã chuyển đổi lại ta được bản rõ P  
   * Ta mã hóa lại bằng công thức : C = P^E mod n  
   * [linkcode](https://github.com/HoangNguyen242/RSA/blob/master/mahoa.py)  
   
 * Encode(giải mã):  
   * Lấy bản mã C về từ mã hóa  
   * Lấy cặp khóa bí mật(n,d)  
   * Giải bản mã hóa C thành bản rõ P bằng công thức : P = C^d mod n  
   * Chuyển đổi bản rõ P về thông tin bí mật bằng base64  
   * [linkcode](https://github.com/HoangNguyen242/RSA/blob/master/giaima.py)  
   
 
   
