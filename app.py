from flask import Flask, request, Response

app = Flask(__name__)

@app.before_request
def index():
    accept_header = request.headers.get('Accept', '')

    if 'image' in accept_header:

        fake_gif = b'GIF89a\x01\x00\x01\x00\x80\xff\x00\xff\xff\xff\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b'
        response = Response(fake_gif, content_type='image/gif')

    else:
        # Respond with JavaScript code if 'image' is not in the Accept header
        with open('script.js', 'r') as js_file:
            javascript_code = js_file.read()
        response = Response(javascript_code, content_type='application/javascript')
    
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response
    

if __name__ == '__main__':
    app.run(debug=False)
