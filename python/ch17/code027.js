function doGet(e) {
  var SpreadSheet = SpreadsheetApp.getActive();  // 讀取 Apps Script 所綁定的 Google Sheet
  var params = e.parameter;                      // 讀取網址參數
  var name = params.name || '工作表1';            // 如果參數有 name 就使用，否則就是工作表1
  var SheetName = SpreadSheet.getSheetByName(name); // 取得工作表內容
  var raw_data = params.data;                    // 讀取網址參數的 data 內容
  data = JSON.parse(raw_data);                   // 轉換成 json 格式
  var top = params.top || false;                 // 如果沒有設定 top 參數就使用 false
  var range;
  try{
    if(top){
      SheetName.insertRowsBefore(1,1);           // 如果 top 等於 true，從上方插入資料
      range = SheetName.getRange(1,1,1,data.length); // 設定插入資料範圍
    }
    else{
      range = SheetName.getRange(SheetName.getLastRow()+1,1,1,data.length);  // 如果 top 等於 false，從下方插入資料
    }
  }catch{
    range = SheetName.getRange(SheetName.getLastRow()+1,1,1,data.length);
  }
  range.setValues([data]) // 插入資料
  return ContentService.createTextOutput(true);
}

// 完成後部署 Apps Script，得到一串可使用 Get 方法讀取的網址。

