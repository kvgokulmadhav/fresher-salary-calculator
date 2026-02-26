import streamlit as st
import pandas as pd

# --------------------------
# 1. Page Config & CSS Styling
# --------------------------
st.set_page_config(
    page_title="Fresher ROI & Target Salary Calculator",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for a beautiful, premium look
st.markdown("""
<style>
    /* Highlight the target salary with a cool gradient background */
    .target-box {
        background: linear-gradient(135deg, #1f4037 0%, #4cb8c4 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 20px 0px;
    }
    .target-box h1 {
        font-size: clamp(2rem, 5vw, 3.5rem); /* Responsive font size for mobile */
        margin: 0;
        color: white;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
    }
    .target-box h3 {
        font-size: clamp(1.2rem, 3vw, 2rem); /* Responsive sub-heading */
        margin: 10px 0 0 0;
        color: #e0f2f1;
        font-weight: 500;
    }
    .target-box p {
        font-size: 1.2rem;
        margin-bottom: 5px;
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------
# Helper Function for Commas
# --------------------------
def fmt(num):
    return f"{num:,.2f}"

# --------------------------
# Header Section & Currency Selector
# --------------------------
st.markdown("<h1 style='text-align: center;'> Fresher Minimum Salary Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #555;'>Find out exactly what <strong>Minimum Starting Salary (CTC)</strong> you need to ask for to comfortably pay off your education costs AND afford your monthly living expenses.</p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

_, col_curr, _ = st.columns([1, 2, 1])
with col_curr:
    currency_dict = {
        "INR": "₹",
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "CAD": "C$"
    }
    # Using a horizontal radio button looks much cleaner globally than a bulky selectbox in the corner
    selected_currency = st.radio(
        "🌍 **Choose your Currency:**", 
        list(currency_dict.keys()), 
        index=0, 
        horizontal=True
    )
    cy = currency_dict[selected_currency]

st.markdown("<hr style='margin-top: 10px; margin-bottom: 20px;'>", unsafe_allow_html=True)

# --------------------------
# Data Definitions
# --------------------------
ug_courses = {
    "3-Year Degree (B.Sc, B.A, B.Com, BBA, BCA)": 3.0, 
    "4-Year Degree (B.Tech, B.E)": 4.0, 
    "5-Year Degree (B.Arch)": 5.0, 
    "5.5-Year Degree (MBBS)": 5.5,
    "Other (Custom)": 0.0
}
pg_courses = {"2-Year Master's (M.Tech, MBA, M.Sc, M.A)": 2.0, "1-Year Master's / PG Diploma": 1.0, "Other (Custom)": 0.0}
cert_courses = {"6-Month BootCamp": 0.5, "1-Year Certification": 1.0, "Other (Custom)": 0.0}

def get_duration(course_dict, label):
    course = st.selectbox(f"Select your {label} Course:", list(course_dict.keys()))
    if course == "Other (Custom)":
        return st.number_input(f"Enter exact years for {label}:", min_value=0.5, value=2.0, step=0.5)
    return course_dict[course]

# --------------------------
# Dashboard Inputs (3 Columns)
# --------------------------
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("### 🎓 Step 1: The Journey")
    st.markdown("Tell us what you studied! 📚")
    
    edu_level = st.selectbox(
        "Your highest education level?", 
        ["Undergraduate (UG) Only", "Postgraduate (PG) Only", "Both (UG + PG)", "Diploma / Certification"]
    )

    standard_duration = 0.0
    if edu_level == "Undergraduate (UG) Only":
        standard_duration = get_duration(ug_courses, "UG")
    elif edu_level == "Postgraduate (PG) Only":
        standard_duration = get_duration(pg_courses, "PG")
    elif edu_level == "Both (UG + PG)":
        st.markdown("**Wow, double degree! Awesome. 🌟**")
        dur_ug = get_duration(ug_courses, "UG")
        dur_pg = get_duration(pg_courses, "PG")
        standard_duration = dur_ug + dur_pg
    elif edu_level == "Diploma / Certification":
        standard_duration = get_duration(cert_courses, "Certification")

    st.markdown("---")
    break_even_target = st.number_input(
        "⏳ Target Years to Break-Even/Repay:", 
        min_value=0.5, 
        value=float(max(1.0, standard_duration)), 
        step=0.5,
        help="How fast do you want to recover your costs? (Usually matches course duration)"
    )

with col2:
    st.markdown("### 💰 Step 2: The Investment")
    st.markdown("How much did it cost? Be honest! 🎓")
    
    # Use a text input to force comma formatting, parsing back to float behind the scenes
    raw_cost_str = st.text_input(
        f"Total Education Cost ({cy})", 
        value=f"{1000000.0 if selected_currency == 'INR' else 50000.0:,.2f}"
    )
    # Clean the input string by removing commas and any extra spaces
    try:
        total_cost = float(raw_cost_str.replace(",", "").replace(" ", ""))
    except ValueError:
        st.error("Please enter a valid number.")
        total_cost = 0.0

    st.markdown("---")
    st.markdown("**Did you take an Education Loan? 🏦**")
    took_loan = st.checkbox("Yes, I have an EMI to pay! 🙋‍♂️")

    loan_amount = 0.0
    interest_rate = 0.0

    if took_loan:
        st.warning("Let's calculate those EMIs! 📊")
        raw_loan_str = st.text_input(
            f"Loan Amount ({cy})", 
            value=f"{total_cost * 0.8:,.2f}"
        )
        try:
            loan_amount = float(raw_loan_str.replace(",", "").replace(" ", ""))
        except ValueError:
            st.error("Please enter a valid loan amount.")
            loan_amount = 0.0
        interest_rate = st.slider("Annual Interest Rate (%)", 1.0, 30.0, 9.5, step=0.5)

with col3:
    st.markdown("### 🍕 Step 3: The Lifestyle")
    st.markdown("What does it take to survive in your city? 🏙️")
    
    raw_exp_str = st.text_input(
        f"Monthly Living Expenses ({cy})", 
        value=f"{30000.0 if selected_currency == 'INR' else 2000.0:,.2f}"
    )
    try:
        monthly_expenses = float(raw_exp_str.replace(",", "").replace(" ", ""))
    except ValueError:
        st.error("Please enter a valid monthly expense.")
        monthly_expenses = 0.0
    
    st.markdown("---")
    st.markdown("**Don't forget the Government! 🏛️**")
    tax_rate = st.slider("Estimated Tax Rate (%)", 0, 80, 15)


# --------------------------
# 5. Backend Math Engine
# --------------------------
if took_loan and loan_amount > 0 and break_even_target > 0:
    P = loan_amount
    r = (interest_rate / 100) / 12  
    n = break_even_target * 12      
    
    if r > 0:
        monthly_emi = P * r * ((1 + r)**n) / (((1 + r)**n) - 1)
    else:
        monthly_emi = P / n
        
    yearly_loan_payoff = monthly_emi * 12
    self_funded = total_cost - loan_amount
    yearly_self_funded_recovery = self_funded / break_even_target
    
    yearly_recovery = yearly_loan_payoff + yearly_self_funded_recovery
else:
    yearly_recovery = total_cost / break_even_target if break_even_target > 0 else 0


yearly_living = monthly_expenses * 12
net_salary = yearly_recovery + yearly_living
gross_salary = net_salary / (1 - (tax_rate / 100))
yearly_tax = gross_salary - net_salary

# --------------------------
# 6. The Grand Reveal!
# --------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>🚀 Your Magic Number! 🚀</h2>", unsafe_allow_html=True)

# Shiny Target Box
st.markdown(f"""
<div class="target-box">
    <p>Target Gross Yearly Salary (CTC)</p>
    <h1>{cy} {fmt(gross_salary)}</h1>
    <h3>Monthly In-Hand (Net): {cy} {fmt(net_salary/12)}</h3>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Metrics Breakdown
st.markdown("### 🧩 The Yearly Breakdown")
st.markdown("Here is exactly where every dollar (or rupee!) is going over the next **{}** years:".format(break_even_target))

m1, m2, m3 = st.columns(3)
with m1:
    label = "Education ROI & EMI Payoff 🎓" if took_loan else "Education ROI Payoff 🎓"
    st.metric(label, f"{cy} {fmt(yearly_recovery)}")
with m2:
    st.metric("Survival & Fun (Living) 🍕", f"{cy} {fmt(yearly_living)}")
with m3:
    st.metric(f"Taxes to Govt ({tax_rate}%) 🏛️", f"{cy} {fmt(yearly_tax)}")

# Interactive Chart
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 📊 Visualizing your Salary Split")

chart_data = pd.DataFrame({
    "Category": ["Survival (Living)", "Education Payoff", "Taxes"],
    "Amount": [yearly_living, yearly_recovery, yearly_tax]
})

st.bar_chart(chart_data, x="Category", y="Amount", use_container_width=True, color="#1f4037")

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 1.1rem;'>🔥 You've got this! Start planning your career moves today! 💪</p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.info("""
**⚠️ Disclaimer:**
* **Market Realities:** This calculator shows the salary you mathematically *need*, not necessarily what the job market is currently offering. If your required CTC is unrealistically high, try increasing your Break-Even Target years.
* **Taxes & Interest:** This tool uses a simplified flat tax rate and does not account for compound interest on student loans or progressive tax brackets. 
* **Not Financial Advice:** This is an estimation tool for career planning. Always do your own thorough research before making financial or educational commitments.
""")
