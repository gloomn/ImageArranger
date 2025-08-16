import os
from datetime import datetime
from tkinter import Tk, filedialog, messagebox

def rename_date_folders(folder_path):
    """폴더 이름이 yyyy-mm-dd 형식이면 [yyyy년 mm월 dd일]로 바꿈"""
    changed = 0
    for name in os.listdir(folder_path):
        full_path = os.path.join(folder_path, name)
        if os.path.isdir(full_path):
            try:
                # yyyy-mm-dd 형식인지 확인
                date_obj = datetime.strptime(name, "%Y-%m-%d")
                new_name = date_obj.strftime("[%Y년 %m월 %d일]")
                new_path = os.path.join(folder_path, new_name)

                # 이름이 다르면 변경
                if full_path != new_path:
                    os.rename(full_path, new_path)
                    changed += 1
            except ValueError:
                # 날짜 형식이 아니면 무시
                continue

    return changed

def main():
    root = Tk()
    root.withdraw()  # 기본 창 숨기기
    folder_path = filedialog.askdirectory(title="폴더 이름을 변환할 상위 폴더를 선택하세요")
    if folder_path:
        changed = rename_date_folders(folder_path)
        if changed:
            messagebox.showinfo("완료", f"{changed}개의 폴더 이름이 변환되었습니다!")
        else:
            messagebox.showinfo("알림", "변경할 yyyy-mm-dd 형식의 폴더가 없습니다.")

if __name__ == "__main__":
    main()
