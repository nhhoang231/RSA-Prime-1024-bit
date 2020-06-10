dig ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-+"
def getId(ch):
	if ch == '-':
		return 62
	if ch == '+':
		return 63
	if ch <= '9':
		return int(ch)
	if ch <= 'Z':
		return ord(ch) - ord('A') + 10
	return ord(ch) - ord('a') + 36

def toBase(a, base):
	r = ""
	while a != 0:
		r+=dig[a % base]
		a //= base
	r = r[::-1]
	return r;

def toInt(r, base):
	a = 0;
	for i in r:
		a*= base
		a+= getId(i)
	return a
