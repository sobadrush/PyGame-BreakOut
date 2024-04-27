import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('打磚塊 Breakout Clone')

# Define colors
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_green = (0, 255, 0)
color_blue = (0, 0, 255)

# Game variables
brick_width = 50 # 磚塊的寬度
brick_height = 20 # 磚塊的高度
player_width = 100 # 平板的寬度
player_height = 20 # 平板的高度
ball_diameter = 15 # 球的直徑
ball_radius = ball_diameter // 2 # 球的半徑

# Player paddle (平板的位置)
offset = 10
player_x = any # To-Be-Filled
player_y = any # To-Be-Filled
player = pygame.Rect(player_x, player_y, player_width, player_height) # 使用 pygame.Rect 來表示平板，(x, y, width, height)，以偵測碰撞

# Ball setup (球的位置)
ball_x = any # To-Be-Filled
ball_y = any # To-Be-Filled
ball_speed_x = 4 * random.choice([-1, 1]) # 隨機決定球的 x 軸移動方向
ball_speed_y = -4 # 球的 y 軸移動方向
ball = pygame.Rect(ball_x, ball_y, ball_diameter, ball_diameter) # 使用 pygame.Rect 來表示球，(x, y, diameter, diameter)，以偵測碰撞

# Bricks (磚塊的位置)
bricks = []
# 使用 for 迴圈來建立磚塊 List
# To-Be-Filled
# To-Be-Filled
# To-Be-Filled

running = True
while running:
    # 事件處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ======================================== 繪製畫面
    # To-Be-Filled: BUG-FIX
    
    # 繪製平板
    # To-Be-Filled, 提示：使用 pygame.draw.rect 來繪製平板
    
    # 繪製球
    # To-Be-Filled, 提示：使用 pygame.draw.ellipse 來繪製球
        
    # 繪製磚塊, 根據 「磚塊 List」+ 迴圈 來繪製磚塊
    # To-Be-Filled: 提示：使用 pygame.draw.rect 來繪製磚塊

    # 更新視窗
    pygame.display.flip() # 更新整個視窗或螢幕的內容
    pygame.time.Clock().tick(60) # 表示每秒執行 60 次迴圈。這樣做可以確保遊戲以每秒 60 幀的速率運行

    # ======================================== 移動

    # 平板的移動
    keys = pygame.key.get_pressed()
    # 平板的左移
    if keys[pygame.K_LEFT] and any: # To-Be-Filled，請將條件補全
        player.x -= 5
    # To-Be-Filled: 平板的右移

    # 球的移動
    ball.x += ball_speed_x # rect物件.x，表示球的 x 座標
    ball.y += ball_speed_y # rect物件.y，表示球的 y 座標

    # ======================================== 碰撞

    # 球 與 牆 的碰撞偵測
    if any or any: # To-Be-Filled: 球的 x 座標到達左右邊界時，將球的 x 軸移動方向反轉
        any # To-Be-Filled: 球的 x 座標到達左右邊界時，將球的 x 軸移動方向反轉
    if ball.top <= 0:
        any # To-Be-Filled: 球的 y 座標到達上邊界時，將球的 y 軸移動方向反轉

    # 球 與 平板 的碰撞偵測
    if ball.colliderect(player):
        any # To-Be-Filled: 碰撞後，將球的 y 軸移動方向反轉
        ball.y = player.top - ball_diameter # 碰撞後，將球的 y 座標設為平板的上方，以避免球卡在平板內

    # 球 與 磚塊 的碰撞偵測
    for brick in bricks[:]:
        if any: # To-Be-Filled: 球與磚塊碰撞偵測
            any # To-Be-Filled: 碰撞後，將球的 y 軸移動方向反轉
            any # To-Be-Filled: 碰撞後，移除磚塊

pygame.quit()