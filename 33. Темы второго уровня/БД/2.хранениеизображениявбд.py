import sqlite3 as sq

def readIMG(n):
    try:
        with open(f'{n}.png', 'rb') as f:
            return f.read()
    except IOError as e:
        print(e)
        return False

def writeimg(name, data):
    try:
        with open(name, 'wb') as f:
            f.write(data)
    except IOError as e:
        print(e)
        return False

    return True


with sq.connect('img.db') as con:
    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS yuuy (name TEXT, ava BLOB)')

    # img = readIMG('this')
    # if img:
    #     bynary = sq.Binary(img)
    #     cur.execute("INSERT INTO yuuy VALUES ('Вацап', ?)", (bynary,))

    cur.execute('SELECT ava FROM yuuy')
    img = cur.fetchone()[0]
    writeimg('out.png', img)





