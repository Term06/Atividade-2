import hashlib
#Inserir a string a ser verificada na variavel string
string = "O Centro Universitário da FEI passou a fazer parte do seleto grupo que produz ciência no Brasil, quando a CAPES aprovou o primeiro curso de Mestrado em Engenharia Elétrica em 2005."
#Inserir o hash sha256 para verificar
hash256 = "da9f214449005850f4fd552238658820434c15ca06389d018b1814bb376abaa6"
#Inserir o hash md5 para verificar
hashmd5 = "2e20bfbece6fdc62de4c4bb80a77ba1f"
encoded_string = string.encode()
hash_256 = hashlib.sha256(encoded_string)
hex_dig_256 = hash_256.hexdigest()
hash_md5 = hashlib.md5(encoded_string)
hex_dig_md5 = hash_md5.hexdigest()
print("String sendo testada:\n",string)
print("\n")
if(hash256 == hex_dig_256):
  print("Hash SHA256 correto.\n")
else:
  print("Hash SHA256 errado.\n")
if(hashmd5 == hex_dig_md5):
  print("Hash MD5 correto.\n")
else:
  print("Hash MD5 errado.\n")
