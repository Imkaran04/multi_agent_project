# **Market Research and  AI/ML Use Case Generator**

## **Project Description**

The **Market Research and  AI/ML Use Case Generator** is an interactive web application that enables users to explore tailored AI/ML use cases and relevant industry insights for a given industry and focus area (Optional). This project simplifies market research and accelerates the ideation of AI/ML applications in diverse industries such as healthcare, finance, retail, and more.

### **Features**
- **Industry Research Insights**: Real-time fetching of industry trends and reports.
- **AI/ML Use Case Generation**: Industry-specific AI/ML applications with feasibility analysis.
- **Report Download**: Auto-generated markdown reports summarizing all insights.
- **User-Friendly Interface**: Built using Streamlit for an intuitive experience.

### **Technology Stack**
- **Python**: Core logic and API integration.
- **Streamlit**: Frontend for seamless user interaction.
- **TAVILY API**: To fetch industry research data.
- **Markdown Generation**: Dynamic report creation in markdown format.

### **Challenges Faced**
- Ensuring accurate and concise data collection from external APIs.
- Designing a user-friendly and responsive interface with Streamlit.
- Managing API errors and handling edge cases like missing data or invalid inputs.

---

## **Table of Contents**
1. [Project Description](#project-description)
2. [How to Install and Run the Project](#how-to-install-and-run-the-project)
3. [How to Use the Project](#how-to-use-the-project)
4. [Credits](#credits)
5. [License](#license)

---

## **How to Install and Run the Project**

### **Prerequisites**
1. **Python 3.9+**: Ensure Python is installed on your system.
2. **Streamlit**: Install Streamlit for the frontend.
3. **Environment File (.env)**: Create a `.env` file with your TAVILY API key.

### **Steps**
1. **Clone the Repository**
   ```bash
   [[git clone https://github.com/Imkaran04/multi_agent_project.git]

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**
   - Create a `.env` file in the root directory.
   - Add your TAVILY API key:
     ```plaintext
     TAVILY_API_KEY=your_api_key_here
     ```

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

5. Open the application in your browser at [http://localhost:8501](http://localhost:8501).

---

## **How to Use the Project**

1. **Enter the Industry Name**:
   - Input the industry you wish to explore (e.g., Healthcare, Retail).
   
2. **Specify a Focus Area (Optional)**:
   - Enter a focus area such as Supply Chain or Customer Experience to refine results.

3. **Generate Insights**:
   - Click the "Generate Insights" button to fetch:
     - Industry research insights.
     - AI/ML use cases with feasibility scores.

4. **View and Download Report**:
   - The insights and use cases are displayed in the application.
   - Click the "Download Report" button to save the generated report.

---

## **Credits**

### **Team Members**
- [Karan Singh](https://github.com/Imkaran04) – Developer


### **Acknowledgments**
- **TAVILY API**: For providing industry research data.
- **Streamlit**: For the intuitive frontend framework.

### **References**
- [Streamlit Documentation](https://docs.streamlit.io/)
- [TAVILY API Documentation](https://tavily.io/)

---

## **License**

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## **Architecture Flowchart**

```plaintext
User Input (Industry, Focus Area)
         |
         v
+---------------------------+
| Streamlit Frontend        |
+---------------------------+
         |
         v
+---------------------------+
| IndustryResearchAgent     |<---> External API (TAVILY)
+---------------------------+
         |
         v
+---------------------------+
| UseCaseGenerationAgent    |
+---------------------------+
         |
         v
+---------------------------+
| Markdown Report Generator |
+---------------------------+
         |
         v
+---------------------------+
| Display & Download Report |
+---------------------------+
```

---

#### **Badges**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-1.14%2B-orange)](https://streamlit.io/)  
[![License](https://img.shields.io/badge/License-MIT-green)](https://choosealicense.com/licenses/mit/)

---

## **How to Contribute to the Project**

Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a feature"
   ```
4. Push the changes to your branch:
   ```bash
   git push origin feature-name
   ```
5. Create a Pull Request.

---

## **Tests**

### **Running Tests**
To ensure the application functions as expected:
1. Run unit tests:
   ```bash
   pytest
   ```
2. Verify that all tests pass successfully.

---

## Thank you!
