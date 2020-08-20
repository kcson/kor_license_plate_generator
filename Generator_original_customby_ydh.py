import os, random
import cv2, argparse
import numpy as np

def random_bright(img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    img = np.array(img, dtype=np.float64)
    random_bright = .5 + np.random.uniform()
    img[:, :, 2] = img[:, :, 2] * random_bright
    img[:, :, 2][img[:, :, 2] > 255] = 255
    img = np.array(img, dtype=np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    return img

class ImageGenerator:
    def __init__(self, save_path):
        self.save_path = save_path
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        # Plate
        self.new_plate1 = cv2.imread("new_plate1.png")
        self.new_plate2 = cv2.imread("new_plate2.png")
        self.new_plate3 = cv2.imread("new_plate3.png")
        self.new_plate4 = cv2.imread("new_plate4.png")
        self.new_plate5 = cv2.imread("new_plate5.png")
        self.new_plate6 = cv2.imread("new_plate6.png")
        self.new_plate7 = cv2.imread("new_plate7.png")
        self.new_plate8 = cv2.imread("new_plate8.png")

        # loading Number
        file_path = "./num/"
        file_list = os.listdir(file_path)
        self.Number = list()
        self.number_list = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Number.append(img)
            self.number_list.append(file[0:-4])

        #load reverse Number
        file_path = "./num_r/"
        file_list = os.listdir(file_path)
        self.Number_r = list()
        self.number_list_r = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            img_r = cv2.bitwise_not(img)
            self.Number_r.append(img_r)
            self.number_list_r.append(file[0:-4])

        
        # loading Char
        file_path = "./char1/"
        file_list = os.listdir(file_path)
        self.char_list = list()
        self.Char1 = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Char1.append(img)
            self.char_list.append(file[0:-4])

        # loading reverse char
        file_path = "./char1_r/"
        file_list = os.listdir(file_path)
        self.char_list_r = list()
        self.Char1_r = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            img_r = cv2.bitwise_not(img)
            self.Char1_r.append(img)
            self.char_list_r.append(file[0:-4])

        # loading reverse Region
        file_path = "./region_r/"
        file_list = os.listdir(file_path)
        self.Region_r = list()
        self.region_list_r = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Region_r.append(img)
            self.region_list_r.append(file[0:-4])
       
        # loading Region
        file_path = "./region_ry/"
        file_list = os.listdir(file_path)
        self.Region_ry = list()
        self.region_list_ry = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Region_ry.append(img)
            self.region_list_ry.append(file[0:-4])
        #=========================================================================

    # 일반 흰색 2자리 번호판
    def Type_1(self, num, save=False):
        number = [cv2.resize(number, (56, 83)) for number in self.Number]
        char = [cv2.resize(char1, (60, 83)) for char1 in self.Char1]
        Plate = cv2.resize(self.new_plate1,(520,110))

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.new_plate1, (520,110))
            label = "Z"
            # row -> y , col -> x
            row, col = 13, 35  # row + 83, col + 56
            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            #Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # character 3
            label += self.char_list[i%37]
            #Plate[row:row + 83, col:col + 60, :] = char[i%37]
            Plate[row:row + 83, col:col + 60, :] = char[i%37]
            col += (60 + 36)

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            #Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            #Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            #Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            #Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56
            #Plate = random_bright(Plate)
            Plate = random_bright(Plate)
            # 2자리 번호판 맨뒤에label 전용 X 삽입
            if save:
                #cv2.imwrite(self.save_path + label + "X.jpg", Plate)
                cv2.imwrite(self.save_path + label + "X.jpg", Plate)
                
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    # 흰색 2자리 번호판 , 현대
    def Type_2(self, num, save=False):
        number = [cv2.resize(number, (56, 83)) for number in self.Number]
        char = [cv2.resize(char1, (60, 83)) for char1 in self.Char1]
        Plate =  Plate = cv2.resize(self.new_plate2,(520,110))

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.new_plate2, (520,110))
            label = "Z"
            # row -> y , col -> x
            row, col = 13, 35  # row + 83, col + 56
            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # character 3
            label += self.char_list[i%37]
            Plate[row:row + 83, col:col + 60, :] = char[i%37]
            col += (60 + 36)

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56
            Plate = random_bright(Plate)
            # 2자리 번호판 맨뒤에 X 삽입
            if save:
                #cv2.imwrite(self.save_path + label + "X.jpg", Plate)
                cv2.imwrite(self.save_path + label + "X.jpg", Plate)
                
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
    # 흰색 2자리 번호판, 현대
    def Type_3(self, num, save=False):
        number = [cv2.resize(number, (56, 83)) for number in self.Number]
        char = [cv2.resize(char1, (60, 83)) for char1 in self.Char1]
        Plate =  Plate = cv2.resize(self.new_plate3,(520,110))

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.new_plate3, (520,110))
            label = "Z"
            # row -> y , col -> x
            row, col = 13, 35  # row + 83, col + 56
            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # character 3
            label += self.char_list[i%37]
            Plate[row:row + 83, col:col + 60, :] = char[i%37]
            col += (60 + 36)

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56
            Plate = random_bright(Plate)
            # 2자리 번호판 맨뒤에 X 삽입
            if save:
                #cv2.imwrite(self.save_path + label + "X.jpg", Plate)
                cv2.imwrite(self.save_path + label + "X.jpg", Plate)
                
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
    # 흰색 2자리 번호판 (기아)
    def Type_4(self, num, save=False):
        number = [cv2.resize(number, (56, 83)) for number in self.Number]
        char = [cv2.resize(char1, (60, 83)) for char1 in self.Char1]
        Plate =  Plate = cv2.resize(self.new_plate4,(520,110))

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.new_plate4, (520,110))
            label = "Z"
            # row -> y , col -> x
            row, col = 13, 35  # row + 83, col + 56
            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # character 3
            label += self.char_list[i%37]
            Plate[row:row + 83, col:col + 60, :] = char[i%37]
            col += (60 + 36)

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56
            Plate = random_bright(Plate)
            # 2자리 번호판 맨뒤에 X 삽입
            if save:
                #cv2.imwrite(self.save_path + label + "X.jpg", Plate)
                cv2.imwrite(self.save_path + label + "X.jpg", Plate)
                
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    # 흰색 배경 ,까만 글씨, 위 두줄 
    def Type_5(self, num, save=False):
        number = [cv2.resize(number, (38, 83)) for number in self.Number]
        char = [cv2.resize(char1, (40, 70)) for char1 in self.Char1]
        Plate = cv2.resize(self.new_plate5, (355, 155))

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.new_plate5, (355, 155))
            label = "Z"
            row, col = 46, 10  # row + 83, col + 56

            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 38, :] = number[rand_int]
            col += 45

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 38, :] = number[rand_int]
            col += 45

            # character 3
            label += self.char_list[i%37]
            Plate[row + 12:row + 82, col + 2:col + 40 + 2, :] = char[i%37]
            col += 49 + 2

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col + 2:col + 38 + 2, :] = number[rand_int]
            col += 45 + 2

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 38, :] = number[rand_int]
            col += 45

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 38, :] = number[rand_int]
            col += 45

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 38, :] = number[rand_int]
            col += 45
            Plate = random_bright(Plate)
            if save:
                cv2.imwrite(self.save_path + label + "X.jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
    #초록색 배경 -> 까만색 배경에 흰색 숫자, 지역이름과 번호까지 있음.
    def Type_6(self, num, save=False):
        number1 = [cv2.resize(number, (44, 60)) for number in self.Number_r]
        number2 = [cv2.resize(number, (64, 90)) for number in self.Number_r]
        region = [cv2.resize(region, (88, 60)) for region in self.Region_r]
        char = [cv2.resize(char, (64, 62)) for char1 in self.Char1_r]

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.new_plate6, (336, 170))

            label = str()
            # row -> y , col -> x
            row, col = 8, 76

            # region
            label += self.region_list_r[i % 16]
            Plate[row:row + 60, col:col + 88, :] = region[i % 16]
            col += 88 + 8

            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list_r[rand_int]
            Plate[row:row + 60, col:col + 44, :] = number1[rand_int]
            col += 44

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 60, col:col + 44, :] = number1[rand_int]

            row, col = 72, 8

            # character 3
            label += self.char_list[i % 37]
            Plate[row:row + 62, col:col + 64, :] = char[i % 37]
            col += 64

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            col += 64

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            col += 64

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            col += 64

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            Plate = random_bright(Plate)
            if save:
                cv2.imwrite(self.save_path + label + "X.jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    # 지역이름은 없고, 번호만 있음. 02무 , 초록색 2자리 번호판 (흰색 글씨)
    def Type_7(self, num, save=False):
        number1 = [cv2.resize(number, (44, 60)) for number in self.Number_r]
        number2 = [cv2.resize(number, (64, 90)) for number in self.Number_r]
        region = [cv2.resize(region, (88, 60)) for region in self.Region_r]
        char = [cv2.resize(char1, (64, 62)) for char1 in self.Char1_r]

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.new_plate7, (336, 170))

            label = str()
            # row -> y , col -> x
            row, col = 8, 76

            # resion
            label += self.region_list_r[i % 16]
            Plate[row:row + 60, col:col + 88, :] = region[i % 16]
            col += 88 + 8

            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list_r[rand_int]
            Plate[row:row + 60, col:col + 44, :] = number1[rand_int]
            col += 44

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list_r[rand_int]
            Plate[row:row + 60, col:col + 44, :] = number1[rand_int]

            row, col = 72, 8

            # character 3
            label += self.char_list_r[i % 37]
            Plate[row:row + 62, col:col + 64, :] = char[i % 37]
            col += 64

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list_r[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            col += 64

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list_r[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            col += 64

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list_r[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            col += 64

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list_r[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            Plate = random_bright(Plate)
            if save:
                cv2.imwrite(self.save_path + label + "X.jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()


    def Type_8(self, num, save=False):
        number1 = [cv2.resize(number, (60, 65)) for number in self.Number_r]
        number2 = [cv2.resize(number, (80, 90)) for number in self.Number_r]
        char = [cv2.resize(char1, (60, 65)) for char1 in self.Char1_r]

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.plate5, (336, 170))
            random_width, random_height = 336, 170
            label = "Z"

            # row -> y , col -> x
            row, col = 8, 78

            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 65, col:col + 60, :] = number1[rand_int]
            col += 60

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 65, col:col + 60, :] = number1[rand_int]
            col += 60

            # character 3
            label += self.char_list_g[i%37]
            Plate[row:row + 65, col:col + 60, :] = char[i%37]
            row, col = 75, 8

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 80, :] = number2[rand_int]
            col += 80


            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 80, :] = number2[rand_int]
            col += 80

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 80, :] = number2[rand_int]
            col += 80

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 80, :] = number2[rand_int]

            Plate = random_bright(Plate)

            if save:
                cv2.imwrite(self.save_path + label + "X.jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
    
    # 3자리 번호판 
    def Type_9(self, num, save=False):
        number = [cv2.resize(number, (56, 83)) for number in self.Number]
        char = [cv2.resize(char1, (60, 83)) for char1 in self.Char1]
        Plate = cv2.resize(self.plate1, (520+56, 110))

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.plate, (520+56, 110))
            label = "Z"
            # row -> y , col -> x
            row, col = 13, 35  # row + 83, col + 56
            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 3
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # character 3
            label += self.char_list[i%37]
            Plate[row:row + 83, col:col + 60, :] = char[i%37]
            col += (60 + 36)

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56
            Plate = random_bright(Plate)
            if save:
                cv2.imwrite(self.save_path + label + ".jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()


    def Type_10(self, num, save=False):
        number = [cv2.resize(number, (45, 83)) for number in self.Number]
        char = [cv2.resize(char1, (49, 70)) for char1 in self.Char1]
        Plate = cv2.resize(self.plate, (355+45, 155))

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.plate, (355+45, 155))
            label = "Z"
            row, col = 46, 10  # row + 83, col + 56

            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45

            # number 3
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45

            # character 4
            label += self.char_list[i%37]
            Plate[row + 12:row + 82, col + 2:col + 49 + 2, :] = char[i%37]
            col += 49 + 2

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col + 2:col + 45 + 2, :] = number[rand_int]
            col += 45 + 2

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45
            Plate = random_bright(Plate)
            if save:
                cv2.imwrite(self.save_path + label + ".jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()


    def Type_11(self, num, save=False):
        number = [cv2.resize(number, (56, 83)) for number in self.Number_y]
        resion = [cv2.resize(resion, (88, 60)) for resion in self.Resion_y]
        char = [cv2.resize(char1, (60, 83)) for char1 in self.Char1_y]

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.plate2, (520+56, 110))
            label = "Z"
            # row -> y , col -> x
            row, col = 13, 35  # row + 83, col + 56
            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 3
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # character 3
            label += self.char_list_y[i%37]
            Plate[row:row + 83, col:col + 60, :] = char[i%37]
            col += (60 + 36)

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56
            Plate = random_bright(Plate)
            if save:
                cv2.imwrite(self.save_path + label + ".jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()


    def Type_12(self, num, save=False):
        number = [cv2.resize(number, (45, 83)) for number in self.Number_y]
        char = [cv2.resize(char1, (49, 70)) for char1 in self.Char1_y]
        Plate = cv2.resize(self.plate2, (355+45, 155))

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.plate2, (355+45, 155))
            label = "Z"
            row, col = 46, 10  # row + 83, col + 56

            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45

            # number 3
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45

            # character 4
            label += self.char_list_y[i%37]
            Plate[row + 12:row + 82, col + 2:col + 49 + 2, :] = char[i%37]
            col += 49 + 2

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 83, col + 2:col + 45 + 2, :] = number[rand_int]
            col += 45 + 2

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45
            Plate = random_bright(Plate)
            if save:
                cv2.imwrite(self.save_path + label + ".jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()



parser = argparse.ArgumentParser()
parser.add_argument("-i", "--img_dir", help="save image directory",
                    type=str, default="../DB/train/")
parser.add_argument("-n", "--num", help="number of image",
                    type=int)
parser.add_argument("-s", "--save", help="save or imshow",
                    type=bool, default=True)
args = parser.parse_args()


img_dir = args.img_dir
A = ImageGenerator(img_dir)

num_img = args.num
Save = args.save
'''
A.Type_1(num_img, save=Save)
print("Type 1 finish")
A.Type_1_2(num_img, save=Save)
print("Type 1_2 finish")
A.Type_1_3(num_img, save=Save)
print("Type 1_3 finish")
A.Type_1_4(num_img, save=Save)
print("Type 1_4 finish")
'''
A.Type_1(num_img, save=Save)
print("Type 1 finish")
A.Type_2(num_img, save=Save)
print("Type 2 finish")
A.Type_3(num_img, save=Save)
print("Type 3 finish")
A.Type_4(num_img, save=Save)
print("Type 4 finish")
A.Type_5(num_img, save=Save)
print("Type 5 finish")

A.Type_6(num_img, save=Save)
print("Type 6 finish")
A.Type_7(num_img, save=Save)
print("Type 7 finish")
'''
A.Type_8(num_img, save=Save)
print("Type 8 finish")
A.Type_9(num_img, save=Save)
print("Type 9 finish")
'''