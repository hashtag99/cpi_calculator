from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Grade mapping
GRADE_DICT = {
    'A+': 10, 'A': 10, 'B+': 9, 'B': 8,
    'C+': 7, 'C': 6, 'D+': 5, 'D': 4,
    'E': 0, 'F': 0
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_cpi():
    data = request.json
    credits = data.get('credits')
    grades = data.get('grades')

    try:
        total_weighted_score = sum(
            int(credits[i]) * GRADE_DICT[grades[i]] for i in range(len(credits))
        )
        total_credits = sum(map(int, credits))
        cpi = total_weighted_score / total_credits
        return jsonify({'cpi': round(cpi, 2)})
    except Exception as e:
        return jsonify({'error': 'Invalid input! Please check your data.'})

if __name__ == '__main__':
    app.run(debug=True)
