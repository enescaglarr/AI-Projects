Installation & Setup
Follow these steps to get the development environment running locally:

1. Clone the Repository
Bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Create a Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies:

Bash

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Bash

pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the root directory to store your API key securely:

Plaintext

GEMINI_API_KEY=your_actual_api_key_here
Note: Never commit your .env file to GitHub.

💻 Usage
To launch the application:

Ensure your Customer_Support_Training_Dataset.csv is in the root directory.

Run the Streamlit application:

Bash

streamlit run demo.py
Access the interface at http://localhost:8501 in your browser.

📁 Project Structure
demo.py: The frontend interactive interface.

helper.py: Backend logic for the RAG pipeline, including embedding and indexing.

/vector_store: Local storage for the FAISS index files (index.faiss and index.pkl).

Customer_Support_Training_Dataset.csv: The knowledge base used for retrieval.
