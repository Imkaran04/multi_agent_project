# utils/report_generator.py

def generate_markdown_report(industry, focus_area, research_results, use_cases):
    # Start with the title and industry info
    report = f"# Market Research & AI/ML Use Case Proposal Report\n\n"
    report += f"## Industry: {industry}\n"
    if focus_area:
        report += f"### Focus Area: {focus_area}\n\n"
    
    # Add market research summary section
    report += "### **Market Research Summary**\n"
    for result in research_results:
        report += f"1. **{result['title']}**\n"
        report += f"   - [Learn More]({result['url']})\n\n"
    
    report += "---\n\n### **Generated Use Cases**\n"
    for use_case in use_cases:
        report += f"1. **{use_case['title']}**\n"
        report += f"   - Description: {use_case['description']}\n"
        report += f"   - Feasibility: {use_case['feasibility']}\n\n"
    
    # Add the relevant datasets section at the end
    report += "---\n\n### **Relevant Datasets**\n"
    report += "You can find relevant datasets for the AI/ML use cases on the following platforms:\n\n"
    report += "- [Google Dataset Search](https://datasetsearch.research.google.com/)\n"
    report += "- [Kaggle Datasets](https://www.kaggle.com/datasets)\n"
    report += "- [Datahub.io](https://datahub.io/)\n"
    report += "- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)\n"
    report += "- [Earth Data](https://earthdata.nasa.gov/)\n"
    report += "- [CERN Open Data Portal](http://opendata.cern.ch/)\n"

    return report
