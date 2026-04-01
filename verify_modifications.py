#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证修改结果
"""

import os

def verify_modifications():
    """验证图片和演讲人筛选修改"""
    print("=" * 50)
    print("修改验证")
    print("=" * 50)
    
    html_file = 'standalone.html'
    
    if not os.path.exists(html_file):
        print("❌ 错误：找不到HTML文件")
        return False
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("📋 验证图片修改：")
    
    # 检查图片CSS样式（无边框和阴影）
    if 'box-shadow: var(--shadow-2)' in content:
        print("❌ 图片CSS：仍然有阴影效果")
        css_ok = False
    else:
        print("✅ 图片CSS：已移除阴影效果")
        css_ok = True
    
    if 'border: 1px solid var(--surface-variant)' in content:
        print("❌ 图片CSS：仍然有边框")
        border_ok = False
    else:
        print("✅ 图片CSS：已移除边框")
        border_ok = True
    
    print("\n📋 验证演讲人筛选顺序：")
    
    # 检查演讲人顺序
    analysts_order = []
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        if 'analyst-card' in line and 'handleSpeakerFilter' in line:
            # 提取演讲人名字
            start = line.find("handleSpeakerFilter('") + len("handleSpeakerFilter('")
            end = line.find("')", start)
            if end > start:
                name = line[start:end]
                analysts_order.append(name)
    
    # 过滤掉"null"（全部）
    analysts_order = [name for name in analysts_order if name and name != 'null']
    
    expected_order = ['胡咏嘉', '王天奇', '梁雅静', '赵雅韵', '施琪', '张晴']
    
    print(f"当前顺序: {analysts_order}")
    print(f"期望顺序: {expected_order}")
    
    if analysts_order == expected_order:
        print("✅ 演讲人顺序：正确")
        order_ok = True
    else:
        print("❌ 演讲人顺序：不正确")
        order_ok = False
    
    print(f"\n📋 验证胡咏嘉头像：")
    
    # 检查胡咏嘉头像是否使用图片
    if 'analyst-card" onclick="handleSpeakerFilter(\'胡咏嘉\')"' in content:
        after_huyongjia = content.split('analyst-card" onclick="handleSpeakerFilter(\'胡咏嘉\')"')[1][:200]
        if 'img-avatar img-huyongjia' in after_huyongjia:
            print("✅ 胡咏嘉头像：使用图片样式")
            huyongjia_ok = True
        else:
            print("❌ 胡咏嘉头像：未使用图片样式")
            huyongjia_ok = False
    else:
        print("❌ 未找到胡咏嘉的卡片")
        huyongjia_ok = False
    
    print("\n" + "=" * 50)
    all_ok = css_ok and border_ok and order_ok and huyongjia_ok
    
    if all_ok:
        print("✅ 所有修改验证通过！")
        print("\n📝 修改总结：")
        print("1. 图片已移除边框和阴影")
        print("2. 演讲人筛选顺序已调整为：胡咏嘉 → 王天奇 → 梁雅静 → 赵雅韵 → 施琪 → 张晴")
        print("3. 胡咏嘉头像已使用图片样式")
    else:
        print("❌ 部分修改未通过验证")
    
    print("=" * 50)
    
    return all_ok

def main():
    verify_modifications()

if __name__ == '__main__':
    main()