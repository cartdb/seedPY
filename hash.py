import hashlib
import zlib
import sys
file = sys.argv[1]
file = open(file, "rb")
file = file.read()
print("ADLER32:" + hex(zlib.adler32(file)).replace("0x", ""))
print("CRC32:" + hex(zlib.crc32(file)).replace("0x", ""))
print("MD5:" + hashlib.md5(file).hexdigest())
print("SHA1:" + hashlib.sha1(file).hexdigest())
print("SHA224:" + hashlib.sha224(file).hexdigest())
print("SHA256:" + hashlib.sha256(file).hexdigest())
print("SHA384:" + hashlib.sha384(file).hexdigest())
print("SHA512:" + hashlib.sha512(file).hexdigest())
