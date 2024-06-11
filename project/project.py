import os
from PIL import Image
import pytesseract

# Tesseract OCR의 실행 경로를 설정 (tesseract-OCR이 설치된 경로)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 파일 경로를 입력받아 텍스트를 추출해주는 함수
def extractText(file_path):
    try:
        # 테서랙트를 이용하여 파일을 열어 텍스트를 추출
        text = pytesseract.image_to_string(Image.open(file_path), lang="kor")
        return text
    except Exception as e:
        print("에러: 텍스트 추출에 실패했습니다. 이미지 파일을 다시 확인해주세요.")
        return None

# 파일을 열어주는 함수 (CLI)
def openFileCLI():
    file_path = input("이미지 파일 경로를 입력하세요: ")
    os.system('cls')  # 화면 초기화
    showTextCLI(file_path)

# 텍스트를 CLI에 출력해주는 함수
def showTextCLI(file_path):
    text = extractText(file_path)
    if text:
        print("추출된 텍스트:\n", text)
        saveToFile(text)

# 텍스트를 파일에 저장하는 함수
def saveToFile(text):
    file_path = input("저장할 파일 경로를 입력하세요: ")
    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(text + "\n")  # 기존 파일에 이어서 내용을 추가하고 줄 바꿈 추가
        print("텍스트가 파일에 저장되었습니다.")
    except Exception as e:
        print("에러: 파일에 저장 중 오류가 발생했습니다.")

# 사용자로부터 텍스트를 입력받는 함수
def inputTextCLI():
    word = input("검색할 단어를 입력하세요: ")
    file_path = r'C:\Users\skyst\Desktop\al_project\textfile.txt'
    os.system('cls')  # 화면 초기화
    findWordInFile(word, file_path)

# 단어를 파일에서 찾아 인덱스를 출력하는 함수
def findWordInFile(word, file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        # 텍스트를 줄 단위 또는 마침표(.) 단위로 나눠 리스트에 저장
        sentences = [sentence.strip() for sentence in text.replace('\n', ' ').split('.') if sentence.strip()]
        # 입력된 단어가 포함된 문장의 인덱스를 출력
        indices = [i for i, sentence in enumerate(sentences) if word in sentence]
        if indices:
            print(f"단어 '{word}'는 다음 인덱스(문장)에 위치합니다:")
            for index in indices:
                print(f"[{index}] - {sentences[index]}")
            # 사용자가 특정 인덱스를 선택하면 해당 문장을 출력
            selected_index = int(input("출력할 인덱스를 선택하세요: "))
            if selected_index in indices:
                os.system('cls')  # 화면 초기화
                print(f"선택된 문장 [{selected_index}] - {sentences[selected_index]}")
            else:
                print("잘못된 인덱스 선택.")
        else:
            print(f"단어 '{word}'를 찾을 수 없습니다.")
    except Exception as e:
        print("에러: 파일을 읽는 중 오류가 발생했습니다.")

# CLI에서 실행하는 부분
def mainCLI():
    while True:
        print(" ㅡ" * 10)
        print("ㅣ    이미지 텍스트 추출기    ㅣ")
        print("ㅣ                            ㅣ")
        print("ㅣ [1] 이미지 열기            ㅣ")
        print("ㅣ [2] 텍스트 입력            ㅣ")
        print("ㅣ [3] 종료                   ㅣ")
        print(" ㅡ" * 10)
        choice = input("선택: ")

        os.system('cls')  # 화면 초기화
        if choice == '1':
            openFileCLI()
        elif choice == '2':
            inputTextCLI()
        elif choice == '3':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 옵션을 선택하세요.")

# CLI에서 실행
if __name__ == "__main__":
    mainCLI()