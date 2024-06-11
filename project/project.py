import os
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extractText(file_path):
    try:
        text = pytesseract.image_to_string(Image.open(file_path), lang="kor")
        return text
    except Exception as e:
        print("에러: 텍스트 추출에 실패했습니다. 이미지 파일을 다시 확인해주세요.")
        return None

def openFileCLI():
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

def showTextCLI(file_path):
    text = extractText(file_path)
    if text:
        print("추출된 텍스트:\n", text)
        saveToFile(text)

def saveToFile(text):
    file_path = "textfile.txt"
    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(text + "\n")
        print("텍스트가 파일에 저장되었습니다.")
    except Exception as e:
        print("에러: 파일에 저장 중 오류가 발생했습니다.")

def inputTextCLI():
    word = input("검색할 단어를 입력하세요: ")
    file_path = "textfile.txt"
    os.system('cls')  # 화면 초기화
    findWordInFile(word, file_path)

# 보이어-무어 알고리즘을 사용하여 문자열 탐색
def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    
    if m == 0:
        return -1
    
    skip = {}
    for i in range(m - 1):
        skip[pattern[i]] = m - i - 1
    
    i = m - 1
    while i < n:
        j = m - 1
        k = i
        while j >= 0 and text[k] == pattern[j]:
            j -= 1
            k -= 1
        if j == -1:
            return k + 1
        if text[i] in skip:
            i += skip[text[i]]
        else:
            i += m

    return -1

def findWordInFile(word, file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        
        printed_header = False
        indices = []
        index_count = 1
        
        # 보이어-무어 알고리즘을 사용하여 문자열 탐색
        idx = boyer_moore(text, word)
        
        # 탐색 결과 출력
        if idx != -1:
            sentences = text.split('\n')
            for index, sentence in enumerate(sentences):
                if word in sentence:
                    if not printed_header:
                        print(f"단어 '{word}'는 해당 인덱스(문장)에 위치합니다:")
                        printed_header = True
                    print(f"[{index_count}] - {sentence}")
                    indices.append(index)
                    index_count += 1
            if indices:
                selected_index = int(input("출력할 인덱스를 선택하세요: "))
                if selected_index in range(1, len(indices) + 1):
                    os.system('cls')
                    print(f"선택된 문장 [{selected_index}] - {sentences[indices[selected_index - 1]]}")
                else:
                    os.system('cls')
                    print("잘못된 인덱스 선택.")
        else:
            print(f"단어 '{word}'를 찾을 수 없습니다.")
            
    except Exception as e:
        print("에러: 파일을 읽는 중 오류가 발생했습니다.")

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

if __name__ == "__main__":
    mainCLI()