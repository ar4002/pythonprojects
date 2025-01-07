from openai import OpenAI
 

client = OpenAI(
  api_key="<Your Key Here>",
)

command = '''
[20:30, 12/6/2024] Goku: jo sunke coding ho sake?
[20:30, 12/6/2024] RamDas: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:30, 12/6/2024] RamDas: ye
[20:30, 12/6/2024] RamDas: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:31, 12/6/2024] Goku: This is hindi
[20:31, 12/6/2024] Goku: send me some english songs
[20:31, 12/6/2024] Goku: but wait
[20:31, 12/6/2024] Goku: this song is amazing
[20:31, 12/6/2024] Goku: so I will stick to it
[20:31, 12/6/2024] Goku: send me some english song also
[20:31, 12/6/2024] RamDas: hold on
[20:31, 12/6/2024] Goku: I know what you are about to send
[20:32, 12/6/2024] Goku: 😂😂
[20:32, 12/6/2024] RamDas: https://www.youtube.com/watch?v=ar-3chBG4NU
ye hindi English mix hai but best hai
[20:33, 12/6/2024] Goku: okok
[20:33, 12/6/2024] RamDas: Haan
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named harry who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Harry"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)
