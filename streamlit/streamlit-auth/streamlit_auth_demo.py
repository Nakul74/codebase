import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
    
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

def update_config_file():
    with open('config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)

name, authentication_status, username = authenticator.login('Login', 'main')

choice_placeholder = st.sidebar.empty()
c = choice_placeholder.radio(label='Choose', options=['Login', 'Signup'], index=0)
if (c == 'Login'):
    if st.session_state["authentication_status"]:
        choice_placeholder.empty()
        authenticator.logout('Logout', 'sidebar')
        st.write(f'Welcome *{st.session_state["name"]}*')
        st.title('Some content')
        if st.session_state["authentication_status"]:
            try:
                if authenticator.update_user_details(st.session_state["username"], 'Update user details'):
                    st.success('Entries updated successfully')
                    update_config_file()
            except Exception as e:
                st.error(e)
        
    elif st.session_state["authentication_status"] == False:
        st.error('Username/password is incorrect')
        try:
            username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password('Forgot password')
            if username_of_forgotten_password:
                st.success('New password to be sent securely')
                update_config_file()
            else:
                st.error('Username not found')
        except Exception as e:
            st.error(e)
            
        try:
            username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username('Forgot username')
            if username_of_forgotten_username:
                st.success('Username to be sent securely')
                update_config_file()
            else:
                st.error('Email not found')
        except Exception as e:
            st.error(e)
    elif st.session_state["authentication_status"] == None:
        st.warning('Please enter your username and password')
else:
    try:
        if authenticator.register_user('Register user', preauthorization=False):
            st.success('User registered successfully')
            update_config_file()
    except Exception as e:
        st.error(e)