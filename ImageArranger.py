import os
import shutil
from tkinter import Tk, filedialog, messagebox
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

def get_image_date(file_path):
    #이미지의 촬영 날짜(EXIF) 또는 파일 수정 날짜 반환
    try:
        image = Image.open(file_path)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                if TAGS.get(tag) == "DateTimeOriginal":
                    return datetime.strptime(value, "%Y:%m:%d %H:%M:%S").strftime("[%Y년 %m월 %d일]")
    except Exception:
        pass
    # EXIF 없으면 파일 수정 시간 사용
    return datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("[%Y년 %m월 %d일]")

def organize_images_by_date(folder_path):
    #선택한 폴더 내 이미지를 날짜별 폴더로 정리
    supported_ext = [".jpg", ".jpeg", ".png", ".heic", ".bmp"]
    files = [f for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in supported_ext]

    if not files:
        messagebox.showinfo("알림", "이미지를 찾을 수 없습니다.")
        return

    for file in files:
        file_path = os.path.join(folder_path, file)
        date_str = get_image_date(file_path)
        target_folder = os.path.join(folder_path, date_str)

        os.makedirs(target_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(target_folder, file))

    messagebox.showinfo("완료", "이미지가 날짜별로 정리되었습니다!")

def main():
    root = Tk()
    root.withdraw()  # 기본 창 숨기기
    folder_path = filedialog.askdirectory(title="이미지가 있는 폴더를 선택하세요")
    if folder_path:
        organize_images_by_date(folder_path)

if __name__ == "__main__":
    main()

