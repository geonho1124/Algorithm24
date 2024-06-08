import tkinter as tk
from tkinter import filedialog

from PIL import Image, ImageTk
import pytesseract

# Tesseract OCR의 실행 경로를 설정 (tesseract-OCR이 설치된 경로)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 파일을 열어주는 함수 (UI)
def openFile():
    # filedialog = 파일을 선택할 수 있게 해주는 것
    # askopenfilename() = 파일 선택창을 열고 사용자가 파일을 선택하도록 함 선택하면 해당 파일의 경로를 반환해줌(여기서는 file_path라는 변수에 경로를 지정해주는 것임)
    file_path = filedialog.askopenfilename()

    # 변수에 저장된 값이 비어있지 않은지 확인하는 것임(선택하였을때만 실행됨)
    if file_path:
        showImage(file_path)        # 이미지 추출 함수 호출
        showText(file_path)         # 글자 추출 함수 호출

#파일 이미지를 보여주는 함수 (UI)
def showImage(file_path):
    try:
        # 선택된 파일 경로에서 이미지를 열고이것은 PIL라이브러리의 Image 모듈을 사용하여 이미지를 열어 image 변수에 저장
        image = Image.open(file_path)

        # 이미지의 크기를 300x300 픽셀로 조절(tkinter창에 맞게 표시하기 위한 것임)
        image = image.resize((300, 300))

        # ImageTk사용하여 image변수를 tkinter에서 사용가능한 PhotoImage로 변환시켜셔(변환시켜주지 않으면 안됨) photo변수에 저장
        photo = ImageTk.PhotoImage(image)

        # Label 위젯에 이미지를 설정(이미지가 들어갈 틀을 만들어준거임)
        label.config(image=photo)

        # 그안에 불러온 이미지를 넣어주는것임
        label.image = photo

    # 이미지를 츌력하던중 예외가 발생하면 잡아서 처해주는 것임(어떤 예외가 발생하든 다 잡아줌)
    except Exception as e:
        print("에러: 이미지 출력 중 오류가 발생했습니다")

# 텍스트 추출후 출력해주는 함수 (OCR 기능)
def showText(file_path):
    try:
        # 테서랙트를 이용하여 파일을 열어 영어텍스트를 추출해줌(lang="eng")가 영어만 추출해준다는 말임 추출된 텍스트는 text변수에 저장
        text = pytesseract.image_to_string(Image.open(file_path), lang="kor")

        # 텍스트에 값이 들어왔는지 확인하는 것 들어와야 실행됨
        if text:
            # 출력
            print("추출된 텍스트:\n", text)

    # 텍스트를 추출하던중 예외가 발생하면 잡아서 처해주는 것임(어떤 예외가 발생하든 다 잡아줌)
    except Exception as e:
        print("에러: 텍스트 추출 중 오류가 발생했습니다")

# Tkinter 창 생성 (UI)
root = tk.Tk()
root.title("이미지 표시")

# 이미지를 표시할 라벨 (UI)
label = tk.Label(root)
label.pack(pady=10)

# 이미지 열기 버튼 (UI)
open_button = tk.Button(root, text="이미지 열기", command=openFile)
open_button.pack(pady=10)

# Tkinter 이벤트 루프 시작 (UI)
root.mainloop()