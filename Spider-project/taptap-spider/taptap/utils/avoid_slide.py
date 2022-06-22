import execjs
import re

def run_avoid(response_text:str =None):
    requestInfo = re.findall("requestInfo='(.*?)'", response_text)[0]
    # todo: 从源码找到绕过滑动滑块, 完成表单提交的方法
    '''function reform(data) {
        var form = document.createElement('form');
        var parsedUrl = parseURL(requestInfo.url);
        parsedUrl.search = addQuery(parsedUrl.search,data)
        var newUrl = combineUrl(parsedUrl);
        form.action = newUrl;
        form.method = "POST";
        form.innerHTML = parseFormQuery(requestInfo.data).join('');
        document.body.appendChild(form);
        form.submit();
        // document.body.appendChild(form);
    }'''