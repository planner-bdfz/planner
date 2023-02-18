from PIL import Image

img_circle = Image.open("assets/ico/a.png").convert('RGBA')
for i in range(36):
    img_base = Image.open("assets/ico/empty.png").convert('RGBA')
    c = img_circle.rotate(i * 10).convert('RGBA')
    r, g, b, a = c.split()
    img_base.paste(c, (0, 0, 1024, 1024), mask=a)
    file = "src/ico/loading/"+str(i)+".png"
    img_base.save(file)
    print(i)