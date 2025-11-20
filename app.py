import pandas as pd

if st.button("🔮 Predict Usage"):
    input_df = pd.DataFrame([{
        "num_rooms": num_rooms,
        "num_people": num_people,
        "housearea": housearea,
        "is_ac": is_ac,
        "is_tv": is_tv,
        "is_flat": is_flat,
        "num_children": num_children,
        "is_urban": is_urban,
        "amount_paid": amount_paid
    }])

    prediction = model.predict(input_df)
    st.success(f"Estimated Monthly Electricity Usage: {prediction[0]:.2f} units ⚡")
