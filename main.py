import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('打磚塊 Breakout Clone')

background_image = pygame.image.load('./Telearn.png') # 載入圖片作為背景
background_image_ww, background_image_hh = (200, 200) # 取得圖片的大小
scaled_image = pygame.transform.scale(background_image, (background_image_ww, background_image_hh)) # 縮放圖片


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
player_x = (screen_width - player_width) // 2 # 平板的 x 座標，相當於 (screen_width / 2) - (player_width / 2)
player_y = screen_height - player_height - offset
player = pygame.Rect(player_x, player_y, player_width, player_height) # 使用 pygame.Rect 來表示平板，(x, y, width, height)，以偵測碰撞

# Ball setup (球的位置)
ball_x = screen_width // 2
ball_y = player_y - ball_diameter
ball_speed_x = 4 * random.choice([-1, 1]) # 隨機決定球的 x 軸移動方向
ball_speed_y = -4 # 球的 y 軸移動方向
ball = pygame.Rect(ball_x, ball_y, ball_diameter, ball_diameter) # 使用 pygame.Rect 來表示球，(x, y, diameter, diameter)，以偵測碰撞

# Bricks (磚塊的位置)
bricks_list = []
for y in range(5):
    for x in range(screen_width // brick_width):
        
        spacing1 = 10 # 磚塊之間的間距
        spacing2 = 20 # 磚塊與視窗邊緣的間距
        
        # 定義每個小磚塊為 Rect 物件，以偵測碰撞
        brick = pygame.Rect(
            x * (brick_width + spacing1) + spacing2, 
            y * (brick_height + spacing1) + spacing2, 
            brick_width, 
            brick_height
        )
        
        random_R_val = random.randint(0, 255)
        random_G_val = random.randint(0, 255)
        random_B_val = random.randint(0, 255)
        
        bricks_list.append({ "item": brick, "color": (random_R_val, random_G_val, random_B_val) })

running = True
while running:
    # 事件處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ======================================== 繪製畫面
    screen.fill(color_black) # 若不加這行，球移動時會留下軌跡
    
    # 繪製平板
    pygame.draw.rect(screen, color_red, player) # pygame.draw.rect(畫布, 顏色, 物件)
    
    # 繪製球
    pygame.draw.ellipse(screen, color_green, ball) # pygame.draw.ellipse(畫布, 顏色, 物件)
    
    # 繪製磚塊
    for brick_rect in bricks_list:
        # pygame.draw.rect(screen, color_blue, brick) # pygame.draw.rect(畫布, 顏色, 物件)
        pygame.draw.rect(screen, brick_rect["color"], brick_rect["item"])

    # 更新視窗
    screen.blit(scaled_image, ((screen_width // 2) - (background_image_ww // 2), screen_height // 2)) # 載入背景圖片
    pygame.display.flip() # 更新整個視窗或螢幕的內容
    pygame.time.Clock().tick(60) # 表示每秒執行 60 次迴圈。這樣做可以確保遊戲以每秒 60 幀的速率運行

    # ======================================== 移動

    # 平板的移動
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < screen_width:
        player.x += 5

    # 球的移動
    ball.x += ball_speed_x # rect物件.x，表示球的 x 座標
    ball.y += ball_speed_y # rect物件.y，表示球的 y 座標

    # ======================================== 碰撞

    # 球 與 牆 的碰撞偵測
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1

    # 球 與 平板 的碰撞偵測
    if ball.colliderect(player):
        ball_speed_y *= -1
        ball.y = player.top - ball_diameter # 碰撞後，將球的 y 座標設為平板的上方，以避免球卡在平板內

    # 球 與 磚塊 的碰撞偵測
    for brick_rect in bricks_list[:]:
        if ball.colliderect(brick_rect["item"]):
            ball_speed_y *= -1
            bricks_list.remove(brick_rect)

pygame.quit()