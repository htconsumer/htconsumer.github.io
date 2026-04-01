#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证图片插入结果
"""

import os

def verify_image_insertion():
    """验证图片插入结果"""
    print("=" * 50)
    print("图片插入验证")
    print("=" * 50)
    
    html_file = 'standalone.html'
    image_file = 'image.png'
    
    # 1. 检查HTML文件是否存在
    if not os.path.exists(html_file):
        print("❌ 错误：找不到HTML文件")
        return False
    
    # 2. 检查图片HTML代码
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    checks = [
        ('图片HTML代码', 'update-image-container'),
        ('图片标签', 'src="image.png"'),
        ('图片类名', 'class="update-image"'),
        ('CSS容器样式', '.update-image-container {'),
        ('CSS图片样式', '.update-image {'),
    ]
    
    all_passed = True
    for check_name, check_value in checks:
        if check_value in content:
            print(f"✅ {check_name} - 存在")
        else:
            print(f"❌ {check_name} - 不存在")
            all_passed = False
    
    # 3. 检查图片文件
    print("\n📁 检查图片文件...")
    if os.path.exists(image_file):
        file_size = os.path.getsize(image_file)
        print(f"✅ 图片文件存在：{image_file}")
        print(f"   文件大小：{file_size} 字节")
        if file_size == 0:
            print("⚠️  警告：图片文件大小为0，可能无效")
    else:
        print(f"⚠️  警告：图片文件 {image_file} 不存在")
        print("   请将您的图片保存为 'image.png' 并放在当前目录下")
    
    return all_passed

def main():
    success = verify_image_insertion()
    
    print("\n" + "=" * 50)
    if success:
        print("✅ 验证通过！")
        print("\n📋 使用说明：")
        print("1. 确保图片文件命名为 'image.png'")
        print("2. 将图片放在与 standalone.html 相同的目录下")
        print("3. 在浏览器中打开 standalone.html")
        print("4. 图片将显示在'更新时间'下方")
        
        # 显示文件位置
        current_dir = os.getcwd()
        print(f"\n📂 文件位置：")
        print(f"   HTML文件：{current_dir}\\standalone.html")
        print(f"   图片文件：{current_dir}\\image.png")
    else:
        print("❌ 验证失败，请检查以上问题")
    
    print("=" * 50)

if __name__ == '__main__':
    main()