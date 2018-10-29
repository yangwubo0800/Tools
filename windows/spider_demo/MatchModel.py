import re



IP_PATTERN='[0-9]{1,3}'+'\\.'+'[0-9]{1,3}'+'\\.'+'[0-9]{1,3}'+'\\.'+'[0-9]{1,3}'
COMMON_PICTURE_JPG=r'src="([.*\S]*\.jpg)"'
COMMON_PICTURE_PNG=r'src="([.*\S]*\.png)"'