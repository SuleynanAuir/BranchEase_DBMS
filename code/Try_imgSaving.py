from pywebio.input import file_upload
from pywebio.output import put_text
import os

def upload_and_save_image():
    # 提示用户选择要上传的图片文件
    uploaded_file = file_upload(label='请选择要上传的图片文件', accept='image/*')

    if uploaded_file:
        # 获取上传文件的名称和内容
        file_name = uploaded_file['filename']
        file_content = uploaded_file['content']

        # 设置保存图片的文件夹路径
        save_folder = 'uploaded_images'
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        # 保存图片到指定文件夹
        save_path = os.path.join(save_folder, file_name)
        with open(save_path, 'wb') as f:
            f.write(file_content)

        # 显示保存成功的消息
        put_text(f'图片已成功保存到 {save_path}')

if __name__ == '__main__':
    upload_and_save_image()
