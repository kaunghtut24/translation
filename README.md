```markdown
# Basic Translation App

This is a simple translation app built using Streamlit and the Backenster translation API. It allows users to translate text between various languages.

## Features

- Translates text between multiple languages.
- User-friendly interface with language selection dropdowns.
- Copy button to easily copy the translated text.

## Requirements

- Python 3.7 or higher
- Streamlit
- Requests
- python-dotenv

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kaunghtut24/translation.git
   ```

2. Install the required packages:

   ```bash
   pip install streamlit requests python-dotenv
   ```

3. Create a `.env` file in the project directory and add your Backenster API key:

   ```
   API_KEY=your_actual_api_key_here
   ```

## Usage

1. Run the app:

   ```bash
   streamlit run copy.py
   ```

2. Enter the text you want to translate in the text area.

3. Select the source and target languages from the dropdowns.

4. Click the "Translate" button.

5. The translated text will be displayed below.

6. Click the "Copy Translation" button to copy the translated text to the clipboard.

## Supported Languages

The app currently supports the following languages:

- English (US)
- English (Great Britain)
- Myanmar (Burmese)
- Russian
- Hindi
- Bengali
- Japanese
- Korean
- Thai
- Chinese (Simplified)
- French
- Spanish
- German
- Portuguese (Brazil)
- Portuguese
- Arabic
- and many more

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## Acknowledgments

- Backenster translation API
- Streamlit
```


