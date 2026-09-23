import streamlit as st

st.set_page_config(page_title="Smart AI Traveller APP", page_icon="✈️")

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #0f172a 0%, #1d4ed8 45%, #0ea5e9 100%);
        }
        .main {
            padding-top: 2rem;
        }
        .title-box {
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 16px;
            padding: 1.2rem 1.4rem;
            margin-bottom: 1rem;
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        }
        .summary-card {
            background: rgba(15, 118, 110, 0.18);
            border-left: 6px solid #22c55e;
            border-radius: 12px;
            padding: 1rem 1.2rem;
            margin: 0.8rem 0;
        }
        .budget-pill {
            display: inline-block;
            font-weight: 700;
            padding: 0.4rem 0.8rem;
            border-radius: 999px;
            background: #fbbf24;
            color: #111827;
            margin-top: 0.6rem;
        }
        .hotel-pill {
            display: inline-block;
            font-weight: 700;
            padding: 0.4rem 0.8rem;
            border-radius: 999px;
            background: #38bdf8;
            color: #082f49;
            margin-top: 0.6rem;
        }
        .travel-tip {
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.18);
            border-radius: 12px;
            padding: 0.8rem 1rem;
            margin-top: 0.8rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title-box"><h1 style="color:#f8fafc; margin:0;">✈️ Smart AI Traveller APP</h1></div>', unsafe_allow_html=True)

destination = st.text_input("Enter destination")
travel_date = st.date_input("Enter the travel Date")
budget = st.number_input("Enter budget")
hotel_required = st.selectbox("Do you need hotel stay", ("Yes", "No"))

travel_type = st.selectbox(
    "Travel Type",
    ["Solo", "Family", "Couple", "Business"],
)

interest = st.multiselect(
    "Interest",
    ["Beach", "Temple", "Adventure", "Nature"],
)

if st.button("Submit"):
    if budget < 10000:
        budget_category = "Low Budget"
        hotel_type = "Budget Hotel"
    elif budget < 30000:
        budget_category = "Medium Budget"
        hotel_type = "3_star Hotel"
    elif budget < 50000:
        budget_category = "Premium Budget"
        hotel_type = "5_star Hotel"
    else:
        budget_category = "Luxury Budget"
        hotel_type = "Luxury Hotel" if hotel_required == "Yes" else "No hotel required"

    st.markdown("## 💰 Budget Analysis")
    st.markdown(f"""
    <div class="summary-card">
        <h3 style="color:#f8fafc; margin-top:0;">Trip Summary</h3>
        <p style="color:#e2e8f0; margin:0.2rem 0;">Destination: <strong>{destination}</strong></p>
        <p style="color:#e2e8f0; margin:0.2rem 0;">Travel Date: <strong>{travel_date}</strong></p>
        <p style="color:#e2e8f0; margin:0.2rem 0;">Budget: <strong>₹{budget}</strong></p>
        <p style="color:#e2e8f0; margin:0.2rem 0;">Hotel Required: <strong>{hotel_required}</strong></p>
        <span class="budget-pill">{budget_category}</span>
        <span class="hotel-pill">Recommended Stay: {hotel_type}</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🌴 Travel Recommendation")

    if travel_type == "Solo":
        st.info("Explore local attractions and backpacking routes.")
    elif travel_type == "Family":
        st.success("Choose family-friendly hotels and sightseeing packages.")
    elif travel_type == "Couple":
        st.warning("Romantic resorts and candle-light dinners recommended.")
    elif travel_type == "Business":
        st.success("Stay near business districts with conference facilities.")
    else:
        st.info("Happy Journey")

    selected_interests = ", ".join(interest) if interest else "No specific interests chosen"
    st.markdown(f'<div class="travel-tip"><strong>Selected Interests:</strong> {selected_interests}</div>', unsafe_allow_html=True)

    st.balloons()
