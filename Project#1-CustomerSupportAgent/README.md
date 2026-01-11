## 🚀 Installation & Setup

Follow these steps to set up the development environment on your local machine:

### 1. Clone the Repository
Since this project is part of the `AI-Projects` suite, you must clone the main repository and navigate to this folder:

```bash
# Clone the main repository
git clone https://github.com/enescaglarr/AI-Projects.git

# Enter this project's directory
cd "AI-Projects/Project#1-CustomerSupportAgent"
```

2. Create a Virtual Environment
It is recommended to use a virtual environment to isolate project dependencies:

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install Dependencies
Install the required libraries, including LangChain, Streamlit, and FAISS, as specified in the project architecture:
```bash
pip install -r requirements.txt
```

4. Configure Environment Variables
The system requires a Google Gemini API Key to power the models/text-embedding-004 and gemini-1.5-flash models.

Create a file named .env in the root directory.

Add your API key to the file:
```bash
GEMINI_API_KEY=your_actual_api_key_here
```
