first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

message = f"        Hello, {full_name.title()}!          "

print(message,"- tabs both")
print(message.rstrip(),"- right stripped")
print(message.lstrip(),"- left stripped")

message = message.lstrip()
message = message.rstrip()

print(message,"- final, both L & R stripped")