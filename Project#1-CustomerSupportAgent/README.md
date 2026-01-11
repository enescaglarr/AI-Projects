🚀 Installation & Setup
Follow these steps to set up the development environment on your local machine:

1. Clone the Repository
Open your terminal and run the following commands to clone the project:

Bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Create a Virtual Environment
It is recommended to use a virtual environment to isolate project dependencies:

Windows:

Bash

python -m venv venv
venv\Scripts\activate
macOS/Linux:

Bash

python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Install the required libraries, including LangChain, Streamlit, and FAISS, as specified in the project architecture:

Bash

pip install -r requirements.txt
4. Configure Environment Variables
The system requires a Google Gemini API Key to power the models/text-embedding-004 and gemini-1.5-flash models.

Create a file named .env in the root directory.

Add your API key to the file:

Plaintext

GEMINI_API_KEY=your_actual_api_key_here
Security Note: Ensure your .env file is listed in your .gitignore to prevent your API key from being uploaded to GitHub.

5. Prepare the Dataset
Ensure the Customer_Support_Training_Dataset.csv file is located in the root directory, as the backend logic (helper.py) relies on this specific filename to build the knowledge base.
