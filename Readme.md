
Smart Autocorrect Tool 🧠

This is a Python-based AI-powered desktop application that automatically detects and corrects spelling and grammatical errors in user-input text. The project was built as part of my internship with Pinnacle Labs, under the Ministry of Corporate Affairs, Government of India. It blends Natural Language Processing (NLP) with a clean, interactive interface to offer a smart and intuitive writing experience.

The tool works in a simple five-step process. First, users type or paste their sentence into the GUI text box. The application then applies spelling correction using the TextBlob library, which suggests accurate replacements based on common English usage patterns. Next, grammar checking is done using the language_tool_python library, which identifies grammar mistakes and corrects them using rules from LanguageTool.

Additionally, I implemented post-processing logic to fix common contextual or subject-verb errors that automated tools often miss. For example, terms like "leaders" can be incorrectly used where "learners" is intended. These refinements ensure better accuracy in real-world scenarios.

The graphical user interface was built using Tkinter, which provides a scrollable input and result area, an "Analyze" button to trigger corrections, and a "Copy to Clipboard" button using the pyperclip library for convenience. The tool is responsive and simple enough for anyone to use without prior technical knowledge.

To run the tool, users simply install the required libraries (textblob, language-tool-python, and pyperclip) and execute the Python file. It opens a user-friendly window where they can instantly correct their writing. This project helped me explore how AI and NLP can solve practical problems and reinforced my understanding of string processing, GUI development, and user-focused design.

The complete source code is available in this repository. Feel free to explore, use, and contribute to it.

Here's a demo video link for your reference: https://drive.google.com/file/d/1FEEEgFG6hk3fYriGssWVC1tIXiOCrY81/view?usp=drivesdk
