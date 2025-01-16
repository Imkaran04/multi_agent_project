import streamlit as st
import os
from dotenv import load_dotenv
from agents.industry_research_agent import IndustryResearchAgent
from agents.use_case_generation_agent import UseCaseGenerationAgent
from utils.report_generator import generate_markdown_report  # Import the updated report generator function

# Load environment variables from .env file
load_dotenv()

# Fetch the API key from environment variable
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Streamlit UI setup
st.title("Dynamic AI/ML Use Case Generator")

# Add unique keys for each text_input element to prevent duplicate IDs
industry = st.text_input("Enter Industry Name:", placeholder="e.g., Retail, Healthcare, Finance", key="industry_input_key")
focus_area = st.text_input("Enter Focus Area (Optional):", placeholder="e.g., Supply Chain, Customer Experience", key="focus_area_input_key")

if st.button("Generate Insights"):
    if industry:
        # Display Industry Research
        st.subheader("Industry Research")
        
        # Instantiate the IndustryResearchAgent and fetch industry data
        research_agent = IndustryResearchAgent(api_key=TAVILY_API_KEY)
        industry_info = research_agent.fetch_industry_info(industry, focus_area)
        
        if isinstance(industry_info, str):  # Error case
            st.write(industry_info)
        else:
            for entry in industry_info:
                st.markdown(f"**{entry['title']}**")
                st.markdown(f"[Learn More]({entry['url']})")
                st.write("")  # Add space between entries

            # Display Use Cases
            st.subheader("Generated Use Cases")
            
            # Instantiate UseCaseGenerationAgent and fetch use cases
            use_case_agent = UseCaseGenerationAgent(api_key=TAVILY_API_KEY)
            use_cases = use_case_agent.generate_use_cases(industry)

            # Display use cases in Streamlit UI
            for use_case in use_cases:
                st.markdown(f"### {use_case['title']}")
                st.write(use_case['description'])
                st.write(f"Feasibility: {use_case['feasibility']}")

            # Generate the report content
            report_content = generate_markdown_report(industry, focus_area, industry_info, use_cases)

            # Display the full report content as markdown (in Streamlit UI)
            st.markdown("### **Generated Report**")
            st.markdown(report_content)

            # Streamlit download button for markdown file
            st.download_button(
                label="Download Report", 
                data=report_content, 
                file_name="generated_report.md", 
                mime="text/markdown",
                use_container_width=True  # Make button take full width
            )

    else:
        st.error("Please enter an industry name.")
