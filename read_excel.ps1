$excelPath = "c:\Users\Thea\WorkBuddy\20260401131958\data.xlsx"

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

$workbook = $excel.Workbooks.Open($excelPath)
$worksheet = $workbook.Sheets.Item(1)

$usedRange = $worksheet.UsedRange
$rowCount = $usedRange.Rows.Count
$colCount = $usedRange.Columns.Count

# 获取列名
$columns = @()
for ($col = 1; $col -le $colCount; $col++) {
    $columns += $usedRange.Cells.Item(1, $col).Text
}

# 获取数据
$data = @()
for ($row = 2; $row -le $rowCount; $row++) {
    $obj = @{}
    for ($col = 1; $col -le $colCount; $col++) {
        $value = $usedRange.Cells.Item($row, $col).Text
        if ($value) {
            $obj[$columns[$col-1]] = $value
        }
    }
    if ($obj.Count -gt 0) {
        $data += $obj
    }
}

$workbook.Close($false)
$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

# 输出结果
Write-Host "列名: $($columns -join ', ')"
Write-Host "`n数据条数: $($data.Count)"
Write-Host "`n前3条数据:"
for ($i = 0; $i -lt [Math]::Min(3, $data.Count); $i++) {
    Write-Host "`n第$($i+1)条:"
    $data[$i].GetEnumerator() | ForEach-Object {
        Write-Host "  $($_.Key): $($_.Value)"
    }
}

# 保存为JSON
$json = $data | ConvertTo-Json -Depth 10
$json | Out-File -FilePath "data.json" -Encoding UTF8
Write-Host "`n数据已保存到 data.json"
