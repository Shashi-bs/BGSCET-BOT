from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    bot_response = generate_response(user_message)
    return jsonify({"user_message": user_message, "bot_response": bot_response})

def generate_response(message):
    # Convert the user message to lowercase for case-insensitive matching
    message_lower = message.lower().strip()

    if "hi" in message_lower:
        response = (
         "HELLO WELCOME TO BGSCET BOT\n"   
        "What would you like to know about BGSCET?\n"  # Add a newline after the question
        "1. About Adichunchanagiri Mutt\n"
        "2. Academics\n"
        "3. Contact Us\n"
        "4. Location & Transportation\n"
        "5. Departments\n"
        "6. Staff Information\n"
        "7. Exit\n"
    )

    # elif "1" in message_lower:
    #     response = (
    #         "Select an option:\n"
    #         "a. History\n"
    #         "b. Spiritual Significance\n"
    #         "c. Programs\n"
    #         "d. Notable Events"
    #     )
    elif "1" in message_lower:
        response = "Sri Adichunchanagiri Mahasamsthana Mutt has a history of 2000 years of its existence.\n It is the holy land engulfed with the divine resonance and vibration.\n Sri Mutt serves free food to more than twenty thousand people every day.\n Lord Shiva performed penance at Sri Kshetra, during which he devoured two demons."
    elif "2" in message_lower:
        response = (
            "Select an option:\n"
            "a. Branches\n"
            "b. Library\n"
            "c. Labs\n"
            "d. Campus Facilities"
        )
        if "2a" in message_lower:
            response = "BGSCET offers branches like CSE, ISE, AIML, AIDS, and CSD."
        elif "2b" in message_lower:
            response = "BGSCET has a well-equipped library with a vast collection of books."
        elif "2c" in message_lower:
            response = "BGSCET provides state-of-the-art laboratories for practical learning."
        elif "2d" in message_lower:
            response = "The campus includes hostels, sports facilities, and a cafeteria."
    elif "3" in message_lower:
        response = (
            "Select an option:\n"
            "a. General Enquiries\n"
            "b. Admissions\n"
            "c. Administration\n"
            "d. Support"
        )
        if "3a" in message_lower:
            response = "For general enquiries, contact us at 9731292555."
        elif "3b" in message_lower:
            response = "For admissions, contact us at 9964897207."
        elif "3c" in message_lower:
            response = "For administration, contact us at 9731292555."
        elif "3d" in message_lower:
            response = "For support, contact us at 9964897207."
    elif "4" in message_lower:
        response = (
            "Select an option:\n"
            "a. Campus Location\n"
            "b. Nearest Landmark\n"
            "c. Transportation\n"
            "d. Mailing Address"
        )
        if "4a" in message_lower:
            response = "CA Site No. 6 & 7, 3rd Main Pipeline Road, Chord Rd, Mahalakshmipuram, Bengaluru."
        elif "4b" in message_lower:
            response = "The campus is adjacent to Mahalakshmi Metro Station."
        elif "4c" in message_lower:
            response = "The campus is well-connected by public transportation."
        elif "4d" in message_lower:
            response = "BGSCET, 2nd Phase, Stage 2, Mahalakshmipuram, Bengaluru, Karnataka 560086."
    elif "5" in message_lower:
        response = (
            "Select an option:\n"
            "a. Computer Science & Engineering\n"
            "b. Information Science & Engineering\n"
            "c. Artificial Intelligence & Machine Learning\n"
            "d. Artificial Intelligence & Data Science"
        )
        if "5a" in message_lower:
            response = "CSE is a popular branch focusing on software development and computer systems."
        elif "5b" in message_lower:
            response = "ISE emphasizes information systems and data management."
        elif "5c" in message_lower:
            response = "AIML focuses on creating intelligent systems and machine learning applications."
        elif "5d" in message_lower:
            response = "AID combines AI techniques with data analysis and processing."
    elif "6" in message_lower:
        response = (
            "Select an option:\n"
            "a. Teaching Staff\n"
            "b. Research Staff\n"
            "c. Administrative Staff\n"
            "d. Support Staff"
        )
        if "6a" in message_lower:
            response = "Our teaching staff consists of experienced professionals with advanced degrees."
        elif "6b" in message_lower:
            response = "Our research staff is involved in cutting-edge research projects."
        elif "6c" in message_lower:
            response = "Our administrative staff ensures the smooth operation of the college."
        elif "6d" in message_lower:
            response = "Our support staff provides essential services to students and faculty."
    else:
        response = "I'm sorry, I didn't understand that. Can you please select an option from the list?"

    return response

if __name__ == "__main__":
    app.run(debug=True)
