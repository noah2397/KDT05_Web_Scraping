# 1. PIL 라이브러리를 이용하여 이미지를 회전하는 프로그램 작성

# 클래스 ImageProcess의 내부 메소드로 아래의 각 기능들을 구현하세요.
# - getpixel((x, y)), putpixel((x, y)), pixel) 사용
# 1) 과제5처럼 이미지를 반시계 방향으로 90도 회전시키는 메소드 구현
# - newyork-ccw90.jpg 파일 저장 및 화면 출력

# 2) 거울에 비친 이미지(mirror image)를 만드는 메소드 구현
# - Image.FLIP_LEFT_RIGHT와 동일 기능의 함수 구현
# - newyork-mirror.jpg 파일 저장 및 화면 출력

# 3) 아래, 위가 바뀐 이미지(mirror image)를 만드는 메소드 구현
# - Image.FLIP_TOP_BOTTOM과 동일 기능의 함수 구현

# newyork-flipy.jpg 파일 저장 및 화면 출력
# 24.02.15 정창수 교수님 감사했습니다!
from PIL import Image

class ImageProcess:
    def __init__(self, image):
        self.image = image
        self.pixels=[[0 for i in range(self.image.size[0])] for _ in range(self.image.size[1])]
        
    def getpixel(self):
        width, height = self.image.size
        for i in range(height):
            for j in range(width):
                pixel = self.image.getpixel((j, i)) 
                self.pixels[i][j]=pixel

    def ccw90(self):
        width, height = self.image.size
        new_image = Image.new("RGB", (height,width), "white")
        for i in range(height):
            for j in range(width):
                x,y,z=self.pixels[i][width-j-1]
                new_image.putpixel((i,j), (x,y,z))
        return new_image

    def mirror(self):
        width, height = self.image.size
        new_image = Image.new("RGB", (width,height), "white")
        for i in range(height):
            for j in range(width):
                x,y,z=self.pixels[i][width-j-1]
                new_image.putpixel((j,i), (x,y,z))
        return new_image
    
    def flipy(self):
        width, height = self.image.size
        new_image = Image.new("RGB", (width,height), "white")
        for i in range(height):
            for j in range(width):
                x,y,z=self.pixels[height-i-1][j]
                new_image.putpixel((j,i), (x,y,z))
        return new_image
    
    
    
if __name__ == "__main__":
    test=ImageProcess(Image.open("newyork.jpg"))
    test.getpixel()
    #1 이미지를 반시계 방향으로 90도 회전시키는 메소드 구현
    output=test.ccw90()
    output.save('newyork-ccs90.jpg')
    output.show()
    
    #2 거울에 비친 이미지를 만드는 메소드 구현
    output2=test.mirror()
    output2.save('newyork-mirror.jpg')
    output2.show()

    #3 아래, 위가 바뀐 이미지를 만드는 메소드 구현
    output3=test.flipy()
    output3.save('newyork-flipy.jpg')
    output3.show()