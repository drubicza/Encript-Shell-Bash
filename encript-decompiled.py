import os, sys, fileinput, time, socket, random, time, sys, platform, os

def tampil(x):
    w = {'m': 31, 'h': 32, 'k': 33, 'b': 34, 'p': 35, 'c': 36}
    for i in w:
        x = x.replace('\r%s' % i, '\x1b[%s;1m' % w[i])

    x += '\x1b[0m'
    x = x.replace('\r0', '\x1b[0m')
    print x


N = '\x1b[0m'
D = '\x1b[90m'
W = '\x1b[1;37m'
B = '\x1b[1;34m'
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
C = '\x1b[1;36m'
ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '\xe2\x88\x9a' + G + '] '
eror = R + '[' + W + '!' + R + ']'
print
print '\x1b[91m _____ _      ____  ____  _  ____  _____'
print '\x1b[91m*  __****  *|*   _**  __** **  __**__ __*'
print '\x1b[91m|  *  | |* |||  *  |  **|| ||  **|  * *'
print '\x1b[91m|  /_ | | \\|||  \\_ |    /| ||  __/  | |'
print '\x1b[91m\\____\\_/  \\|\\____/\\_/\\_\\_/\\_/     \\_/'
print '                                 \x1b[91m*\x1b[95mScipt Bash'
print
print '\x1b[94m===================== \x1b[91m====================='
print
print '\x1b[91m[1]\x1b[97mEncript   #\x1b[92mAuthor   :\x1b[36;1mAsecC|~|eror404'
print '\x1b[91m[0]\x1b[97mKeluar    #\x1b[92mTeam     :\x1b[36;1mHaxID'
print '             #\x1b[92mgithub   :\x1b[36;1mhttps://github.com/muhammadfathul'
print '             #\x1b[92mFacebook :\x1b[36;1mhttps://www.facebook.com/komaro.bae'
print
print '\x1b[92m===================== \x1b[95m====================='
print

def keluar():
    tampil('\rm[!]BY~~~HaxID')
    os.sys.exit()


def dekrip():
    try:
        sc = raw_input(ask + W + 'Masukan Alamat Script ' + G + '> ' + W)
        f = open(sc, 'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace('eval', 'echo')
        out = raw_input(ask + W + 'Masukan Alamat Output' + G + ' > ' + W)
        f = open(out, 'w')
        f.write(newdata)
        f.close()
        os.system('touch decript.sh')
        os.system('bash ' + out + ' > decript.sh')
        os.remove(out)
        os.rename('tes.sh', out)
        print sukses + 'Berhasil..'
    except KeyboardInterrupt:
        print eror + ' Berhenti!'
    except IOError:
        print eror + ' File Tidak Terdeteksi!'


def enkrip():
    try:
        script = raw_input(ask + W + 'Masukan Alamat Script ' + G + '|> ' + W)
        output = raw_input(ask + W + 'Masukan Alamat Output ' + G + '|> ' + W)
        os.system('bash-obfuscate ' + script + ' -o ' + output)
        print sukses + 'Berhasil..'
    except KeyboardInterrupt:
        print eror + ' Berhenti!'
    except IOError:
        print eror + ' File Tidak Terdeteksi!'


takok = raw_input(W + 'Encript' + G + ' |> ')
if takok == '1' or takok == '01':
    enkrip()
elif takok == '2' or takok == '02':
    dekrip()
elif tatok == '0' or tatok == '00':
    keluar()
else:
    print eror + ' Wrong input'
    keluar()
