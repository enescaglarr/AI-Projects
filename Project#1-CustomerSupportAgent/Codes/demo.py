import streamlit as st
import faiss
import pandas as pd
from src.helper import semantic_similarity, call_llm

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Gemini Free Support", layout="wide")
st.title("🚀 AI Assisted Customer Support")

# Sidebar for Configuration
st.sidebar.header("Settings")
gemini_api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

# --- UPDATED: Verified Free Tier Models ---
selected_model = st.sidebar.selectbox(
    "Select Gemini Model (Free Tier):",
    options=[
        "gemini-3-flash-preview",             
        "gemini-2.5-flash",         
        "gemini-2.5-flash-lite"
    ],
    index=0,
    help="Note: Pro 3 is paid only. Pro 2.5 and Flash 3 are available for Free Tier."
)

if not gemini_api_key:
    st.warning("Please enter your Gemini API key in the sidebar to proceed.")
    st.stop()

# --- CACHED DATA LOADING ---
@st.cache_resource
def load_assets():
    # Load the FAISS index and the knowledge base CSV
    index = faiss.read_index('vector_store/faiss_index.index')
    df = pd.read_csv('Customer_Support_Training_Dataset/Customer_Support_Training_Dataset.csv')
    return index, df

index, df = load_assets()

# --- MAIN INTERFACE ---
query = st.text_input("Customer Inquiry:", placeholder="e.g., My order hasn't arrived.")

# Trigger the initial search and generation
if st.button("Run AI Assistant", type="primary"):
    if not query:
        st.error("Please enter a query.")
    else:
        # 1. Search for similar cases
        with st.spinner("Finding similar cases..."):
            distances, indices = semantic_similarity(query, index, gemini_api_key)
            top_matches = df.iloc[indices[0]].reset_index(drop=True)
            # Store results in session state so they persist during reruns
            st.session_state['top_matches'] = top_matches
            st.session_state['last_query'] = query

        # 2. Initial Generation
        with st.spinner("Generating initial response..."):
            llm_response = call_llm(query, top_matches['response'].tolist(), gemini_api_key, model_name=selected_model)
            st.session_state['llm_response'] = llm_response

# --- DISPLAY SECTION ---
# This section runs every time the app reruns, 
# ensuring the content stays visible if it exists in session state.
if 'llm_response' in st.session_state:
    # Display Internal Knowledge
    st.subheader("Internal Database Knowledge")
    st.dataframe(st.session_state['top_matches'][['instruction', 'intent', 'response']], use_container_width=True)
    
    st.divider()
    
    # Display AI Response
    st.subheader(f"AI Analysis ({selected_model})")
    st.markdown(st.session_state['llm_response'])

    # --- REFINEMENT / REGENERATE SECTION ---
    st.divider()
    feedback = st.text_area("Refine this response:", placeholder="e.g., Make it shorter.")
    
    if st.button("Regenerate"):
        if feedback:
            # Create a refinement prompt using the previous answer and user feedback
            ref_prompt = f"Previous Response: {st.session_state['llm_response']}\n\nUser Feedback for refinement: {feedback}"
            
            with st.spinner("Updating response based on feedback..."):
                # Call LLM again with the new refined prompt
                new_resp = call_llm(
                    ref_prompt, 
                    st.session_state['top_matches']['response'].tolist(), 
                    gemini_api_key, 
                    model_name=selected_model
                )
                # Update the session state and trigger a rerun to refresh the UI
                st.session_state['llm_response'] = new_resp
                st.rerun()
        else:
            st.warning("Please provide feedback or instructions to regenerate.")