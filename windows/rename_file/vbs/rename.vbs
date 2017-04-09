
'get file system obj
Set objFSO = CreateObject("Scripting.FileSystemObject")
'for each the file in this dir
set currentFoler = createobject("Scripting.FileSystemObject").GetFolder(".")
'define the varaible
dim  count, message, changedName, extensionName
count = 0
'use for each to find all the file
for each file in currentFoler.Files
'get the file  extension name
extensionName = objFSO.GetExtensionName(file)
'to get the file modify time
set fsFile=objFSO.GetFile(file)
'use the modify time: year_month_day_hour_minute_sencond and extension name as changed name
changedName=year(fsFile.DateLastModified)&"_"&month(fsFile.DateLastModified)&"_"&day(fsFile.DateLastModified)&"_"&_
hour(fsFile.DateLastModified)&"_"& minute(fsFile.DateLastModified)&"_"& second(fsFile.DateLastModified)&"."&extensionName
'rename the file to modify time if the file is not vbs file and not exist before
if StrComp(lcase(extensionName), "vbs") <> 0  and not objFSO.FileExists(changedName) then
count=count+1
fsFile.name=changedName
end if

next

MsgBox "主人，我们总共修改了 "&count&" 个文件的名称，赶快看看吧！^_^"

set fsFile= Nothing
set objFSO=Nothing
set currentFoler=Nothing
