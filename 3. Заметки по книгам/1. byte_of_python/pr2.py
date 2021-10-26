import time
import os

list = ['"C:\\Мои коды"']
target_d = 'E:\\Backup'

name = target_d + '123' + '.zip'
zip_cmd = f"zip -qr {name} {' '.join(list)}"

if os.system(zip_cmd) == 0:
    print('Команда выполнена')
else:
    print("ошибочка")

