from flask import Flask, request, render_template
import joblib
import datetime

app = Flask(__name__)

model = joblib.load("LinearSVCTuned.pkl")
vectorizer = joblib.load("tfidfvector.pkl")

interpretations = {
    0: "Age Based Cyber Bullying",
    1: "Ethnicity Based Cyber Bullying",
    2: "Gender Based Cyber Bullying",
    3: "Not Cyberbullying",
    4: "Other Cyberbullying",
    5: "Religion Based Cyber Bullying"
}

def log_prediction(input_text, prediction):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Input: \"{input_text}\" | Prediction: {prediction}\n"
    
    log_file_path = "prediction_logs.txt" 
    
    try:
        with open(log_file_path, "a", encoding="utf-8") as f:
            f.write(log_entry)
        print(f"Logged entry: {log_entry.strip()}") 
    except IOError as e:
        print(f"Error writing to log file: {e}")


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    input_text_preserved = "" 

    if request.method == "POST":
        input_text = request.form["input_text"]

        input_text_preserved = input_text 

        transformed_input = vectorizer.transform([input_text])
        
        prediction_value = model.predict(transformed_input)[0]
        
        for i in interpretations.keys():
            if i == prediction_value:
                prediction = interpretations[i]
        
        log_prediction(input_text, prediction)

    return render_template("index.html", prediction=prediction, input_text_preserved=input_text_preserved)

if __name__ == "__main__":
    app.run(debug=True)