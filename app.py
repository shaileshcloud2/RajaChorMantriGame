import random
import streamlit as st

def assign_roles():
    players = ["Papa", "Mummy", "Suggi", "Suggu"]
    roles = ["Raja", "Chor", "Mantri", "Sipahi"]
    random.shuffle(roles)
    return dict(zip(players, roles))

# Streamlit app
st.title("Raja, Chor, Mantri, Sipahi Game")

# Assign roles
if "assigned_roles" not in st.session_state:
    st.session_state.assigned_roles = assign_roles()

assigned_roles = st.session_state.assigned_roles

raja = [name for name, role in assigned_roles.items() if role == "Raja"][0]
sipahi = [name for name, role in assigned_roles.items() if role == "Sipahi"][0]
chor = [name for name, role in assigned_roles.items() if role == "Chor"][0]
mantri = [name for name, role in assigned_roles.items() if role == "Mantri"][0]

# Display Raja and Sipahi
st.write(f"**Raja:** {raja}")
st.write(f"**Sipahi:** {sipahi}")

# Input for guessing Chor
chor_guess = st.text_input("Sipahi, who do you think is the Chor?")

# Display result
if st.button("Submit"):
    if chor_guess.strip() == chor:
        st.success("Correct! You identified the Chor.")
    else:
        st.error("Wrong! That is not the Chor.")
    st.write(f"**Mantri:** {mantri}")
    st.write(f"**Chor:** {chor}")

# Refresh game
if st.button("Refresh Game"):
    st.session_state.assigned_roles = assign_roles()
    st.experimental_rerun()
