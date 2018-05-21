反编译apk代码方式：
1、将apk后缀名.apk 改成 .zip， 然后用解压缩工具解压，
2、将解压缩后得到的classes.dex 用d2j-dex2jar.bat脚本运行，得到jar包文件
3、用jd-gui.exe工具打开JAR包文件，查看源码。