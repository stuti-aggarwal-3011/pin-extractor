# Pin Extractor

A clever, lightweight Python script that utilizes basic steganography principles to extract a secret numeric PIN from a given list of poems or text blocks. 

## 🚀 How It Works

The script systematically evaluates each text block (poem) line by line, mapping the line's position to a specific word index to build the final passkey:

* **Line-to-Word Mapping:** It targets the $N$-th word on the $N$-th line of a poem (using standard 0-based indexing).
* **Length Keying:** The character length of that specific target word is calculated and appended to the PIN.
* **Fallback Check:** If a line is empty or does not contain enough words to match the current line index, the script automatically appends a fallback value of `0`.

## 🛠️ Variables Evaluated

| Variable | Type | Description |
| :--- | :--- | :--- |
| `poems` | `list[str]` | A list containing the raw text strings/poems to be processed. |
| `secret_codes` | `list[str]` | The final output list containing the extracted numeric PIN strings. |
| `lines` | `list[str]` | An intermediate array representing individual lines extracted from a poem. |
| `words` | `list[str]` | An intermediate array representing individual words extracted from a single line. |

## 💻 Tech Stack
* **Language:** Python 3.x
* **Concepts:** String manipulation, index tracking, looping structures, data parsing.
