/**
 * 热点表格数据加载器
 * 从Excel文件中读取消费和海外热点数据
 */

// 热点表格数据
const hotspotsData = {
    consumer: [
        { topic: "春假/清明假期", themes: "酒旅、餐饮" },
        { topic: "茅台提价", themes: "白酒、大消费策略" },
        { topic: "“龙虾”出圈", themes: "AI消费、互联网" },
        { topic: "创新药BD临床", themes: "医药" },
        { topic: "地缘/油价传导", themes: "农产品" },
        { topic: "金价高波动", themes: "黄金策略" }
    ],
    overseas: [
        { topic: "中东冲突", themes: "全球权益策略" },
        { topic: "高油价影响", themes: "日、韩、巴西ETF" },
        { topic: "港股高波动", themes: "港股策略、恒生科技" },
        { topic: "美国通胀/降息节奏", themes: "美股策略" },
        { topic: "企业出海", themes: "出海专题、目的地研究" }
    ]
};

/**
 * 渲染热点列表
 * @param {string} containerId - 容器ID
 * @param {Array} data - 热点数据
 * @param {string} type - 类型 ('consumer' 或 'overseas')
 */
function renderHotspotList(containerId, data, type) {
    const container = document.getElementById(containerId);
    if (!container) return;
    
    if (!data || data.length === 0) {
        container.innerHTML = `
            <li class="hotspot-item">
                <div class="hotspot-marker ${type}"></div>
                <div class="hotspot-content">
                    <div class="hotspot-topic">暂无热点数据</div>
                    <div class="hotspot-themes"><strong>相关路演主题：</strong></div>
                </div>
            </li>
        `;
        return;
    }
    
    let html = '';
    data.forEach((item, index) => {
        html += `
            <li class="hotspot-item" data-index="${index}">
                <div class="hotspot-marker ${type}"></div>
                <div class="hotspot-content">
                    <div class="hotspot-topic">${item.topic}</div>
                    <div class="hotspot-themes"><strong>相关路演主题：</strong>${item.themes}</div>
                </div>
            </li>
        `;
    });
    
    container.innerHTML = html;
}

/**
 * 初始化热点表格
 */
function initHotspots() {
    // 渲染消费热点
    renderHotspotList('consumerHotspots', hotspotsData.consumer, 'consumer');
    
    // 渲染海外热点
    renderHotspotList('overseasHotspots', hotspotsData.overseas, 'overseas');
    
    // 添加点击事件处理
    const hotspotItems = document.querySelectorAll('.hotspot-item');
    hotspotItems.forEach(item => {
        item.addEventListener('click', function() {
            const index = this.getAttribute('data-index');
            const type = this.querySelector('.hotspot-marker').className.includes('consumer') ? '消费' : '海外';
            console.log(`点击了${type}热点 #${index}`);
            
            // 这里可以添加跳转到相关路演主题的功能
            highlightCardByHotspot(type, this.querySelector('.hotspot-topic').textContent);
        });
    });
}

/**
 * 根据热点高亮相关卡片
 * @param {string} type - 热点类型
 * @param {string} topic - 热点主题
 */
function highlightCardByHotspot(type, topic) {
    // 这里实现根据热点主题搜索相关路演主题的功能
    console.log(`搜索与${type}热点 "${topic}" 相关的路演主题`);
    
    // 在实际应用中，这里可以调用搜索功能或跳转到相关页面
}

// 页面加载时初始化热点表格
document.addEventListener('DOMContentLoaded', initHotspots);

/**
 * 导出模块
 */
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        hotspotsData,
        renderHotspotList,
        initHotspots
    };
}