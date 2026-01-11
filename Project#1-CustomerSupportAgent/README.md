### Installation & Setup
Follow these steps to set up the development environment on your local machine:

1. Clone the Repository
Open your terminal and run the following commands to clone the project:
```bash
git clone https://github.com/enescaglarr/Project#1-CustomerSupportAgent.git
cd Project#1-CustomerSupportAgent
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
