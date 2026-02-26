# 🎓 Fresher ROI & Minimum Salary Calculator (Rebuilt)

A complete, interactive Streamlit web application designed perfectly to the requirements. It calculates your Target Gross Yearly Salary (CTC) based on education details, living expenses, and tax rates.

## 🌟 Features Included

1. **Global Settings**: Choose any currency (INR, USD, EUR, GBP, CAD) and see dynamic symbol updates across the entire app.
2. **Education Details Logic**: 
    - Intelligent dropdowns for UG, PG, Both (UG + PG), or Certifications.
    - If "Both (UG + PG)" is selected, **two** separate course dropdowns appear and their standard durations are added together automatically!
    - Dynamic Break-Even Target defaulting to the standard duration.
3. **Financial Reality**: Add monthly living expenses and a custom Tax Rate (%).
4. **Backend Math**: Accurate calculations splitting your salary into Education Payoff, Living Survival, and Taxes.
5. **Main Display**: A prominent CTC output, a clear breakdown, and an interactive pandas Bar Chart.

---

## 🚀 How to Run (Foolproof Guide)

### **Option 1: The Easy Way (Windows)**
1. Double-click the `run_app.bat` file in your project folder.
2. If you don't have Python installed, the script will automatically tell you and open the Microsoft Store so you can easily click "Get" to install it.
3. Once Python is installed, run `run_app.bat` again. It will handle all installations (`streamlit`, `pandas`) and launch the app in your browser!

### **Option 2: Terminal Execution**
If you prefer doing it manually:
1. Ensure Python is installed (`python --version` should work).
2. Open your terminal in this folder (`e:/My Apps`).
3. Run `python -m pip install -r requirements.txt`.
4. Run `python -m streamlit run app.py`.

Enjoy finding your minimum salary target!
