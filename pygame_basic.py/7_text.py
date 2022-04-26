import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Mura Game")  #게임 이름

# FPS
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\Lenovo\\Desktop\\pythonworkspace\\pygame_basic.py\\background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\Lenovo\\Desktop\\pythonworkspace\\pygame_basic.py\\character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) -(character_width/2) #화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래에 해당하는 곳 위치

#이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적_enermy캐릭터
enermy = pygame.image.load("C:\\Users\\Lenovo\\Desktop\\pythonworkspace\\pygame_basic.py\\enemy.png")
enermy_size = enermy.get_rect().size #이미지의 크기를 구해옴
enermy_width = enermy_size[0]
enermy_height = enermy_size[1]
enermy_x_pos = (screen_width/2) -(enermy_width/2) #화면 가로의 절반 크기에 해당하는 곳에 위치
enermy_y_pos = (screen_height/2) - (enermy_height/2) #화면 세로 크기 가장 아래에 해당하는 곳 위치

# 폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성(폰트, 크기)

# 총 시간
total_time = 10

#시간 계산
start_ticks = pygame.time.get_ticks() #시작 tick을 받아옴(시작시간 정보)

#이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정

    #캐릭터가 1초 동안 100만큼 이동해야함
    #10 fps : 1초 동안에 10번 동작 -> 1번에 몇 만큼 이동? 10만큼
    #20 fps : 1초 동안에 20번 동작 -> 1번에 몇 만큼? 5만큼
    # print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running = False #게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed # to_x = to_x - 5
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x *dt
    character_y_pos += to_y *dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
        

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enermy_rect = enermy.get_rect()
    enermy_rect.left = enermy_x_pos
    enermy_rect.top = enermy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enermy_rect):
        print("충돌했어요")
        running = False

    screen.blit(background, (0,0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    screen.blit(enermy, (enermy_x_pos, enermy_y_pos)) #적 그리기

    #타이머 집어 넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    #경과 시간(ms)을 1000으로 나누어서 초(s) 단위 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    # 시간, True, 글자 색상
    screen.blit(timer, (10,10))

    # 만약 시간이 0이하면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False



    pygame.display.update() #게임화면을 다시 그리기

# 잠시대기
pygame.time.delay(2000) #2초 대기

pygame.quit()