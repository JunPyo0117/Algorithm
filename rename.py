import os
import re

def rename_items(directory='.'):
    # 현재 디렉토리의 모든 항목을 가져옴
    items = os.listdir(directory)
    
    # 모든 항목에 대해 처리
    for item in items:
        full_path = os.path.join(directory, item)
        
        if os.path.isdir(full_path):
            # 디렉토리인 경우
            match = re.match(r'^(\d+)\.\s*(.+)$', item)
            if match:
                number = int(match.group(1))
                rest_of_name = match.group(2)
                
                # 새로운 이름 생성 (숫자를 두 자리로 포맷팅)
                new_name = f"{number:02d}. {rest_of_name}"
                new_full_path = os.path.join(directory, new_name)
                
                # 이름이 다른 경우에만 변경
                if new_name != item:
                    try:
                        os.rename(full_path, new_full_path)
                        print(f"디렉토리 변경: {item} -> {new_name}")
                    except OSError as e:
                        print(f"오류 발생: {item} 변경 실패 - {e}")
                
                # 변경된 디렉토리 내부도 처리
                rename_items(new_full_path if new_name != item else full_path)
        
        else:
            # 파일인 경우
            match = re.match(r'^(\d+)([^\d].*)?$', item)
            if match:
                number = int(match.group(1))
                rest_of_name = match.group(2) if match.group(2) else ''
                
                # 새로운 이름 생성
                new_name = f"{number:02d}{rest_of_name}"
                new_full_path = os.path.join(directory, new_name)
                
                if new_name != item:
                    try:
                        os.rename(full_path, new_full_path)
                        print(f"파일 변경: {item} -> {new_name}")
                    except OSError as e:
                        print(f"오류 발생: {item} 변경 실패 - {e}")

if __name__ == "__main__":
    rename_items()
