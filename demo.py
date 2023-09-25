

import streamlit as st

import snowflake.connector

 

# Define admin credentials

admin_credentials = {

    "admin_username": "admin_password"

}

 

def authenticate(username, password):

    """Authenticate admin users."""

    if username in admin_credentials and admin_credentials[username] == password:

        return True

    return False

 

def main():

    st.title("Admin Login")

 

    username = st.text_input("Username")

    password = st.text_input("Password", type="admin")

 

    if st.button("Login"):

        if authenticate(username, password):

            st.success("Login successful. Redirecting to admin panel...")

 

            # You can add a session token or other authentication mechanism here

 

            # Redirect to the admin panel

            admin_panel()

 

        else:

            st.error("Invalid username or password")

 

def admin_panel():

    st.title("Snowflake Admin Page")

 

    # Snowflake credentials

    SNOWFLAKE_ACCOUNT = "your_account_url"

    SNOWFLAKE_USER = "your_username"

    SNOWFLAKE_PASSWORD = "your_password"

    SNOWFLAKE_DATABASE = "your_database"  # Optional

    SNOWFLAKE_SCHEMA = "your_schema"      # Optional

 

    # Connect to Snowflake

    conn = snowflake.connector.connect(

        "account": "xh84085.ap-southeast-1",

    "user": "sravani12",

    "password": "Sravani@12",

    "role": "accountadmin",

    "warehouse": "COMPUTE_WH",

    "database": "UTIL_DB",

    "schema": "ADMIN_TOOLS"

    )

    cursor = conn.cursor()

 

    # Add the Snowflake admin interface here

 

    if st.button("Logout"):

        conn.close()

        st.write("Snowflake connection closed.")

        st.write("Streamlit app closed.")

 

if __name__ == "__main__":

    main()

 