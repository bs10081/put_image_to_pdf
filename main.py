import os
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PIL import Image
import pyheif

# 將 HEIC 圖片轉換為 PIL Image 格式
def convert_heic_to_pil(image_path):
    heif_file = pyheif.read(image_path)
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data, 
        "raw", 
        heif_file.mode, 
        heif_file.stride
    )
    return image

# 使用 reportlab 創建 PDF 檔案，將每個子資料夾中的圖片逐一放入 PDF
def create_pdf_for_folder(folder_path, output_pdf_path):
    c = canvas.Canvas(output_pdf_path, pagesize=A4)
    width, height = A4
    
    # 遍歷該資料夾中的所有圖片
    for image_filename in sorted(os.listdir(folder_path)):
        image_path = os.path.join(folder_path, image_filename)
        
        # 確認檔案是否為圖片 (包括 HEIC)
        try:
            if image_filename.lower().endswith(".heic"):
                # 轉換 HEIC 為 PIL Image
                img = convert_heic_to_pil(image_path)
            else:
                # 讀取其他格式的圖片
                img = Image.open(image_path)
        except IOError:
            print(f"跳過非圖片檔案: {image_filename}")
            continue
        
        # 獲取圖片尺寸以保持原始比例
        img_width, img_height = img.size
        aspect_ratio = img_width / img_height
        
        # 根據比例調整圖片在 PDF 頁面的大小
        if aspect_ratio > 1:
            # 寬度優先
            new_width = width
            new_height = width / aspect_ratio
        else:
            # 高度優先
            new_height = height
            new_width = height * aspect_ratio
        
        # 計算圖片位置，使其置中
        x_offset = (width - new_width) / 2
        y_offset = (height - new_height) / 2
        
        # 使用 ImageReader 將 PIL 圖片轉換為 reportlab 可用的格式
        img_reader = ImageReader(img)

        # 在當前頁面上放置圖片
        c.drawImage(img_reader, x_offset, y_offset, new_width, new_height, preserveAspectRatio=True)
        c.showPage()  # 新增一頁
    
    c.save()

# 主函數，讀取根資料夾中的每個子資料夾並生成 PDF
def generate_pdfs_from_folders(root_folder):
    # 將輸出資料夾設置為根資料夾中的 output 資料夾
    output_folder = os.path.join(root_folder, "output")
    
    # 確保輸出資料夾存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 遍歷根資料夾中的所有子資料夾
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        
        # 確認該路徑是否為資料夾
        if os.path.isdir(folder_path):
            output_pdf_path = os.path.join(output_folder, f"{folder_name}.pdf")
            print(f"正在生成 PDF: {output_pdf_path}")
            create_pdf_for_folder(folder_path, output_pdf_path)
            print(f"完成: {output_pdf_path}")

# 主程式入口
if __name__ == "__main__":
    # 根資料夾，包含多個子資料夾，每個子資料夾內含圖片
    root_folder = "/home/bs10081/Dropbox/Saya_AI_HW2"  # 替換為你的資料夾路徑
    
    # 開始生成 PDF
    generate_pdfs_from_folders(root_folder)  # 刪除第二個參數 output_folder
    print("所有 PDF 已生成。")
