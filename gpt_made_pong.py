import os
import time
import keyboard
import random

# Define the size of the game board
WIDTH = 60
HEIGHT = 20


def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def move_ball(ball_pos, ball_dir):
    """Update ball position according to its direction."""
    ball_pos[0] += ball_dir[0]
    ball_pos[1] += ball_dir[1]


def move_paddle1(pad1_pos):
    """Move paddle 1 according to user's input."""
    if keyboard.is_pressed('w'):
        pad1_pos = max(0, pad1_pos - 1)
    elif keyboard.is_pressed('s'):
        pad1_pos = min(HEIGHT - 3, pad1_pos + 1)
    return pad1_pos


def move_paddle2(ball_pos, pad2_pos):
    """Move paddle 2 (AI) towards the ball."""
    if ball_pos[0] < pad2_pos:
        pad2_pos = max(0, pad2_pos - 1)
    elif ball_pos[0] > pad2_pos:
        pad2_pos = min(HEIGHT - 3, pad2_pos + 1)
    return pad2_pos


def check_collision_with_paddles(ball_pos, ball_dir, pad1_pos, pad2_pos):
    """Check if the ball collides with any of the paddles."""
    if ball_pos[1] == 1 and abs(ball_pos[0] - pad1_pos) <= 2:
        ball_dir[1] = 1
    elif ball_pos[1] == WIDTH - 2 and abs(ball_pos[0] - pad2_pos) <= 2:
        ball_dir[1] = -1


def check_collision_with_walls(ball_pos, ball_dir):
    """Check if the ball collides with the top or bottom wall."""
    if ball_pos[0] == 0 or ball_pos[0] == HEIGHT - 1:
        ball_dir[0] *= -1


def check_goal(ball_pos, score):
    """Check if a goal has been scored and update the score."""
    if ball_pos[1] == 0:
        score[1] += 1
        ball_pos = [HEIGHT // 2, WIDTH // 2]
        ball_dir = [random.choice([-1, 1]), random.choice([-1, 1])]
    elif ball_pos[1] == WIDTH - 1:
        score[0] += 1
        ball_pos = [HEIGHT // 2, WIDTH // 2]
        ball_dir = [random.choice([-1, 1]), random.choice([-1, 1])]


def print_game_board(ball_pos, pad1_pos, pad2_pos):
    """Print the game board."""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if i == ball_pos[0] and j == ball_pos[1]:
                print('-', end='')
            elif j == 0 and abs(i - pad1_pos) <= 2:
                print('I', end='')
            elif j == WIDTH - 1 and abs(i - pad2_pos) <= 2:
                print('I', end='')
            else:
                print(' ', end='')
        print()


def main():
    # Define the initial positions of the ball and the paddles
    ball_position = [HEIGHT // 2, WIDTH // 2]
    ball_direction = [random.choice([-1, 1]), random.choice([-1, 1])]
    paddle1_position = HEIGHT // 2
    paddle2_position = HEIGHT // 2

    # Define the score
    score = [0, 0]

    while True:
        clear_screen()

        move_ball(ball_position, ball_direction)
        paddle1_position = move_paddle1(paddle1_position)
        paddle2_position = move_paddle2(ball_position, paddle2_position)

        check_collision_with_paddles(ball_position, ball_direction, paddle1_position, paddle2_position)
        check_collision_with_walls(ball_position, ball_direction)
        check_goal(ball_position, score)

        print_game_board(ball_position, paddle1_position, paddle2_position)

        print('Score: {} - {}'.format(*score))

        if max(score) == 3:
            print('Game over!')
            break

        time.sleep(0.1)


if __name__ == "__main__":
    main()
