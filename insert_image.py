#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
在HTML文件中插入图片到"更新时间"下方
"""

import os
import sys

def insert_image_after_update_time():
    """在"更新时间"下方插入图片"""
    
    # 文件路径
    html_file = 'standalone.html'
    image_file = 'image.png'
    
    # 检查HTML文件是否存在
    if not os.path.exists(html_file):
        print(f"❌ 错误：找不到HTML文件 {html_file}")
        return False
    
    # 检查图片文件是否存在
    if not os.path.exists(image_file):
        print(f"⚠️  警告：找不到图片文件 {image_file}")
        print("   请将图片文件保存为 'image.png' 并放在当前目录下")
        print("   或者修改脚本中的图片路径")
    
    print(f"📁 正在处理文件：{html_file}")
    
    try:
        # 读取HTML文件内容
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经插入过图片
        if 'update-image-container' in content:
            print("✅ 图片已经插入过了")
            return True
        
        # 定义要插入的图片HTML代码
        image_html = '''                <div class="update-image-container">
                    <img src="image.png" alt="华泰财富研究大消费团队" class="update-image">
                </div>
                
'''
        
        # 查找"更新时间"文本的位置
        update_time_text = '📅 更新时间：2026年4月</p>'
        if update_time_text not in content:
            print(f"❌ 错误：未找到'更新时间'文本")
            return False
        
        # 找到更新时间文本后的位置
        update_time_pos = content.find(update_time_text)
        if update_time_pos == -1:
            print("❌ 错误：无法定位更新时间位置")
            return False
        
        # 找到更新时间段落结束的位置
        p_end_pos = content.find('</p>', update_time_pos) + 4  # 加上</p>的长度
        
        # 插入图片HTML代码
        new_content = content[:p_end_pos] + '\n' + image_html + content[p_end_pos:]
        
        # 检查CSS中是否已经有对应的样式
        if '.update-image-container' not in new_content:
            # 添加CSS样式
            css_style = '''
        /* 更新时间下方图片样式 */
        .update-image-container {
            margin: 20px auto 25px auto;
            text-align: center;
            max-width: 800px;
        }
        
        .update-image {
            width: 100%;
            max-width: 800px;
            height: auto;
            border-radius: 12px;
            box-shadow: var(--shadow-2);
            border: 1px solid var(--surface-variant);
        }
        
        @media (max-width: 768px) {
            .update-image-container {
                margin: 15px auto 20px auto;
            }
            
            .update-image {
                max-width: 100%;
                border-radius: 8px;
            }
        }
'''
            
            # 找到style标签结束位置
            style_end_pos = new_content.find('</style>')
            if style_end_pos != -1:
                new_content = new_content[:style_end_pos] + css_style + new_content[style_end_pos:]
                print("✅ 已添加图片CSS样式")
            else:
                print("⚠️  警告：未找到</style>标签，无法添加CSS样式")
        
        # 保存修改后的文件
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✅ 图片已成功插入到'更新时间'下方")
        print("   • 图片路径：image.png")
        print("   • 图片类名：update-image")
        print("   • 容器类名：update-image-container")
        
        if os.path.exists(image_file):
            print(f"✅ 图片文件存在：{image_file}")
        else:
            print(f"⚠️  请确保图片文件 '{image_file}' 存在")
        
        return True
        
    except Exception as e:
        print(f"❌ 插入图片过程中发生错误：{e}")
        return False

def main():
    """主函数"""
    print("=" * 60)
    print("图片插入工具 - 在'更新时间'下方插入图片")
    print("=" * 60)
    
    # 显示当前目录
    current_dir = os.getcwd()
    print(f"📂 当前目录：{current_dir}")
    
    # 执行插入操作
    success = insert_image_after_update_time()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ 操作完成！")
        print("请刷新浏览器查看效果。")
        print("=" * 60)
        
        print("\n📝 使用说明：")
        print("1. 确保图片文件命名为 'image.png'")
        print("2. 将图片放在与 standalone.html 相同的目录下")
        print("3. 刷新浏览器查看插入的图片")
    else:
        print("\n" + "=" * 60)
        print("❌ 操作失败")
        print("请检查错误信息并重试。")
        print("=" * 60)

if __name__ == '__main__':
    main()