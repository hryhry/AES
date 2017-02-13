import os
import time

import aes128
import tkinter as tk
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as mb

def work(input_path, way, key):
    with open(input_path, 'rb') as f:
        data = f.read()

    if way == '1':
        crypted_data = []
        temp = []
        for byte in data:
            temp.append(byte)
            if len(temp) == 16:
                crypted_part = aes128.encrypt(temp, key)
                crypted_data.extend(crypted_part)
                del temp[:]
        else:
            # padding v1
            # crypted_data.extend(temp)

            # padding v2
            if 0 < len(temp) < 16:
                empty_spaces = 16 - len(temp)
                for i in range(empty_spaces - 1):
                    temp.append(0)
                temp.append(1)
                crypted_part = aes128.encrypt(temp, key)
                crypted_data.extend(crypted_part)

        out_path = os.path.join(os.path.dirname(input_path), 'crypted_' + os.path.basename(input_path))

        # Ounput data
        with open(out_path, 'xb') as ff:
            ff.write(bytes(crypted_data))

    else:  # if way == '2'
        decrypted_data = []
        temp = []
        for byte in data:
            temp.append(byte)
            if len(temp) == 16:
                decrypted_part = aes128.decrypt(temp, key)
                decrypted_data.extend(decrypted_part)
                del temp[:]
        else:
            # padding v1
            # decrypted_data.extend(temp)

            # padding v2
            if 0 < len(temp) < 16:
                empty_spaces = 16 - len(temp)
                for i in range(empty_spaces - 1):
                    temp.append(0)
                temp.append(1)
                decrypted_part = aes128.encrypt(temp, key)
                decrypted_data.extend(crypted_part)

        out_path = os.path.join(os.path.dirname(input_path), 'decrypted_' + os.path.basename(input_path))

        # Ounput data
        with open(out_path, 'xb') as ff:
            ff.write(bytes(decrypted_data))

    time_after = time.time()

    print('New file here:', out_path)
    print('If smth wrong check the key you entered')
    mb.showinfo("Завершено", out_path)


if __name__ == '__main__':


    def btnenc(event):
        fname = askopenfilename()
        print("Start encrypting")
        print (entkey.get())
        print (fname)
        work(fname, '1', entkey.get())


    def btndec(event):
        print("Start decrypting")
        fname = askopenfilename()
        print (entkey.get())
        print (fname)
        work(fname, '2', entkey.get())

    root = tk.Tk()
    but = tk.Button(root)
    but["text"] = "Encrypt"
    but.bind("<Button-1>", btnenc)
    but.pack()
    but2 = tk.Button(root)
    but2["text"] = "decrypt"
    but2.bind("<Button-1>", btndec)
    but2.pack()
    labl = tk.Label(root)
    labl["text"]="Key:"
    labl.pack()
    entkey = tk.Entry(root, width=20, bd=3)
    entkey.pack()
    root.mainloop()

