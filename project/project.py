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
    # 사용자의 홈 디렉토리와 바탕화면의 경로를 결합하여 이미지 파일 탐색
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    image_files = [f for f in os.listdir(desktop_path) if f.endswith('.png') or f.endswith('.jpg')]
    print("바탕화면에 있는 이미지 파일 목록:")
    for idx, image_file in enumerate(image_files):
        print(f"[{idx + 1}] {image_file}")
    file_index = int(input("열고자 하는 이미지 파일의 번호를 입력하세요: "))
    file_name = image_files[file_index - 1]
    file_path = os.path.join(desktop_path, file_name)
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
    # 스크립트가 있는 디렉토리를 기준으로 상대경로 계산
    file_path = "textfile.txt"
    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(text + "\n")  # 기존 파일에 이어서 내용을 추가하고 줄 바꿈 추가
        print("텍스트가 파일에 저장되었습니다.")
    except Exception as e:
        print("에러: 파일에 저장 중 오류가 발생했습니다.")

# 사용자로부터 텍스트를 입력받는 함수
def inputTextCLI():
    word = input("검색할 단어를 입력하세요: ")
    # 스크립트가 있는 디렉토리를 기준으로 상대경로 계산
    file_path = "textfile.txt"
    os.system('cls')  # 화면 초기화
    findWordInFile(word, file_path)

# 단어를 파일에서 찾아 인덱스를 출력하는 함수
def findWordInFile(word, file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        # 텍스트를 줄 단위로 나누어서 리스트에 저장
        sentences = text.split('\n')
        # 입력된 단어가 포함된 문장의 인덱스를 출력
        printed_header = False  # 헤더가 출력되었는지 여부를 나타내는 변수
        indices = []  # 단어가 포함된 문장의 인덱스를 저장할 리스트
        index_count = 1  # 출력할 문자열 인덱스를 나타내는 변수
        for index, sentence in enumerate(sentences):
            if word in sentence:
                # 처음에만 단어가 있는 위치를 알리는 헤더를 출력
                if not printed_header:
                    print(f"단어 '{word}'는 해당 인덱스(문장)에 위치합니다:")
                    printed_header = True
                # 문장과 인덱스를 출력
                print(f"[{index_count}] - {sentence}")
                indices.append(index)  # 단어가 있는 문장의 인덱스를 리스트에 추가
                index_count += 1  # 출력할 문자열 인덱스 증가
        # 사용자가 선택한 인덱스를 출력
        if indices:
            selected_index = int(input("출력할 인덱스를 선택하세요: "))
            if selected_index in range(1, len(indices) + 1):
                os.system('cls')  # 화면 초기화
                print(f"선택된 문장 [{selected_index}] - {sentences[indices[selected_index - 1]]}")
            else:
                os.system('cls')  # 화면 초기화
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