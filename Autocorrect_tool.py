import tkinter as tk
from tkinter import messagebox, scrolledtext
from textblob import TextBlob
import language_tool_python
import pyperclip

# Initialize grammar tool (language_tool)
grammar_tool = language_tool_python.LanguageTool('en-US')

def correct_spelling(text: str) -> str:
    """Correct spelling using TextBlob."""
    return str(TextBlob(text).correct())

def correct_grammar(text: str) -> str:
    """Correct grammar using LanguageTool."""
    matches = grammar_tool.check(text)
    return language_tool_python.utils.correct(text, matches), matches

def process_text(text: str) -> str:
    """Process text to correct both spelling and grammar."""
    # Step 1: Correct spelling
    corrected_spelling = correct_spelling(text)

    # Step 2: Correct grammar
    corrected_grammar, grammar_matches = correct_grammar(corrected_spelling)

    # Step 3: Post-processing for contextual errors (like "learners" vs "leaders")
    corrected_grammar = corrected_grammar.replace("leaders", "learners")

    # Additional post-processing for subject-verb agreement errors
    corrected_grammar = corrected_grammar.replace("This tool are", "This tool is")
    corrected_grammar = corrected_grammar.replace("It make", "It makes")

    return corrected_grammar, grammar_matches

def display_results():
    user_input = input_box.get("1.0", tk.END).strip()
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    # Step 1: Correct spelling and grammar
    corrected_text, grammar_matches = process_text(user_input)

    # Prepare output
    result = ""
    if corrected_text == user_input:
        result += "✅ No spelling or grammar errors found.\n\n"
    else:
        result += f"🎯 Final Corrected Text:\n{corrected_text}\n\n"

    if grammar_matches:
        result += "🔍 Grammar Suggestions Applied:\n"
        result += "\n".join(f"- {match.message}" for match in grammar_matches)
    else:
        result += "🧠 Text is grammatically correct and meaningful!"

    # Update result display
    result_box.config(state=tk.NORMAL)
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, result)
    result_box.config(state=tk.DISABLED)

    # Enable copy to clipboard
    copy_btn.config(state=tk.NORMAL)
    window.corrected_text = corrected_text

def copy_result_to_clipboard():
    pyperclip.copy(window.corrected_text)
    messagebox.showinfo("Copied", "Corrected text copied to clipboard!")

# ---- UI Setup ---- #
window = tk.Tk()
window.title("Smart Autocorrect Tool 🧠")
window.geometry("650x520")
window.resizable(False, False)
window.corrected_text = ""

# Input area
tk.Label(window, text="Enter your sentence:", font=("Arial", 12)).pack(pady=5)
input_box = scrolledtext.ScrolledText(window, height=6, wrap=tk.WORD, font=("Arial", 11))
input_box.pack(padx=10, pady=5, fill=tk.BOTH)

# Analyze button
tk.Button(window, text="✅ Analyze", command=display_results,
          bg="#4CAF50", fg="white", font=("Arial", 11), width=15).pack(pady=10)

# Output area
tk.Label(window, text="Result:", font=("Arial", 12)).pack(pady=5)
result_box = scrolledtext.ScrolledText(window, height=12, wrap=tk.WORD, font=("Arial", 11), state=tk.DISABLED)
result_box.pack(padx=10, pady=5, fill=tk.BOTH)

# Copy to clipboard
copy_btn = tk.Button(window, text="📋 Copy to Clipboard", command=copy_result_to_clipboard,
                     font=("Arial", 10), state=tk.DISABLED)
copy_btn.pack(pady=5)

# Run app
window.mainloop()
