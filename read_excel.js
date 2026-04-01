import XLSX from 'xlsx';
import fs from 'fs';

const excelPath = 'F:/华泰工作/项目/260401 AI-消费路演主题/财富研究大消费26年4月可选主题.xlsx';

const workbook = XLSX.readFile(excelPath);
const sheetName = workbook.SheetNames[0];
const worksheet = workbook.Sheets[sheetName];
const data = XLSX.utils.sheet_to_json(worksheet);

console.log('列名:', Object.keys(data[0] || {}));
console.log('\n数据条数:', data.length);
console.log('\n前3条数据:');
data.slice(0, 3).forEach((item, i) => {
  console.log(`\n第${i+1}条:`);
  Object.entries(item).forEach(([key, value]) => {
    console.log(`  ${key}: ${value}`);
  });
});

fs.writeFileSync('data.json', JSON.stringify(data, null, 2), 'utf-8');
console.log('\n数据已保存到 data.json');
