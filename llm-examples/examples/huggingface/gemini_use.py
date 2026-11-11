from gradio_client import Client, handle_file

client = Client("bytedance-research/USO")
result = client.predict(
    prompt="A beautiful woman.",
    image_prompt1=handle_file("https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png"),
    image_prompt2=handle_file("https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png"),
    image_prompt3=handle_file("https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png"),
    seed=-1,
    width=1024,
    height=1024,
    guidance=4,
    num_steps=25,
    keep_size=False,
    content_long_size=512,
    api_name="/gradio_generate",
)
print(result)
