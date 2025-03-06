import gradio as gr
import random

wins = 0
losses = 0
ties = 0

def play_game(user_choice):
    global wins, losses, ties
    choices = ["Rock", "Paper", "Scissors"]
    bot_choice = random.choice(choices)
    if user_choice == bot_choice:
        result = "It's a tie!"
        ties += 1
    elif (user_choice == "Rock" and bot_choice == "Scissors") or \
         (user_choice == "Paper" and bot_choice == "Rock") or \
         (user_choice == "Scissors" and bot_choice == "Paper"):
        result = "You win!"
        wins += 1
    else:
        result = "You lose!"
        losses += 1
    return f"Bot chose: {bot_choice}. {result}", wins, losses, ties

with gr.Blocks() as demo:
    gr.Markdown("## Rock, Paper, Scissors Game")
    user_choice = gr.Radio(choices=["Rock", "Paper", "Scissors"], label="Choose your move")
    result = gr.Textbox(label="Result")
    win_count = gr.Textbox(label="Wins", value="0")
    loss_count = gr.Textbox(label="Losses", value="0")
    tie_count = gr.Textbox(label="Ties", value="0")
    play_button = gr.Button("Play")

    play_button.click(play_game, inputs=user_choice, outputs=[result, win_count, loss_count, tie_count])

demo.launch()