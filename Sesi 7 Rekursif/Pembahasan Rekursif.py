def tampilanangka(batas, i = 1):
    print(f'Data ke {i}')

tampilanangka(3)
tampilanangka(3, 2)
tampilanangka(3, 3)

print(30*"-")

def nampilangka(batas, i = 1):
    print(f'perulangan ke {i}')
    if i < batas:
        nampilangka(batas, i + 1)     # proses rekursif terjadi

nampilangka(10)

print(30*"-")

def tebalikangka(batas, i = 1):
    if i < batas:
        tebalikangka(batas, i + 1)
    print(f'perulangan ke {i}')

tebalikangka(10)