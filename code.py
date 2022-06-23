attempt = 1
while True:
  if attempt == 4:
      break
  else:
    reply = input('請輸入7位密碼')
    if reply == 'a123456':
      print('登入成功')
      break
    else:
      print('密碼錯誤 ，還有',3-attempt,'次機會')
      attempt = attempt + 1
    