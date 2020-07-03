from PIL import Image

mapper = [[(255, 255, 255, 255), 0],
          [(  0,   0,   0, 255), 2],
          [(255, 255,   0, 255), 3],
          [(  0, 255,   0, 255), 4],
          [(255,   0,   0, 255), 5]]

imageName = input("Name of the file: ")
imageExtension = input("Extension of the file: ")

image = Image.open(imageName+"."+imageExtension)
pixels = image.load()

def index2d(ref):
    for valMap in mapper:
        if ref in valMap:
            return(valMap[1])
    print("Value not added to mapper list. Please add this value: " + str(ref))
    return(-1)

width, height = image.size

with open(imageName+".map", "w") as f:
    for h in range(height):
        s=""
        for w in range(width):
            s+=str(index2d(pixels[w,h]))+" "
        f.write(s[0:-1]+"\n") if h!=height-1 else f.write(s[0:-1])
