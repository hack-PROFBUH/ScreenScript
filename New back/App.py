from flask import Flask, request, jsonify
## from some_module import generate_transcript, generate_screenshots, generate_sections  # здесь замените на реальные модули и функции

app = Flask(__name__)

@app.route('/api/generate-article', methods=['POST'])
def generate_article():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    # Этап 1: Получение транскрипции аудио из видео
    transcript = generate_transcript(url)
    
    # Этап 2: Генерация скриншотов из видео
    screenshots = generate_screenshots(url)
    
    # Этап 3: Разделение транскрипции на разделы по скриншотам
    sections = generate_sections(transcript, screenshots)

    # Возвращаем результаты
    return jsonify({
        'transcript': transcript,
        'screenshots': screenshots,
        'sections': sections
    })

if __name__ == '__main__':
    app.run(debug=True)
