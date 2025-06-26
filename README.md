# PRODIGY_CS_04
# 🛡 Simple Python Keylogger (Console-Based Input)

This project is a *simple keylogger* built using *pure Python* with no external libraries. It captures user input typed in the console and writes it to a file named keyloger.txt.

📝 *Note*: This is an interactive, console-based keylogger using input(). It does not run in the background or capture keystrokes system-wide.

---

## 📌 Features

- Console-based input capture
- Saves each input line to keyloger.txt
- Stops when user types STOP
- No external libraries required

---

## 🛠 How It Works

1. The program prompts the user to type input continuously.
2. Each input is logged to keyloger.txt (one per line).
3. Typing STOP (case-insensitive) ends the logging session.

---

## 📂 File Structure


keylogger.py      # Python script
keyloger.txt      # Log file (created/updated automatically)
README.md         # This file


---

## ▶ How to Run

1. Save the script as keylogger.py
2. Run it using IDLE, terminal, or command prompt:

bash
python keylogger.py


3. Type your messages when prompted.
4. Type STOP and press Enter to stop logging.

---

## 📄 Sample Output in keyloger.txt

If the following inputs are typed:


hi!
hello world
123?
STOP


Then the contents of keyloger.txt will be:


hi!
hello world
123?


---

## 🚫 Disclaimer

This project is for *educational purposes only*. Do not use this script in any unethical or unauthorized context.

---

## 📚 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Author

Created by a curious learner exploring the basics of file handling and user input in Python. 🐍
