# -*- coding: UTF-8 -*-
import StringIO
from flask import *
from app.main import main
from basicfunc import ImageChar, create_validate_code, messagecode


@main.route('/VerifyCode/')
def get_code():
    #把strs发给前端,或者在后台使用session保存
    ic = ImageChar(fontColor=(100,211, 90))
    strs,code_img = ic.randChinese(4)
    buf = StringIO.StringIO()
    code_img.save(buf,'JPEG',quality=70)
    buf_str = buf.getvalue()
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/jpeg'
    session['a'] = strs
    return response


@main.route('/testsession', methods=['GET'])
def testsession():
    img_str = request.args.get('code', '')
    if session['img_str'].lower() == img_str:
        return jsonify({'result': 'ok'})
    else:
        return jsonify({'result': 'error'})


@main.route('/VerifyCode2/')
def get_code2():
    code_img = create_validate_code()
    session['img_str'] = code_img[1]
    buf = StringIO.StringIO()
    code_img[0].save(buf, 'JPEG', quality=70)
    buf_str = buf.getvalue()
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    return response


@main.route('/msgcode/', methods=['POST'])
def get_msgcode():
    if request.method == u'POST':
        data = request.get_json(force=True)
        number = data.get('phone-number', '')  # 字符串
        code = messagecode(number)
        if code == 1:
            return jsonify({'result': 'error'})
        else:
            session['msgcode'] = code
            return jsonify({'result': 'code already send'})
    else:
        return jsonify({'result': 'error'})