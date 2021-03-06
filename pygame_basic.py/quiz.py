# Quiz)하늘에서 떨어지는 똥 피하기 게임을 만드시오

# [게임조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤하게 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS는 30으로 고정

# [게임 이미지]
# 1. 배경 : 640 * 480 (세로 * 가로) - backgroud.png
# 2. 캐릭터 : 70*70 - character.png
# 3. 똥 : 70 * 70 - enermy.png

import pygame
import random
###########################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("똥 피하기")  #게임 이름

# FPS
clock = pygame.time.Clock()
###########################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load("C:\\Users\\Lenovo\\Desktop\\pythonworkspace\\pygame_basic.py\\background_quiz.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\Lenovo\\Desktop\\pythonworkspace\\pygame_basic.py\\character_puiz.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) -(character_width/2) #화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래에 해당하는 곳 위치

#캐릭터 스피드
character_speed = 0.6

to_x = 0


# 적_똥 캐릭터
ddong = pygame.image.load("C:\\Users\\Lenovo\\Desktop\\pythonworkspace\\pygame_basic.py\\enemy_ddong.png")
ddong_size = enermy.get_rect().size #이미지의 크기를 구해옴
ddong_width = enermy_size[0]
ddong_height = enermy_size[1]
ddong_x_pos = randint[1:480] #화면 가로의 절반 크기에 해당하는 곳에 위치
ddong_y_pos = 0 #화면 세로 크기 가장 아래에 해당하는 곳 위치


running = True #게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed # to_x = to_x - 5
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

    # 4. 충돌 처리
    
    # 5. 화면에 그리기
    screen.blit(background, (0,0)) #배경 그리기
    
    screen.blit(character, (character_x_pos,character_y_pos)) #캐릭터 그리기

    pygame.display.update() #게임화면을 다시 그리기

pygame.quit()

## 이부분 추가했음
