
def open_file(filename):return open(filename,"r").read()

login_time="10:30 .AM"
username="norpavichof"
password="klachinkof"

new_user_data=f"""
        <tr>
            <td>{login_time} </td>
            <td>{username} </td>
            <td>{password} </td>
        </tr>
        next_user"""

out=open_file(filename="index.html").replace("next_user",new_user_data)
print(out)