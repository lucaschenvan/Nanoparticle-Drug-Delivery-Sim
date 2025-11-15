import streamlit as st
import numpy as np

def main():
    st.title("Nanoparticle Drug Delivery Simulator")

    st.markdown(
        "Explore how changing nanoparticle size, surface coating, and environment pH can affect how fast a drug is released. "
        "This is a simplified toy model for learning, not a real medical tool."
    )

    st.subheader("1. Choose nanoparticle properties")

    size_nm = st.slider(
        "Nanoparticle size (nm)",
        min_value=10,
        max_value=500,
        value=100,
        step=10
    )

    coating = st.selectbox(
        "Surface coating",
        ["Bare particle", "PEG coating", "Antibody targeting", "Lipid shell"]
    )

    ph = st.slider(
        "Environment pH",
        min_value=4.0,
        max_value=8.0,
        value=7.4,
        step=0.1
    )

    st.subheader("2. Your current settings")
    st.write(f"Size: {size_nm} nm")
    st.write(f"Coating: {coating}")
    st.write(f"pH: {ph}")

    st.markdown(
        "General intuition: smaller particles and acidic environments usually speed up release. "
        "Protective coatings like PEG often slow things down, while targeting coatings can change how and where release happens."
    )

    st.subheader("3. Simulated drug release over 24 hours")

    time_hours = np.linspace(0, 24, 100)

    base_k = 0.15

    size_factor = 100 / size_nm

    if coating == "Bare particle":
        coating_factor = 1.2
        coating_text = "Bare particles release faster because there is no protective shell."
    elif coating == "PEG coating":
        coating_factor = 0.7
        coating_text = "PEG coating often makes particles stealthy and slows down release."
    elif coating == "Antibody targeting":
        coating_factor = 0.9
        coating_text = "Antibody targeting aims the particles at specific cells, with a slightly slower release."
    else:
        coating_factor = 1.0
        coating_text = "A lipid shell behaves somewhat like a tiny fat bubble around the drug."

    if ph < 6.5:
        ph_factor = 1.3
        ph_text = "Low pH (more acidic) speeds up release. Many tumors and inflamed tissues are slightly acidic."
    elif ph > 7.5:
        ph_factor = 0.8
        ph_text = "High pH slows release in this toy model."
    else:
        ph_factor = 1.0
        ph_text = "Near neutral pH, similar to healthy blood, gives a baseline release speed."

    k = base_k * size_factor * coating_factor * ph_factor

    fraction_released = 1 - np.exp(-k * time_hours)

    release_data = {
        "Time (hours)": time_hours,
        "Fraction released": fraction_released
    }

    st.line_chart(release_data, x="Time (hours)", y="Fraction released")

    st.subheader("4. How to read this chart")

    st.markdown(
        "The curve shows the fraction of drug that has been released from the nanoparticles over 24 hours. "
        "A curve that rises quickly means fast release. A flatter curve means slow, sustained release."
    )

    st.markdown(
        f"- Size factor: smaller particles release faster. At {size_nm} nm, the model speeds release by a factor of {round(size_factor, 2)} compared to 100 nm.\n"
        f"- Coating effect: {coating_text}\n"
        f"- pH effect: {ph_text}\n\n"
        "Real nanomedicine research uses much more complex models and experiments. This simulator is meant to build intuition, "
        "not to design real treatments."
    )

if __name__ == "__main__":
    main()

