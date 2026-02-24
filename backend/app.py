# Write with OpenCode
import os
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
DEEPSEEK_API_URL = os.getenv('DEEPSEEK_API_URL', 'https://api.deepseek.com')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/evaluate', methods=['POST'])
def evaluate():
    data = request.get_json()
    latex_input = data.get('expression', '').strip()

    if not latex_input:
        return jsonify({'error': '请输入要计算的公式'}), 400

    try:
        response = requests.post(
            f'{DEEPSEEK_API_URL}/chat/completions',
            headers={
                'Authorization': f'Bearer {DEEPSEEK_API_KEY}',
                'Content-Type': 'application/json'
            },
            json={
                'model': 'deepseek-chat',
                'messages': [
                    {
                        'role': 'system',
                        'content': '你是一个数学助手。请根据用户给出的公式进行计算或求解，直接给出最终答案。如果需要解题步骤，可以简要说明。只输出计算结果，不需要输出代码。'
                    },
                    {
                        'role': 'user',
                        'content': f'请计算或求解以下公式：{latex_input}'
                    }
                ],
                'temperature': 0.7,
                'max_tokens': 1000
            },
            timeout=30
        )

        if not response.ok:
            error_data = response.json()
            return jsonify({'error': error_data.get('error', {}).get('message', 'API 请求失败')}), response.status_code

        result = response.json()
        content = result.get('choices', [{}])[0].get('message', {}).get('content', '未获取到结果')

        return jsonify({'result': content})

    except requests.exceptions.Timeout:
        return jsonify({'error': '请求超时，请稍后重试'}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'网络错误: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'服务器错误: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
