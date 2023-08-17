function doGet(e) {
  var SpreadSheet = SpreadsheetApp.getActive();
  var params = e.parameter;                           // 讀取網址參數
  var name = params.name || '工作表1';                 // 如果有 name 就使用，否則 name 等於「工作表1」
  var SheetName = SpreadSheet.getSheetByName(name) ;  // 讀取工作表名稱為 name 的資料
  var start_row = params.start_row || 1;              // 如果有 start_row 就使用，否則 start_row 等於 1
  var start_col = params.start_col || 1;              // 如果有 start_row 就使用，否則 start_col 等於 1
  var row = params.row || SheetName.getLastRow() - start_row + 1;   // 如果有 row 就使用，否則 row 等於 SheetName.getLastRow()
  var col = params.col|| SheetName.getLastColumn() - start_col + 1; // 如果有 col 就使用，否則 col 等於 SheetName.getLastColumn()
  var data = SheetName.getSheetValues(start_row,start_col,row,col);  // 使用變數
  Logger.log(data)
  return ContentService.createTextOutput(JSON.stringify(data)).setMimeType(ContentService.MimeType.JSON); 
}

