function doGet(e) {
  var SpreadSheet = SpreadsheetApp.getActive();         // 讀取目前的試算表
  var SheetName = SpreadSheet.getSheetByName('工作表1'); // 開啟工作表1
  var data = SheetName.getSheetValues(1,1,SheetName.getLastRow(),SheetName.getLastColumn());
  // 取得所有資料，組成 JSON 的形式，用純文字回傳
  Logger.log(data)  // 印出資料 ( 第一次執行時必須有這一行 )
  return ContentService.createTextOutput(JSON.stringify(data)).setMimeType(ContentService.MimeType.JSON);
}

