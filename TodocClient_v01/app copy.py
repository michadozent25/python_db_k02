import streamlit as st

import requests

BASE_URL = "http://127.0.0.1:8000"  # uvicorn-> restapi


st.title("Neues Todo")
user_id = st.number_input("User-Id",min_value=1,step=1,format="%d")
task = st.text_input("Task")
description=st.text_input("Description")
deadline=st.date_input("Deadline",format="DD.MM.YYYY")
state = st.selectbox("State",["OPEN","IN_PROGRESS","DONE"])


json_param={
    "task":task,
    "description":description,
    "deadline":deadline.isoformat(),
    "state":state
}

try:
    if st.button("Todo erstellen"):
        # http:/localhost:8000/todo?user_id=1
        response = requests.post(f"{BASE_URL}/todo/", json=json_param, params={"user_id":user_id})
        #response = requests.post(f"{BASE_URL}/todos/",json=json_param, params={"user_id":user_id} )
  #
        st.text(response.status_code)
        if response.status_code==200:
            st.success("Todo gespeichert")
            st.json(response.json())
            st.table(response.json())
        else:
            st.info("keine Todos")

except requests.exceptions.RequestException as e:
    print("Server nicht erreichbar: {e}")