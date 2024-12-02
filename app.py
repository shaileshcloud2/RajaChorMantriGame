import random
import streamlit as st

# Function to assign roles
def assign_roles():
    players = ["Papa", "Mummy", "Suggi", "Suggu"]
    roles = ["Raja", "Chor", "Mantri", "Sipahi"]
    random.shuffle(roles)
    return dict(zip(players, roles))

# Initialize session state for assigned_roles
if "assigned_roles" not in st.session_state:
    st.session_state.assigned_roles = assign_roles()

def reset_game():
    # Reassign roles and reset game state
    st.session_state.assigned_roles = assign_roles()
    st.session_state.result = None
    st.session_state.chor_guess = ""

# Fetch assigned roles
assigned_roles = st.session_state.assigned_roles

# Identify Raja, Sipahi, Mantri, and Chor
raja = [name for name, role in assigned_roles.items() if role == "Raja"][0]
sipahi = [name for name, role in assigned_roles.items() if role == "Sipahi"][0]
chor = [name for name, role in assigned_roles.items() if role == "Chor"][0]
mantri = [name for name, role in assigned_roles.items() if role == "Mantri"][0]

# Display Raja and Sipahi
st.title("Raja, Chor, Mantri, Sipahi Game")
st.write(f"**Raja:** {raja}")
st.write(f"**Sipahi:** {sipahi}")

# Text input for guessing Chor
if "chor_guess" not in st.session_state:
    st.session_state.chor_guess = ""
st.session_state.chor_guess = st.text_input("Sipahi, who do you think is the Chor?", st.session_state.chor_guess)

# Check the result on Submit
if st.button("Submit"):
    if st.session_state.chor_guess.strip() == chor:
        st.session_state.result = "Correct! You identified the Chor."
        st.success(st.session_state.result)
    else:
        st.session_state.result = "Wrong! That is not the Chor."
        st.error(st.session_state.result)
    st.write(f"**Mantri:** {mantri}")
    st.write(f"**Chor:** {chor}")

# Refresh Game Button
if st.button("Refresh Game"):
    reset_game()
    st.experimental_rerun()

