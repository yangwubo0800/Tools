#!/bin/sh
echo "This is a MAC, let start building..."

cd /Users/hongboni/Svn/hzinfo3000platform/hzinfo-app/IOS/BaseWebviewApp

security unlock-keychain -p 123456

echo "start to replace the first page url..."

first_page_url="http://www.baidu.com"

sed -i ""  "s~<first_page_url>.*<\/first_page_url>~<first_page_url>${first_page_url}<\/first_page_url>~" ./BaseWebviewApp/Resource/app_config.xml


xcodebuild  -project BaseWebviewApp.xcodeproj/  clean

echo "clean over, start to sleep..."
sleep 1

xcodebuild -scheme BaseWebviewApp -archivePath build/BaseWebviewApp.xcarchive archive

echo "archive over, start to sleep..."
sleep 1

xcodebuild -exportArchive -archivePath build/BaseWebviewApp.xcarchive -exportPath build/BaseWebviewApp.ipa -exportOptionsPlist ExportOptions.plist

echo "export over, start to sleep..."
sleep 1





