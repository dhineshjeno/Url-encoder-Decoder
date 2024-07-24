from flask import Flask, request, render_template_string
import urllib.parse

app = Flask(__name__)

TEMPLATE = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>URL Encoder/Decoder</title>
    <style>
      body { 
        font-family: Arial, sans-serif;
        background-color: #f7f7ab;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh; 
      }
      .container {
        background-color: #f7f7ab;
        padding: 50px;
        
        text-align: center;
        width: 300px;
      }
      h1 {
        font-size: 24px;
        margin-bottom: 20px;
      }
      input[type="text"] { 
        width: 80%; 
        padding: 10px; 
        margin: 10px 0; 
      }
      button { 
        padding: 10px 20px; 
        margin: 5px; 
        color: #007bff;
      }
      .result { 
        margin-top: 20px; 
        font-size: 1.2em; 
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>URL Encoder/Decoder</h1>
      <form method="post" action="/">
        <input type="text" name="url" placeholder="Enter URL" required>
        <button type="submit" name="action" value="encode">Encode</button>
        <button type="submit" name="action" value="decode">Decode</button>
      </form>
      {% if result %}
      <div class="result">
        <strong>Result:</strong> {{ result }}
      </div>
      {% endif %}
    </div>
  </body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        url = request.form['url']
        action = request.form['action']
        if action == 'encode':
            result = urllib.parse.quote(url)
        elif action == 'decode':
            result = urllib.parse.unquote(url)
    return render_template_string(TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
