import random
import streamlit as st

# Function to assign roles
def assign_roles():
    players = ["Papa", "Mummy", "Suggi", "Suggu"]
    roles = ["Raja", "Chor", "Mantri", "Sipahi"]
    random.shuffle(roles)
    return dict(zip(players, roles))

# Initialize session state variables
if "assigned_roles" not in st.session_state:
    st.session_state.assigned_roles = assign_roles()
if "chor_guess" not in st.session_state:
    st.session_state.chor_guess = ""
if "result" not in st.session_state:
    st.session_state.result = None

# Define a function to reset the game
def reset_game():
    st.session_state.assigned_roles = assign_roles()
    st.session_state.chor_guess = ""
    st.session_state.result = None

# Fetch roles from session state
assigned_roles = st.session_state.assigned_roles
raja = [name for name, role in assigned_roles.items() if role == "Raja"][0]
sipahi = [name for name, role in assigned_roles.items() if role == "Sipahi"][0]
chor = [name for name, role in assigned_roles.items() if role == "Chor"][0]
mantri = [name for name, role in assigned_roles.items() if role == "Mantri"][0]

# Display Raja and Sipahi
st.title("Raja, Chor, Mantri, Sipahi Game")
st.write(f"**Raja:** {raja}")
st.write(f"**Sipahi:** {sipahi}")

# Input for guessing Chor
st.session_state.chor_guess = st.text_input("Sipahi, who do you think is the Chor?", st.session_state.chor_guess)

# Submit button to check guess
if st.button("Submit"):
    if st.session_state.chor_guess.strip() == chor:
        st.session_state.result = "Correct! You identified the Chor."
        st.success(st.session_state.result)
    else:
        st.session_state.result = "Wrong! That is not the Chor."
        st.error(st.session_state.result)
    st.write(f"**Mantri:** {mantri}")
    st.write(f"**Chor:** {chor}")

# Refresh button to restart the game
if st.button("Refresh Game"):
    reset_game()
    # No need for st.experimental_rerun(); Streamlit updates automatically when session state changes
