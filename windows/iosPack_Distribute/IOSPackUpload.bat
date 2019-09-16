echo "start ssh login and start xcodebuild...."

putty.exe -ssh -pw 123456 -m  ./build.sh userName@host


echo "start to copy ipa from MAC..."
pscp.exe -r -pw 123456 userName@host:/Users/user/Svn/projectxxx/IOS/BaseWebviewApp/build/BaseWebviewApp.ipa ./


echo "start use windows ftp upload file..." 
ftp -s:./ftp_command.txt 


echo "all the steps have done, please use iphone test device, use safari visit address https://test.11ka.wang/ipa_distribution.html to check the new ipa !"
pause