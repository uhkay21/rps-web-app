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

demo.launch(share=True)
# This code creates a simple Rock, Paper, Scissors game using Gradio. The user can choose their move, and the bot randomly selects its move. The result is displayed along with the updated win, loss, and tie counts. The game is launched with a shareable link for easy access and interaction.
# The `play_game` function handles the game logic, comparing the user's choice with the bot's choice and updating the win/loss/tie counts accordingly. The Gradio interface is set up with a radio button for user input, a text box for displaying results, and buttons to play the game. The `gr.Blocks` context manager is used to organize the layout of the interface elements.
